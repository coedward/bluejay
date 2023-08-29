# Developed  by Caesar Oniku Edward
# importing required libraries
import nltk
from nltk.tokenize import word_tokenize
from gtts import gTTS
import pyttsx3
import os
import csv

# nltk.download('averaged_perceptron_tagger')
# import language_tool_python
# tool = language_tool_python.LanguageTool('en-US')  # use a local server
# tool = language_tool_python.LanguageToolPublicAPI('en-US') # or use public API
# creating a  Madi-English dictionary with zero content
madi_eng_dict = {}
madi_eng_dict2 = {}
dinka_madi_dict = {}

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

def untokenize(tokens):
    text_from_tokens = ''
    for i in range(len(tokens)):
        text_from_tokens = text_from_tokens + tokens[i]
    return text_from_tokens

# Creates a Python dictionary from the csv file
def csv_to_dictionary(csv_file):
    with open(csv_file, mode='r') as f:
        created_dictionary = csv.reader(f)
        bilingual_dict = {rows[0]: rows[1] for rows in created_dictionary}
        f.close()
    return bilingual_dict

# Given a source text and a bilingual dictionary, it creates tokens from the source text and translate them
# into another language using the bilngual dictionary
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

def get_token_tags(translated_tokens):
    streams_of_tags = " "
    for m in range(len(translated_tokens)):
        if translated_tokens[m] in madi_eng_dict2:
            streams_of_tags = streams_of_tags + " " + madi_eng_dict2[translated_tokens[m]]
        else:
            continue
    token_tags = word_tokenize(streams_of_tags)
    return token_tags

def get_word_tags(input_text):
    word_tags = nltk.pos_tag(word_tokenize(input_text))
    return word_tags

def text_to_speech(input_sentence):
    sentence = input_sentence
    file = "file.mp3"
    tts = gTTS(sentence, 'en')
    tts.save(file)
    os.system("mpg123" + file)
    return

def text_to_speech_pyttsx3(input_text, rate):
    engine = pyttsx3.init()
    # convert this text to speech
    text = input_text
    # setting the voice rate (faster or slower)
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
    return
