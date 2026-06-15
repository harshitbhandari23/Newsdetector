# 📰 Fake News Detection Web Application

A Flask-based web application that predicts whether a news article is **Real** or **Fake** using a Machine Learning model. The application performs text preprocessing with **NLTK** and **spaCy**, converts the input into word embeddings, and classifies it using a pre-trained model.

---

## 📌 Features

- Detects whether a news article is **Real** or **Fake**
- User-friendly web interface built with Flask
- Text preprocessing using:
  - Regular Expressions
  - NLTK Stopword Removal
  - Lowercasing
- Feature extraction using **spaCy Word Embeddings**
- Pre-trained Machine Learning model loaded with **Joblib**

---

## 🛠️ Technologies Used

- Python
- Flask
- spaCy
- NLTK
- Scikit-learn
- Joblib
- HTML
- CSS

---

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py
├── news.pkl
├── templates/
│   ├── home.html
│   ├── about.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── images/
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Fake-News-Detection.git
```

### 2. Navigate to the project directory

```bash
cd Fake-News-Detection
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the spaCy model

```bash
python -m spacy download en_core_web_lg
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User enters a news article.
2. The text is cleaned using Regular Expressions.
3. Stopwords are removed using NLTK.
4. The cleaned text is converted into a spaCy word vector.
5. The vector is passed to the trained Machine Learning model.
6. The application displays whether the news is **Real** or **Fake**.

---

## 📸 Screenshots

### Home Page

_Add a screenshot here_

### Prediction Result

_Add a screenshot here_

---

## 📦 Requirements

- Python 3.9+
- Flask
- spaCy
- NLTK
- Scikit-learn
- Joblib

---

## 📄 requirements.txt

```
Flask
spacy
nltk
scikit-learn
joblib
```

---

## Future Improvements

- Support for multiple machine learning models
- Confidence score for predictions
- News source verification
- News URL classification
- Better UI/UX
- Deployment on Render/Heroku/AWS

---

## Author

**Harshit Bhandari**

GitHub: https://github.com/yourusername

LinkedIn: *Add your LinkedIn profile here*

---

## License

This project is licensed under the MIT License.
