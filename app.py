import streamlit as st
import joblib
classifier = joblib.load("C:/Users/Kannan/Downloads/spam_classifier.pkl")
cv = joblib.load("C:/Users/Kannan/Downloads/count_vectorizer.pkl")
st.title('Email spam detection')
user_input = st.text_area('Enter the email message')
if st.button('submit'):
    if user_input:
        user_input = [user_input]
        user_input = cv.transform(user_input).toarray()
        prediction = classifier.predict(user_input)
        result = 'Spam' if prediction == 1 else 'Not Spam'
        st.write(f'The email is: {result}')
else:
    st.write('Please enter the email text.')  
