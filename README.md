# 📧 Email Spam Classifier

A machine learning project that classifies emails/SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and multiple ML algorithms.  
The project includes an interactive **Streamlit web app** and supports **real-time email retrieval** via **Gmail API (OAuth)** or **IMAP**.

---

## 🚀 Features

- 📥 Fetch recent emails using **Gmail API** or **IMAP**
- 🧠 NLP text preprocessing pipeline
- 🤖 Multiple ML models evaluated and compared
- 🏆 Best model selected based on performance metrics
- 📊 Accuracy, Precision, Recall, F1 evaluation
- 🌐 Interactive **Streamlit UI**
- 💾 Saved model for real-time predictions

---

## 🛠 Tech Stack

- **Python 3.9+**
- **scikit-learn**, **pandas**, **numpy**
- **NLTK** for NLP preprocessing
- **Streamlit** for UI
- **imaplib** for email retrieval
- **joblib / pickle** for model persistence

---

## 📂 Dataset

- **SMS Spam Collection Dataset (Kaggle)**
- Contains labeled messages as spam or ham
- File used: `spam.csv`

---

## 🔎 Exploratory Data Analysis (EDA)

Performed analysis to understand the dataset:

- Checked class distribution (Spam vs Ham)
- Removed unused columns
- Renamed columns for clarity
- Visualized message length distribution
- Identified most frequent words

---

## 🧹 Data Preprocessing

Applied NLP pipeline:

- Convert text to lowercase
- Tokenization
- Remove special characters
- Remove punctuation
- Remove stopwords
- Stemming (Porter Stemmer)
- Feature extraction using **TF-IDF**

Additional analysis:

- Word Cloud visualization
- Corpus creation
- Most frequent spam/ham words

---

## 🤖 Models Evaluated

Multiple classifiers were trained and compared:

| Model | Accuracy | Precision |
|--------|----------|------------|
| SVC | 0.866 | 0.000 |
| KNN | 0.928 | 0.771 |
| Naive Bayes | 0.940 | **1.000** |
| Decision Tree | 0.944 | 0.877 |
| Logistic Regression | 0.961 | 0.971 |
| Random Forest | **0.975** | 0.983 |

---

## ✅ Final Model Selection

Although ensemble models achieved slightly higher accuracy,  
**Multinomial Naive Bayes** was selected as the final model because:

- 🥇 Perfect precision for spam detection (1.0)
- ⚡ Fast inference time
- 📚 Well-suited for text classification
- 💻 Low computational cost
- 🚀 Ideal for real-time applications

> High precision ensures legitimate emails are not incorrectly marked as spam.

---

## 🌐 Streamlit Web App

The project includes an interactive UI to:

- Enter custom text for prediction
- Classify messages instantly
- Display results clearly
- Fetch emails via IMAP/Gmail API (optional)

Run locally:
  ```bash
   streamlit run app.py
