
from flask import Flask,request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    sentiment = predict_sentiment(text)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
