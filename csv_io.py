from csv import reader
from anonymisation import main_ano
import sys

filepath = sys.argv[1]

thesaurus_path = "thesaurus.txt"

with open(filepath) as file:
    with open(filepath+".anonymized.tsv", "w") as output:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            message = " ".join(row[1:])
            output.write(row[0]+"\t"+message+"\t"+main_ano(message, thesaurus_path)+"\n")
