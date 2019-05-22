from settings import data_dir, output_dir
import numpy as np
import pandas as pd
from os.path import join
import argparse
import warnings
warnings.filterwarnings('ignore')


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--csv", type=str, required=True)
    argument_parser.add_argument("--xlsx", type=str, required=True)
    argument_parser.add_argument("--out", type=str, default='aggreagte.xlsx')

    parse_args = argument_parser.parse_args()
    csv_file = join(data_dir, parse_args.csv)
    xlsx_file = join(data_dir, parse_args.xlsx)
    
    csv_df = pd.read_csv(csv_file)
    xlsx_df = pd.read_excel(xlsx_file)

    csv_key = "Ad Set ID"
    xlsx_key = "Ad set ID"

    keys = list(xlsx_df[xlsx_key])

    cities = []
    regions = []

    for key in keys:
        row = csv_df[csv_df[csv_key] == f'c:{key}']
        city_val = row.Cities.values[0]
        reg_val = row.Regions.values[0]
        regions.append(reg_val)

        if not isinstance(city_val, str):
            cities.append(city_val)
        elif ';' in city_val:
            cities.append('Multiple Cities')
        else:
            cities.append(city_val)

    xlsx_df['Cities'] = cities
    xlsx_df['Regions'] = regions

    unique_cities = set(cities)
    unique_cities.remove(np.nan)
    unique_regions = set(regions)
    unique_regions.remove(np.nan)

    android_install = []
    ios_install = []

    android_xlsx = xlsx_df[xlsx_df['Campaign name'].map(lambda x: 'Android' in x)]
    ios_xlsx = xlsx_df[xlsx_df['Campaign name'].map(lambda x: 'IOS' in x)]

    for xlsx, platform in zip([android_xlsx, ios_xlsx], ['android', 'ios']):
        city_aggregate_results = []
        for city in unique_cities:
            queries = xlsx[xlsx.Cities == city]
            city_aggregate_results.append(
                (city, queries['Amount spent (INR)'].sum(), queries.Results.sum()))
        
        try:
            region_aggregate_results = []
            for region in unique_regions:
                queries = xlsx_df[xlsx.Regions == region]
                region_aggregate_results.append(
                    (region, queries['Amount spent (INR)'].sum(), queries.Results.sum()))
        except pd.core.indexing.IndexingError:
            pass

        aggregate_result = city_aggregate_results + region_aggregate_results


        df = pd.DataFrame(aggregate_result, columns=[
                        "Cities", 'Amount spent (INR)', 'Results'])

        out_file = join(output_dir, f'{platform}_{parse_args.out}')
        df.to_excel(out_file)
