import pandas as pd

'''
Split a large csv into smaller csv(s)
input: df object of a csv, number of splits, prefix of the output files
output: multiple splitted csv files
'''


def split_csv(df, num_of_split, output_prefix):
    total_num_rows = len(df.index)
    split_size = total_num_rows // num_of_split
    split_remainder = total_num_rows % num_of_split

    if split_size <= 0:
        raise Exception(
            "Number of split should be positive and smaller than the total number of rows of df!")

    # larger splits (contains less)
    csv_paths = []
    current_row = 0
    i = 0
    for i in range(1, split_remainder+1):
        df.iloc[current_row:(current_row + split_size + 1)
                ].to_csv(f'{output_prefix}_{i}.csv')
        current_row += split_size + 1
        csv_paths.append(f'{output_prefix}_{i}.csv')

    # smaller splits
    for j in range(i+1, num_of_split + 1):
        df.iloc[current_row:(current_row + split_size)
                ].to_csv(f'{output_prefix}_{j}.csv')
        current_row += split_size
        csv_paths.append(f'{output_prefix}_{j}.csv')

    return csv_paths


if __name__ == "__main__":
    df = pd.read_csv('train.csv', index_col=0)

    n = 10
    print(f'Splitting csv into {n} csv(s)')
    csv_paths = split_csv(df, n, "train")

    total_rows = len(df.index)

    split_rows = 0
    for i in csv_paths:
        new_df = pd.read_csv(i, index_col=0)
        split_rows += len(new_df.index)
        print(f'Saved {len(new_df.index)} rows at {i}')

    print(f'{split_rows} rows are saved')
    assert (total_rows == split_rows)
