import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import imaplib
import email

# Initialize NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    return " ".join([ps.stem(i) for i in y])

# Load the trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("SMS Spam Classifier")

# Manual message input
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    st.header("Spam" if result == 1 else "Ham")

# Fetch and classify the most recent email using IMAP
if st.button('Fetch Most Recent Gmail Message'):
    # User credentials for IMAP login
    EMAIL = "xyz123@gmail.com"  # Replace with your Gmail address
    PASSWORD ="xpzgchbyapoxsbwr"  # Replace with your Gmail App Password

    try:    
        # Connect to Gmail's IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        # Search for the most recent email
        status, messages = mail.search(None, 'ALL')
        messages = messages[0].split()
        latest_email_id = messages[-1]  # Get the latest email ID

        # Fetch the email content by ID
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # Parse the raw email content
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg["subject"]
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            email_body = part.get_payload(decode=True).decode()
                            break
                else:
                    email_body = msg.get_payload(decode=True).decode()

                # Display and classify the email content
                st.write("Most Recent Email Subject: ", email_subject)
                st.write("Email Body Preview: ", email_body[:200])  # Displaying first 200 chars for brevity
                transformed_email = transform_text(email_body)
                vector_input = tfidf.transform([transformed_email])
                email_result = model.predict(vector_input)[0]
                st.write("Prediction: ", "Spam" if email_result == 1 else "Ham")

        mail.logout()

    except imaplib.IMAP4.error:
        st.error("Failed to authenticate. Check your email and App Password.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
