import streamlit as st
import pandas as pd
import pickle

def pred(df):
    model_pkl = pickle.load(open('m.pkl', 'rb'))
    pred1=model_pkl.predict(df)
    st.header('**Predicted Medical Insurance cost**')
    for i in pred1:
        st.write('$',"{:.2f}".format(i))
with st.header(""):
    st.header('**Medical Insurance Expenses Prediction**')
    dict_data={}
with st.form(key = 'form'):
    st.write("Enter the details below")
    dict_data['age'] = st.slider('Age', 0,100)
    x=st.radio(label='Choose gender',options=['Male','Female'])
    if x=='Male':
        dict_data['sex'] = 0
    else:
        dict_data['sex'] = 1
    dict_data['bmi'] = st.number_input('BMI')
    dict_data['children'] = st.slider('Number of children', 0,10)
    y=st.radio(label='Is the person a smoker',options=['Yes','No'])
    if y=='No':
        dict_data['smoker']=0
    else:
        dict_data['smoker']=1
    dict_data['region'] = st.selectbox(label='Region', options=[1,2,3,4])
    index = [1]
    data = pd.DataFrame(dict_data,index)
    if st.form_submit_button('Submit Data'):
        st.write(data)
if st.button("Predict"):
    pred(data)

st.markdown('[Source Code](https://github.com/jdhvsnehal/InsurancePredictor)', unsafe_allow_html=True)