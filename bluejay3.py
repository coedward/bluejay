# importing required libraries
from typing import Any

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
from collections import defaultdict
from bluejay_library import BilingualDictionary
my_file = 'MadiEnglishDict.csv'
Bdict = BilingualDictionary(my_file)
word = 'zangwa'

st.write(Bdict.create())
st.write('---------------------------------------------------')
st.write(Bdict.get_keywords(word))