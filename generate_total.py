from argparse import ArgumentParser
from glob import glob
from os.path import join
import pandas as pd

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    # give the full path of input folder
    argument_parser.add_argument('--inputdir', type=str, required=True)
    # give the full path of output file name
    argument_parser.add_argument('--outfile', type=str, default='output.xlsx')

    parse_args = argument_parser.parse_args()
    input_dir = parse_args.inputdir
    outfile = parse_args.outfile

    xlsx_files = glob(join(input_dir, "*.xlsx"))
    result_df = pd.DataFrame(columns=['Cities', 'Amount spent (INR)', 'Results'])

    for file in xlsx_files:
        df = pd.read_excel(file, use_cols=['Cities', 'Amount spent (INR)', 'Results'])
        result_df = result_df.append(df, ignore_index=True, sort=False)

    unique_cities = result_df.Cities.unique()
    
    output_container = []

    for city in unique_cities:
        aggregate_result = result_df[result_df.Cities == city]
        result = aggregate_result[['Amount spent (INR)', 'Results']].sum()
        result["Cities"] = city
        output_container.append(result)
    
    output = pd.DataFrame(output_container)
    output.to_excel(outfile)