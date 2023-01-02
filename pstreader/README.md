
# Convert .PST to .CSV

This folder contains a script to convert a group of  `.pst` files to a single `.csv` file. 

## Usage 

### Prerequisite
* Python 3.9 installed on your system 
* You are conformable using the command line (*Terminal* on Mac, or *Command Prompt* on Windows)


### Running the script
 1. Dump all your `.pst` files into the folder `pstreader/pst_files`
 2. Open this folder on the command line.
 3. Run the script using the command `python extract_pst.py`. The progress of the script will be outputted to your screen. You should see which files are read correctly, and which cause errors. Once the script is finished you will see something like 
     ```bash
     2023-01-02 14:42:16.069 | SUCCESS  | __main__:main:127 - Exported: messages_2023-01-02T14:42:16.067766.csv 
     ```
	Which tells you that the contents of the pst files are now in the file `messages_2023-01-02T14:42:16.067766.csv` 


### Errors
While running the script, if the program has trouble extracting contents, it will create an `error_file.txt` and output the errors to that file. 

