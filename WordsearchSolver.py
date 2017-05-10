import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordsearch', help='File location of wordsearch, is required', required=True)
parser.parse_args()
