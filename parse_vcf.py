import gzip
from collections import defaultdict
import pandas as pd
import sys

d = defaultdict(list)

def parse_vcf(vcf_file):
    """This function will create a dict(associative array) of lists coming from the INFO field in the vcf file,
    it will then return another function which will create a dataframe.
    Please use this file in this manner from the command line write python parse_vcf <variant_file> <output_file_name>"""
    with gzip.open(vcf_file,'rt',encoding='utf-8') as file:
        for line in file:
            if not line.startswith(('13','chr13')):
                continue
            pos = int(line.split('\t')[1])
            info_array = line.strip().split('\t')[7].split(';')
            if 26000000 <= pos <= 36000000:
                for element in info_array:
                    if '=' in element:
                        key,value = element.split('=')[0],element.split('=')[1]
                        d[key].append(value)
    # transform dictionary in order to get the gene symbol and the first molecular component description
        get_MC = []
        get_GENEINFO = []
        for k,v in d.items():
            if k == 'MC':
                for x in v:
                    split = x.split(',')[0].split('|')[1]
                    get_MC.append(split)
            if k == 'GENEINFO':
                for x in v:
                    split = x.split(':')[0]
                    get_GENEINFO.append(split)
        d['MC'] = get_MC
        d['GENEINFO'] = get_GENEINFO
    # call another func that will create a dataframe out of dict
    df = create_df(d)
    return df
    

def create_df(df):
    df = pd.DataFrame.from_dict(d,orient='index').transpose()
    df = df[['CLNSIG','GENEINFO','MC']]
    df = df.loc[df['CLNSIG'].isin(['Pathogenic','Likely_pathogenic','Pathogenic/Likely_pathogenic'])]
    df.dropna(inplace=True)
    df = pd.crosstab(df.GENEINFO, df.MC)
    df.to_csv(name_of_file,sep='\t')
    return df


def main():
    result = parse_vcf(file)
    return result
    
if __name__=='__main__':
    file = sys.argv[1]
    name_of_file = sys.argv[2]
    main()
