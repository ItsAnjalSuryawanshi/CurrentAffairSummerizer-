# News Summarizer

This is a simple Flask web application that summarizes news articles. The app extracts text from a provided news URL and generates a summary using a machine learning model.

## Features

- Extracts the article text from a given URL.
- Summarizes the article using a machine learning model.
- Simple, easy-to-use web interface.

## Requirements

- Python 3.x
- Flask
- newspaper3k
- nltk
- scikit-learn
- joblib
- gunicorn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/news-summarizer.git
    cd news-summarizer
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app locally:

    ```bash
    python app.py
    ```

4. Visit `http://127.0.0.1:5000/` in your browser.

## Deployment to Heroku

1. Create a new Heroku app:

    ```bash
    heroku create
    ```

2. Push the code to Heroku:

    ```bash
    git push heroku master
    ```

3. Open your app:

    ```bash
    heroku open
    ```

Now your app should be live and accessible from the URL provided by Heroku.
