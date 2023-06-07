import os
import csv
import argparse

from decouple import config
from methods.google_geocode import GoogleGeocodeUtil
from methods.levenshtein_distance import LevenshteinDistUtil
doc = """
Small experimental project to play with different methods for address matching. 
There are two methods used:
Google geocode - ( main.py -m gl ) using google service directly it recognize itself place_id and group on it.
Levenshtein distance - ( main.py -m ld ) using translated to EN address and calc similarity
"""

GOOLEMAPS_API_KEY = config('GOOLEMAPS_API_KEY')
GOOGL_METHOD = 'gl'
LEVENSHTEIN_METHOD = 'ld'
LEVENSHTEIN_METHOD_RATIO_LIMIT = 0.656789
DEFAULT_INPUT_CSV = 'resources/ResTecDevTask-sample_input_v1.csv'
DEFAULT_OUTPUT_CSV = 'output/ResTecDevTask_output.csv'
DEFAULT_EN_LV_INPUT_CSV = 'output/ResTecDevTask-sample_input_v1_EN.csv'

parser = argparse.ArgumentParser(
                    prog='Rzn Address Grouping Utility',
                    description=doc,
                    epilog='')

parser.add_argument('-i', '--input_csv',
                    default=config('MATCH_INPUT_CSV', default=DEFAULT_INPUT_CSV))
parser.add_argument('-o', '--output_csv',
                    default=config('MATCH_OUTPUT_CSV', default=DEFAULT_OUTPUT_CSV))
parser.add_argument('-m', '--method', default=GOOGL_METHOD)
parser.add_argument('-v', '--verbose', action='store_true', default=False)


def method_google_geocode(input_file_name: str) -> list:
    g = GoogleGeocodeUtil(api_key=GOOLEMAPS_API_KEY)
    result: list = g.from_csv(input_file_name=input_file_name)
    return result


def method_levenshtein_distance(input_file_name: str) -> list:
    return LevenshteinDistUtil(
        acceptance_ratio_limit=LEVENSHTEIN_METHOD_RATIO_LIMIT
    ).from_csv(input_file_name)


def write_csv(result: list, output_path_file: str):
    with open(output_path_file, 'w+') as out_fp:
        writer = csv.writer(out_fp)
        for entry in result:
            writer.writerow((entry,))


def read_csv(output_path_file: str, verb: bool):
    with open(output_path_file, 'r') as out_fp:
        reader = csv.reader(out_fp)
        for entry in reader:
            if verb:
                print(entry[0])


def main():
    main_args = parser.parse_args()
    method_map = {
        GOOGL_METHOD: (method_google_geocode, (main_args.input_csv,), {}),
        LEVENSHTEIN_METHOD: (method_levenshtein_distance, (main_args.input_csv,), {}),
    }
    method = main_args.method
    if method in method_map:
        func, args, kwargs = method_map[method]
        print('Method selected: ', method, func, args, kwargs)
        res = func(*args, **kwargs)
        write_csv(res, output_path_file=main_args.output_csv)
        if main_args.verbose:
            print('Following matching result accumulated:')
            print('------------------------')
            read_csv(output_path_file=main_args.output_csv, verb=main_args.verbose)
            print('------------------------')
    else:
        print(f'Unknown method {method}')
        print('Please use gl (google_api) or ld (levenshtein distance)')


if __name__ == '__main__':
    main()
