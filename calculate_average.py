from os.path import join
from collections import Counter
from argparse import ArgumentParser
import pandas as pd
from settings import data_dir, output_dir


def get_regions(city_str):
    try:
        return city_str.split(',')[1].strip()
    except IndexError:
        return city_str.replace(' IN', '')
    
if __name__=="__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--city', type=str, required=True)
    argument_parser.add_argument('--data', type=str, required=True)
    argument_parser.add_argument('--out', type=str, default="avg_result.xlsx")
    
    parse_args = argument_parser.parse_args()
    city_xlsx = join(data_dir, parse_args.city)
    data_xlsx = join(data_dir, parse_args.data)
    outfile = join(output_dir, parse_args.out)
    
    city_df = pd.read_excel(city_xlsx, header=1)
    data_df = pd.read_excel(data_xlsx, header=0)
    
    city_df['Regions'] = city_df.City.apply(get_regions)

    state_counter = Counter(city_df.Regions)

    unique_regions = list(data_df.Region)

    state_count = []
    for region in unique_regions:
        state_count.append(state_counter[region])

    data_df['RegionCount'] = state_count
    data_df['AvgResults'] = round(data_df['Results'] / data_df['RegionCount'], 2)
    data_df['AvgSpent'] = round(data_df['Amount spent (INR)'] / data_df['RegionCount'], 2)

    data_df.to_excel(outfile)