from flask import Flask, render_template, request
import joblib
import nltk
from newspaper import Article
from nltk.tokenize import sent_tokenize
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize Flask app
app = Flask(__name__)

# Load saved model and vectorizer (make sure you have these saved)
model = joblib.load('summary_model.pkl')  # Replace with actual model path
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Replace with actual vectorizer path

# Function to extract article text from the URL
def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# Function to extract features for the sentences
def extract_features(sentences, tfidf_vectorizer):
    tfidf_matrix = tfidf_vectorizer.transform(sentences).toarray()
    features = []
    for i, sent in enumerate(sentences):
        sent_len = len(sent)
        position = i / len(sentences)
        tfidf_score = np.mean(tfidf_matrix[i])
        features.append([sent_len, position, tfidf_score])
    return np.array(features)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Summarize route
@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        url = request.form['url']
        text = extract_article(url)
        sentences = sent_tokenize(text)

        # Extract features and predict summary
        features = extract_features(sentences, tfidf_vectorizer)
        probs = model.predict_proba(features)[:, 1]

        # Select top N sentences for summary (you can change top_n to adjust the length of the summary)
        top_n = 5
        top_indices = probs.argsort()[-top_n:][::-1]
        top_indices = sorted(top_indices)

        summary = ' '.join([sentences[i] for i in top_indices])
        return render_template('index.html', summary=summary, url=url)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
