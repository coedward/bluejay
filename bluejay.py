# importing required libraries
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.grammar import CFG
from nltk.parse import RecursiveDescentParser

nltk.download('averaged_perceptron_tagger')
# import language_tool_python
# tool = language_tool_python.LanguageTool('en-US')  # use a local server
# tool = language_tool_python.LanguageToolPublicAPI('en-US') # or use public API
import streamlit as st
import streamlit as st2
import csv

# creating a  Madi-English dctionary with zero
madi_eng_dict = {}
madi_eng_dict2 = {}

# reading a cvs file into the Madi-English dictionary
with open('MadiEnglishDict.csv', mode='r') as f:
    reader = csv.reader(f)
    madi_eng_dict = {rows[0]: rows[1] for rows in reader}
    f.close()

with open('MadiEnglishDict.csv', mode='r') as g:
    reader = csv.reader(g)
    madi_eng_dict2 = {rows[1]: rows[2] for rows in reader}
    g.close()

# creating the user interface
st.write('Translator')
col1, col2, col3 = st.columns(3)
with col1:
    # st.header("")
    option = st.selectbox('From', ('Arabic', 'English', 'Madi'))

    # implementing the translation algorithm
    # a user selects the language to translate from
    # he writes the text to translate into the left textbox
    # the algorithm iterates through the dictionary to match the key of the target in the dictionary
    # the result (a translation is displayed in the left text box
    text = col1.text_area("", value="", height=50, max_chars=2000, key=1)
    tokens = word_tokenize(text)
    st.write(tokens)
    sentence = ""
    result = ""
    if option == 'Madi':
        for key in madi_eng_dict.keys():
            if key == text:
                col3.text_area("To English ", value=madi_eng_dict[key], height=50, max_chars=None, key=2)
            else:
                for i in range(len(tokens)):
                    if tokens[i] in madi_eng_dict:
                        sentence = sentence + " " + madi_eng_dict[tokens[i]]
                    else:
                        sentence = sentence + " " + tokens[i]
                words_tokens = word_tokenize(sentence)
           # col3.text_area("To English ", value=sentence, height=50, max_chars=None, key=9)

        # create a string of word tags (parts of word) from word tokens
        # The word tokens keys are extracted from Madi to English dictionary
        word_tags = ""
        # The loop iterates through the dictionary to extract the English words
        for m in range(len(words_tokens)):
            if words_tokens[m] in madi_eng_dict2:
                word_tags = word_tags + " " + madi_eng_dict2[words_tokens[m]]
            else:
                continue
        word_tag_tokens = word_tokenize(word_tags)

        # syntax based translation
        # the original translated sentences are trnasformed to conform to correct Madi syntaxes

        for n in range(len(word_tag_tokens) - 1):
            if n <= len(words_tokens):
                # NN JJ (Noun Adjective) in Madi should become JJ NN (Adjective Noun) in English
                if (word_tag_tokens[n] == 'NN') and (word_tag_tokens[n + 1] == 'JJ'):
                    temp = words_tokens[n]
                    words_tokens[n] = words_tokens[n + 1]
                    words_tokens[n + 1] = temp

                    temp2 = word_tag_tokens[n]
                    word_tag_tokens[n] = word_tag_tokens[n + 1]
                    word_tag_tokens[n + 1] = temp2
                else:
                    continue
            else:
                break

        for o in range(len(word_tag_tokens) - 1):
            if o <= len(word_tag_tokens):
                # NN JJ (Noun Adjective) in Madi should become JJ NN (Adjective Noun) in English
                if (word_tag_tokens[o] == 'NN') and (word_tag_tokens[o + 1] == 'IN'):
                    temp = words_tokens[o]
                    words_tokens[o] = words_tokens[o + 1]
                    words_tokens[o + 1] = temp

                    temp2 = word_tag_tokens[o]
                    word_tag_tokens[o] = word_tag_tokens[o + 1]
                    word_tag_tokens[o + 1] = temp2
                else:
                    continue
            else:
                break

        for p in range(len(word_tag_tokens) - 1):
            if p <= len(word_tag_tokens):
                # NN JJ (Noun Adjective) in Madi should become JJ NN (Adjective Noun) in English
                if (word_tag_tokens[p] == 'PRP') and (word_tag_tokens[p + 1] == 'IN'):
                    temp = words_tokens[p]
                    words_tokens[p] = words_tokens[p + 1]
                    words_tokens[p + 1] = temp

                    temp2 = word_tag_tokens[p]
                    word_tag_tokens[p] = word_tag_tokens[p + 1]
                    word_tag_tokens[p + 1] = temp2
                else:
                    continue
            else:
                break

        for q in range(len(word_tag_tokens) - 1):
            if q <= len(word_tag_tokens):
                # NN JJ (Noun Adjective) in Madi should become JJ NN (Adjective Noun) in English
                if (word_tag_tokens[q] == 'NN') and (word_tag_tokens[q + 1] == 'IN'):
                    temp = words_tokens[q]
                    words_tokens[q] = words_tokens[q + 1]
                    words_tokens[q + 1] = temp

                    temp2 = word_tag_tokens[q]
                    word_tag_tokens[q] = word_tag_tokens[q + 1]
                    word_tag_tokens[q + 1] = temp2
                else:
                    continue
            else:
                break

        for r in range(len(word_tag_tokens) - 2):
            if r <= len(word_tag_tokens):
                # NN JJ (Noun Adjective) in Madi should become JJ NN (Adjective Noun) in English
                if (word_tag_tokens[r] == 'IN') and (word_tag_tokens[r + 1] == 'IN') and (
                        word_tag_tokens[r + 2] == 'PRP'):
                    temp = words_tokens[r + 1]
                    words_tokens[r + 1] = words_tokens[r + 2]
                    words_tokens[r + 2] = temp

                    temp2 = word_tag_tokens[r + 1]
                    word_tag_tokens[r + 1] = word_tag_tokens[r + 2]
                    word_tag_tokens[r + 2] = temp2
                else:
                    continue
            else:
                break

        input_to_text_box = ''
        for r in range(len(words_tokens)):
         input_to_text_box = input_to_text_box + " " + words_tokens[r]
         col3.text_area("To English ", value=input_to_text_box, height=50, max_chars=None, key=4)
        st.write(word_tag_tokens)
