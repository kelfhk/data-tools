import pandas as pd

'''
Drop index of a csv
input: df object of a csv with index column
output: a csv without index column
'''


def drop_csv_index(df, output_file='without_index.csv'):
    df.to_csv(output_file, index=False)
    print(f'Saved drop_csv_index output at {output_file}')


if __name__ == "__main__":
    input_file = "train.csv"
    df = pd.read_csv(input_file, index_col=0)

    drop_csv_index(df)
