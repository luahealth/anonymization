from csv import reader
from anonymisation import main_ano
from loguru import logger

import sys

filepath = sys.argv[1]

thesaurus_path = "thesaurus.txt"

with open(filepath) as file:
    logger.success(f'Read file {filepath}')
    logger.info('Anonymising text, this may take some time')
    new_file_path = filepath+".anonymized.tsv"
    with open(new_file_path, "w") as output:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            message = " ".join(row[1:])
            output.write(row[0]+"\t"+message+"\t"+main_ano(message, thesaurus_path)+"\n")
    logger.success(f'Exported to file: {new_file_path}')
