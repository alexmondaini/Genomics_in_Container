# This is a general exercise in genomics where I have analyzed variant(vcf) and bed files to get their summary statistics and parse vcfs in order to detect the frequency of  annotated labels denoted in variant files with a python dictionary structure.


## Let's get started by asking some questions about about bed/vcf files that are located in this repo:

### Get the summary statistics of the ClinVar variants on target regions.
**Input**: 
1. a target file (.bed format) contains multiple regions from chr13:26000000-36000000 of human reference genome GRCh37 (hg19): grch37.testregion.bed
2. Refseq exon list file (.bed format) for all human coding genes, the position is also based on GRCh37: grch37.exon_info_refseq.bed

### For variant input file __*clinvar.vcf.gz*__ derive the following objectices:

1. For all genes located in chr13:26000000-36000000, get the summary statistics of the target file coverage. (For each gene, get the fraction of exonic bases that was covered by the target file)
2. For all the ClinVar variants that are located in this region: chr13:26000000-36000000, get the number of the variants with key: CLNSIG is “Pathogenic” or “Likely_pathogenic” or “Pathogenic/Likely_pathogenic” for each gene (key:GENEINFO in INFO section of vcf file) and each molecular consequence (key:MC in INFO section of vcf file).
3. For all the ClinVar variants that are located in the target region file (grch37.testregion.bed), generate a similar table as in Objective 2, and identify the major differences between them.

-----------

## With that in mind , let's containerize our application by first building a docker image with the dockerfile as such:

    docker build -t <myimage> .

Then run the docker image:

    docker run -it <myimage>

### Once inside the container change directory to:

    cd /mydir/

### You will then see the same files as the directory provided, go ahead and start running bedtools.bash, this has answers for question1

    ./bedtools.bash

### Please take a look at bedtools.bash file , it has step by step explanations on how results are derived.

    vim bedtools.bash or
    nano bedtools.bash

### Once this step is done, the script will generate some files in the cwd one of which is clinvar_chr_intersect.vcf.gz, this is an essential file for question 3, but before let's get back on how to the get results for question 2, which is by runnig the python script parse_vcf.py as such:

    python parse_vcf.py clinvar.vcf.gz <name_of_output_file.tsv>

### Replace <name_of_output_file.tsv> with any name you wish, for example foo.tsv or clinvar.tsv, and also take a look at the python script, it has step-by-step instructions on how question 2 is answered, again by:

    vim parse_vcf.py

### In brief parse_vcf will generate a dictionary in python of keys coming from the info field for the regions of insterest and, will then from this dictionary create a dataframe of counts of each type of variant

### Finally for question 3 the same logic applies and parse_vcf.py is reusable since the code is flexible enough to adapt to minor changes between the different files, therefore to generate results for question 3 simply use the following command:

    python parse_vcf.py clinvar_chr_intersect.vcf.gz <name_of_output_file.tsv>

### The name you chose for <name_of_output_file.tsv> will be a file that is written to the same directory you run the script

### In order to idenfiy major differences between both datasets you may wish to use another python script called differences.py by simply running

    python differences.py <name_of_output_file.tsv> <name_of_output_file.tsv>

### Please substitute <name_of_output_file.tsv> <name_of_output_file.tsv> with names you chose previously for question 2 and 3, for example foo.tsv and baz.tsv or clinvar.tsv and clinvar_from_target_regions.tsv differences.py also have some explanations and will print into stdout some basic differences between both files.
