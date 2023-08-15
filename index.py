import streamlit as st
from PIL import Image
from bluejay_library import translate_tokens
eng_madi_dictionary = 'MadiEnglishDict.csv'

image = Image.open('images/bluejay.png')
st.image(image, caption=None)


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        source_language = st.selectbox('From', ('', 'Arabic', 'English', 'Madi'), key=1)

    with col2:
        target_language = st.selectbox('To', ('', 'Arabic', 'English', 'Madi'), key=2)

with st.container():
    if (source_language == 'Madi') and (target_language == 'English'):
        text_input1 = st.text_area(target_language, '', height=200, key=4)

    elif (source_language == 'English') and (target_language == 'Madi'):
        text = source_language + '  ' + target_language
        text_input1 = st.text_area(target_language, text, height=200, key=5)

    elif (source_language == 'English') and (target_language == 'English'):
        text = 'source language and tagret language should not be the same'
        text_input1 = st.text_area(target_language, text, height=200, key=6)

    elif (source_language == 'Madi') and (target_language == 'Madi'):
        text = 'source language and tagret language should not be the same'
        text_input1 = st.text_area(target_language, text, height=200, key=7)

    elif (source_language == 'Madi') and (target_language == ''):
        text = 'choose target language'
        text_input1 = st.text_area(target_language, text, height=200, key=8)

    elif (source_language == '') and (target_language == 'Madi'):
        text = 'choose target language'
        text_input1 = st.text_area(target_language, text, height=200, key=9)

    elif (source_language == '') and (target_language == 'English'):
        text = 'choose source language'
        text_input1 = st.text_area(target_language, text, height=200, key=10)

    elif (source_language == 'English') and (target_language == ''):
        text = 'choose target language'
        text_input1 = st.text_area(target_language, text, height=200, key=11)

    elif (source_language == 'English') and (target_language == ''):
        text = 'choose target language'
        text_input1 = st.text_area(target_language, text, height=200, key=12)

    elif (source_language == '') and (target_language == ''):
       text = 'choose source and target languages'
       text_input1 = st.text_area(target_language, text, height=200, key=14)

    else:
        text = 'At the moment only English and Madi languages are supported'
        text_input1 = st.text_area(target_language, text, height=200, key=15)

with st.container():
    translation = translate_tokens(text_input1,eng_madi_dictionary)
    st.text_area(source_language, translation, height=200, key=16)
