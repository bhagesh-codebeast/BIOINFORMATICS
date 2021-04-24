import argparse
from Bio import GenBank

#Argparse arguments
parser = argparse.ArgumentParser(description='\n GenBank to Fasta converter.')
parser.add_argument("-i","--input", help = "input filepath/filename of GenBank file example: Data/inputfile.gb")
parser.add_argument("-o","--output", help = "output filepath/filename of fasta file example: Data/outputfile.fasta")

args = parser.parse_args()

#conditions for input & output files
if not args.input:
    print("\n Please enter input file name using -i or --input")
elif not args.output:
    print("\n Please enter Output file name using -o or --ouput")
else:
    inputpath = args.input
    outputpath = args.output

    #GenBank parser
    with open(inputpath) as handle:
        for record in GenBank.parse(handle):

            #writing to a file
            with open(outputpath,'w') as f:
                f.write(">"+outputpath.replace("/","").replace(".","")+"\n"+record.sequence)
                print("\n Fasta file has been created in the folder: "+outputpath)