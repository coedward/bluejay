#Developed  by Caesar Oniku Edward
# importing required libraries
import nltk
from nltk.tokenize import word_tokenize
import csv
#nltk.download('averaged_perceptron_tagger')
# import language_tool_python
# tool = language_tool_python.LanguageTool('en-US')  # use a local server
# tool = language_tool_python.LanguageToolPublicAPI('en-US') # or use public API
# creating a  Madi-English dictionary with zero content
madi_eng_dict = {}
madi_eng_dict2 = {}

with open('MadiEnglishDict.csv', mode='r') as g:
    reader = csv.reader(g)
    madi_eng_dict2 = {rows[1]: rows[2] for rows in reader}
    g.close()

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

def csv_to_dictionary(csv_file):
    with open(csv_file, mode='r') as f:
        reader = csv.reader(f)
        madi_eng_dict = {rows[0]: rows[1] for rows in reader}
        f.close()
    return madi_eng_dict

def translate_tokens(source_text, input_csv_file):
    tokens_from_text = tokenize_text(source_text)
    source_dictionary = csv_to_dictionary(input_csv_file)
    translated_tokens = " "
    for i in range(len(tokens_from_text)):
        for j in range(len(source_dictionary)):
            if tokens_from_text[i] in source_dictionary.keys():
                translated_tokens = translated_tokens + " " + source_dictionary[tokens_from_text[i]]
                break
            else:
                continue
    return translated_tokens

class BilingualDictionary:
    madi_eng_dict = {}
    madi_eng_dict2 = {}

    def __init__(self, csv_file):
        self.csv_file = csv_file

    # creates dictionary from csv file
    def create(self) -> object:
        with open(self.csv_file, mode='r') as f:
            reader = csv.reader(f)
            madi_eng_dict: dict = {rows[0]: rows[1] for rows in reader}
            f.close()
        return madi_eng_dict

    # gets keyword from the dictionary
    def get_keywords(self) -> object:
        bidict = BilingualDictionary
        my_dict = bidict.create(self)
        key_words_tokens = word_tokenize(self)
        for i in range(len(key_words_tokens)):
            if key_words_tokens[i] in my_dict:
                sentence = sentence + " " + my_dict[key_words_tokens[i]]
            else:
                sentence = sentence + " " + key_words_tokens[i]
        words_tokens = word_tokenize(sentence)
        return words_tokens

class madi_eng_dict_tagged (dict):
    # __init__ function
    def __init__(self):
        self = dict()
        # Function to add key:value

    def add(self, key, value):
        self[key] = value