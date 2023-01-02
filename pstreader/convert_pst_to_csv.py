"""Script to convert a folder of g-chat pst files to a single .csv"""
import re
import os
import sys
import glob
import pathlib
import datetime


import pandas as pd
from loguru import logger
from libratom.lib.pff import PffArchive







def clean_format_messages(message):
    """

    :param message: String containing a set of g-chat messages
    :return: String stripped of \r, \n and timestamps
    """
    timestamp_regex = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}'

    message = re.sub(r'\r', ' ', message)  # Removes \r from the text
    message = re.sub(r'\n', ' ', message)  # Removes \n from the text
    message = re.sub(timestamp_regex, ' ', message)
    message = message + " *"
    return message

def name_csv():
    """
    :return: a string with the current timestamp to used for naming .csv files
    """
    dt =  datetime.datetime.now()
    dt = dt.isoformat()
    name = f'messages_{dt}.csv'
    return name

def read_pst_files(directory):
    """

    :param directory: directory to search within
    :return:
    """
    list_of_files = []
    try:
        os.chdir(directory)
    except FileNotFoundError:
        logger.error(F'Directory {directory} not found')
        sys.exit(0)

    for file in glob.glob("*.pst"):
        list_of_files.append(file)

    if len(list_of_files) == 0:
        logger.error(f'No pst files found in the folder: {directory}. ')
        sys.exit(0)

    return (list_of_files)

def write_to_error_file(file,contents):
    """
    Write error logs to a .txt file

    :param file:
    :return:
    """

    with open(file, 'a') as the_file:
        the_file.write(contents + '\n')

def extract_messages_from_pst(PST_FILE):
    """
    :param PST_FILE: pst file to be read and extracted
    :return: a list of dict containing email,message
    """
    email_regex = r"([a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+)"  # matches an email
    text_regex = r"(?<=\*)(.*?)(?=\*)"  # matches text between * and *
    row_list = []
    try:
        with PffArchive(PST_FILE) as archive:
            for message in archive.messages():


                chat_messages = archive.get_message_body(message)

                # Begin by cleaning the messages
                chat_messages = clean_format_messages(chat_messages[0].decode())

                # Given the cleaned messages, find the cleaned text
                matches = re.findall(text_regex, chat_messages)

                for item in matches:
                    # Extract and strip the email, the remaining text is the message
                    email_address = re.findall(email_regex, item)
                    remaining_messages = re.sub(email_regex, ' ', item)
                    if len(email_address) == 1:
                        this_dict = {'email': email_address[0], 'message': remaining_messages}
                        row_list.append(this_dict)

        logger.success(f'Read file: {PST_FILE}')
        return row_list
    except Exception as e:
        logger.error(f'Error reading or extracting data from the file {PST_FILE}. Skipping this file. ')
        write_to_error_file('error-log.txt',PST_FILE+'-'+str(e))
        return []


def main():
    file_dic = 'pst_files'
    path = pathlib.Path(__file__).parent.resolve()

    list_of_pst_files = read_pst_files(str(path) +'/'+ file_dic)


    list_of_rows = []
    for file in list_of_pst_files:
        row_list = extract_messages_from_pst(file)
        list_of_rows = list_of_rows + row_list
    df = pd.DataFrame(list_of_rows)
    csv_name = name_csv()
    df.to_csv(path_or_buf=str(path) +'/'+  csv_name, index=False)
    logger.success(f'Exported: {csv_name} ')


if __name__ == "__main__":
    main()






