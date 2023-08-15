# importing required libraries
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.grammar import CFG
from nltk.parse import RecursiveDescentParser

nltk.download('averaged_perceptron_tagger')
import streamlit as st
import streamlit as st2
import csv

# creating a  Madi-English dictionary with zero
madi_eng_dict = {}

# reading a cvs file into the Madi-English dictionary
with open('MadiEnglishDict3.csv', mode='r') as f:
    reader = csv.reader(f)
    madi_eng_dict = {rows[0]: rows[1] for rows in reader}

with st.container():
    st.write('Translator')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox('From', ('Arabic', 'English', 'Madi'), key ='1')

    with col2:
        option = st.selectbox('To', ('Arabic', 'English', 'Madi'), key ='2')

with st.container():
    col3, col4 = st.columns(2)
    with col3:
        st.header("")
        text = col3.text_area("", value="", height=50, max_chars=2000, key=3)
        if option == 'Madi':
            text2 = col4.text_area("", value=text, height=50, max_chars=2000, key=4)
            st.write(option)
            st.write(text2)
    with col4:
        st.header("")
        text = col4.text_area("", value="", height=50, max_chars=2000, key=5)

    # st.write("------------------------------------------------" )
    # st.write(madi_eng_dict2)
    # st.write("------------------------------------------------")
    # st.write(eng_tokens)
    # st.write("------------------------------------------------")
    # eng_tokens_tags = nltk.pos_tag(eng_tokens)
    # st.write(eng_tokens_tags)
    #
    # grammar = nltk.CFG.fromstring("""
    # S -> NP VP
    # NP -> Det NN | Det NN PP | Det NN RB |NN PRP |N | PRP | NNP
    # VP -> V NP | VP PP | VBP NP
    # PP -> P NP
    # Det -> 'I'  'a' | 'an' | 'my' | 'the' | 'this' | 'those'
    # NN -> 'boy' | 'girl' | 'man' | 'woman' | 'food' | 'home' | 'pajamas' | 'elephant' | 'car' | 'child'
    # V -> 'come'| 'run' | 'go' | 'eat' | 'ate'
    #
    # VBP -> 'came'| 'ran' | 'went' | 'ate' |'shot'
    # P -> 'in' | 'on' | 'by' |'of' | 'off' | 'with'
    # RB -> 'alone' | 'yesterday' | 'here' | 'there' | 'tomorrow'| 'quickly' |'slowly' | 'today'
    # PRP -> 'I' | 'we' | 'he'| 'she'| 'it' | 'you'| 'they' | 'them'| our | 'ours'| their
    # """)
    #
    # parser = nltk.ChartParser(grammar)
    # trees = list(parser.parse(eng_tokens))
    # atree = trees[0]
    # st.write(atree)
    # st.write(atree.leaves())
  #  cp = nltk.RecursiveDescentParser(grammar)
  #  result = cp.parse(eng_tokens_tags)
  #  st.write(result)
#
# with col2:
#     st.button('<<-->>')
#
# with col3:
#     option = st.selectbox( 'Translate To', ('Arabic', 'English', 'Madi'))
#     col3.text_area("To English ", value=option, height=50, max_chars=None, key=3)