# Anonymisation

This is a python based service for redacting sensitive information from text.   

## Setup / Install 
### Prerequisites  
* Python 3.8 or 3.9  

### Installation  
1. [Optional] Setup and activate a virtual environment 
2. Install the required packages by running `pip install -r requirements.txt`


## Usage 

`test_ano.py` gives an example usage. 

`thesaurus.txt` is a custom dictionary of words you can enter that the service will remove. For example, if you have a client called abc_enterprises and you notice the service does not remove it, you can add the name to this text file to ensure it's removed. 


A possible workflow would be;

 1. Create a python file and import `from anonymisation import main_ano`
 2. Add your own code to read your data and iterate over it 
 3. For each piece of text (this could be a message, an email etc) run `main_ano(string,thesaurus_path)` and save the output
 
 
## License 
Copyright 2022 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
