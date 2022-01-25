## Please start by building up a docker image with the dockerfile as such (make sure you cd into the directory provided):

docker build -t <myimage> .

##Then run the docker image:

docker run -it <myimage>

## Once inside the container change directory to:

cd /mydir/

## You will then see the same files as the directory provided, go ahead and start running bedtools.bash, this has answers for question1

./bedtools.bash

## Please take a look at bedtools.bash file , it has step by step explanations on how results are derived.

vim bedtools.bash or
nano bedtools.bash

## Once this step is done, the script will generate some files in the cwd one of which is clinvar_chr_intersect.vcf.gz,
## this is an essential file for question 3, but before let's get back on how to the get results for question 2, which is
## by runnig the python script parse_vcf.py as such:

python parse_vcf.py clinvar.vcf.gz <name_of_output_file.tsv>

## PLease replace <name_of_output_file.tsv> with any name you wish, for example foo.tsv or clinvar.tsv

## PLease also take a look at the python script, it has step-by-step instructions on how question 2 is answered, again by:

vim parse_vcf.py

## In brief parse_vcf will generate a dictionary in python of keys coming from the info field for the regions of insterest and 
## will then from this dictionart create a dataframe of counts of each type of variant

## Finally for question 3 the same logic applies and parse_vcf.py is reusable since the code is flexible enough to adapt to minor changes 
## between the different files, therefore to generate results for question 3 simply use the following command:

python parse_vcf.py clinvar_chr_intersect.vcf.gz <name_of_output_file.tsv>

## The name you chose for <name_of_output_file.tsv> will be a file that is written to the same directory you run the script

## In order to idenfiy major differences between both datasets you may wish to use another python script called
## differences.py by simply running

python differences.py <name_of_output_file.tsv> <name_of_output_file.tsv>

## Please substitute <name_of_output_file.tsv> <name_of_output_file.tsv> with names you chose previously for question 2 and 3,
## for example foo.tsv and baz.tsv or clinvar.tsv and clinvar_from_target_regions.tsv

## differences.py also have some explanations and will print into stdout some basic differences between both files.

## please also use only the gzipped version of the variant files for the python script, the non zipped are there just for quick visualization