"""
Medalogies' command line interface
"""

import argparse
from medalogies.write_stats import write_stats


def stats(args):
    data_file = args.data
    output_file = args.output
    write_stats(data_file, output_file)


def main():
    # Argparse setup
    parser = argparse.ArgumentParser(prog='medalogies', description='Medical Word Embeddings.')
    subparsers = parser.add_subparsers()

    # Stats arguments
    parser_stats = subparsers.add_parser('stats', help='Collect stats about a dataset.')
    parser_stats.add_argument('-d', '--data', help='Path to data file', required=True)
    parser_stats.add_argument('-o', '--output', help='Path to output stats file', required=True)
    parser_stats.set_defaults(func=stats)

    # Parse initial args
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
