# 📧 Email Spam Classifier

A machine learning project that classifies emails as **Spam** or **Ham** using multiple ML algorithms, NLP preprocessing, and a **Streamlit** interactive UI.  
It also supports **real-time email retrieval** via **Gmail API** or **IMAP**.

---

## 🚀 Features
- Fetch recent emails using **Gmail API** (OAuth) or **IMAP**.
- **NLP preprocessing**: tokenization, stopword removal, stemming/lemmatization.
- Multiple models: **Naive Bayes**, **SVM**, **Logistic Regression**, **Random Forest**.
- **Streamlit UI** for classification and metrics visualization.
- Model tuning with scikit-learn’s **GridSearchCV**.
- Accuracy, Precision, Recall, F1, ROC curves.

---

## 🛠 Tech Stack
- **Python 3.9+**
- **scikit-learn**, **pandas**, **numpy**
- **NLTK** or **spaCy** for NLP
- **Streamlit** for the UI
- **imaplib** for IMAP
- **joblib** for saving models

---

