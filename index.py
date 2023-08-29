import streamlit as st
from PIL import Image
from bluejay_library import translate_tokens, get_word_tags, untokenize, text_to_speech_pyttsx3, \
    csv_to_dictionary

eng_madi_dictionary = 'MadiEnglishDict.csv'
eng_madi_dictionary2 = 'MadiEnglishDict2.csv'
dinka_madi_dictionary = 'DinkaMadiDict.csv'

image = Image.open('images/bluejay4.png')
st.image(image, caption=None)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        source_language = st.selectbox('From', ('', 'Arabic','Dinka', 'English', 'Madi'), key=1)

    with col2:
        target_language = st.selectbox('To', ('', 'Arabic', 'Dinka', 'English', 'Madi'), key=2)

checked1 = st.checkbox("Text To Voice")
with st.container():
    if (source_language == 'Dinka') and (target_language == 'Madi'):
        text_input1 = st.text_area(target_language, '', height=200, key=5)
        if checked1:
            text_to_speech_pyttsx3(text_input1, 100)

    elif (source_language == 'Madi') and (target_language == 'English'):
        text_input1 = st.text_area(target_language, '', height=200, key=4)
        if checked1:
            text_to_speech_pyttsx3(text_input1, 100)

    elif (source_language == 'English') and (target_language == 'Madi'):
        text_input1 = st.text_area(target_language, '', height=200, key=5)

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

checked = st.checkbox('Text to Voice')
with st.container():
    # translated_tokens = translate_tokens(text_input1, eng_madi_dictionary)
    # untokenized_string = untokenize(translated_tokens)
    # word_tags = get_word_tags(untokenized_string)
    # st.text_area(source_language, untokenized_string, height=200, key=16)
    #
    if source_language == 'Dinka':
        translated_tokens = translate_tokens(text_input1, dinka_madi_dictionary)
        untokenized_string = untokenize(translated_tokens)
        word_tags = get_word_tags(untokenized_string)
        st.text_area(source_language, untokenized_string, height=200, key=16)

    elif source_language == 'Madi':
        translated_tokens = translate_tokens(text_input1, eng_madi_dictionary)
        untokenized_string = untokenize(translated_tokens)
        word_tags = get_word_tags(untokenized_string)
        st.text_area(source_language, untokenized_string, height=200, key=16)

    else:
        st.write('No dictionary for this pair of languages')

if checked:
    text_to_speech_pyttsx3(untokenized_string, 200)
