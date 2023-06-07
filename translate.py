import csv
import argparse
import csv
from decouple import config
from langdetect import detect as lang_detect
from googletrans import Translator
from logging import getLogger
doc = """
Translate csv to EN language
"""

logger = getLogger()

DEFAULT_INPUT_CSV = 'resources/ResTecDevTask-sample_input_v1.csv'
DEFAULT_OUTPUT_CSV = 'output/ResTecDevTask-sample_input_v1_EN.csv'


parser = argparse.ArgumentParser(
                    prog='Rzn Address Translatein Utility',
                    description=doc,
                    epilog='')

parser.add_argument('-i', '--input_csv',
                    default=config('TRANSLATE_DEFAULT_INPUT_CSV', DEFAULT_INPUT_CSV))      # option that takes a value
parser.add_argument('-o', '--output_csv',
                    default=config('TRANSLATE_DEFAULT_OUTPUT_CSV', DEFAULT_OUTPUT_CSV))

main_args = parser.parse_args()


def main():
    with open(main_args.input_csv) as fp:
        reader = csv.reader(fp)
        with open(main_args.output_csv, 'w+') as out_fp:
            writer = csv.writer(out_fp)
            t = Translator()
            next(reader)
            for name, address in reader:
                detected_language = lang_detect(address)
                if detected_language != 'en':
                    translated = t.translate(address, src=detected_language, dest='en')
                    address = translated.text
                writer.writerow((name, address))


if __name__ == '__main__':
    print(f'Translating csv from: {main_args.input_csv}')
    main()
    print(f'Translate output saved to: {main_args.output_csv}')

