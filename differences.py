import sys
import pandas as pd
import gzip

def compare_files(file1,file2):
    df1 = pd.read_csv(file1,sep='\t')
    df2 = pd.read_csv(file2,sep='\t')
    # Column differences
    print('\n')
    name = df1.columns.difference(df2.columns)
    name = 0 if name.size == 0 else name
    print(f'File1 has {name} variant type differences with File2')
    print('\n')
    # Gene differences
    gd = pd.concat([df1,df2]).drop_duplicates(subset = ['GENEINFO','GENEINFO'],keep=False)
    gd = gd['GENEINFO'].to_numpy()
    print(f'These are gene differences between both datasets: {gd}')
    print('\n')
    # Sum of all variant types for file 1
    s = df1.iloc[:,2:].to_numpy().sum()
    print(f'Sum of all variants for file 1 is: {s}')
    print('\n')
    # Sum of all variant types for file 2
    s = df2.iloc[:,2:].to_numpy().sum()
    print(f'Sum of all variants for file 2 is: {s}')
    print('\n')

def main():
    result = compare_files(file1, file2)
    return result


if __name__=='__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    main()