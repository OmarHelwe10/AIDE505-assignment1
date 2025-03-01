from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/predict', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid request. Provide text in JSON format.'}), 400

    text = data['text']
    sentiment_scores = analyzer.polarity_scores(text)

    
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "positive"
    elif sentiment_scores['compound'] >= 0.05 and sentiment_scores['compound'] <= -0.05:
        sentiment = "neutral"
    else:
        sentiment = "negative"
    

    response = {
        "sentiment": sentiment
        }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

