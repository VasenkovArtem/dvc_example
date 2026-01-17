import argparse

from datasets import load_dataset

DATASET_PATH = 'data/data.csv'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--name',
        help='dataset name',
        required=True,
        type=str,
    )
    parser.add_argument(
        '--rows',
        help='number of rows',
        required=False,
        default=1000,
        type=int,
    )
    args = parser.parse_args()
    dataset = load_dataset(args.name, split=f'train[:{args.rows}]')
    dataset.to_csv(DATASET_PATH)


if __name__ == '__main__':
    main()
