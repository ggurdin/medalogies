"""
Medalogies' command line interface
"""

import argparse
from medalogies.write_stats import write_stats
from medalogies.train_embeddings import train_embeddings


def stats(args):
    data_file = args.data
    output_file = args.output
    write_stats(data_file, output_file)


def embeddings(args):
    directory = args.directory
    output_file = args.output
    train_embeddings(directory, output_file)


def main():
    # Argparse setup
    parser = argparse.ArgumentParser(prog='medalogies', description='Medical Word Embeddings.')
    subparsers = parser.add_subparsers()

    # Stats arguments
    parser_stats = subparsers.add_parser('stats', help='Collect stats about a dataset.')
    parser_stats.add_argument('-d', '--data', help='Path to data file', required=True)
    parser_stats.add_argument('-o', '--output', help='Path to output stats file', required=True)
    parser_stats.set_defaults(func=stats)

    # Stats arguments
    parser_train = subparsers.add_parser('train', help='Train word embeddings.')
    parser_train.add_argument('-d', '--directory', help='Path to directory of text files', required=True)
    parser_train.add_argument('-o', '--output', help='Path to output embeddings', required=True)
    parser_train.set_defaults(func=embeddings)

    # Parse initial args
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
