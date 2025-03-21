"""
Flask server for the EmotionDetection application.
"""

# pylint: disable=invalid-name

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route('/')
def home():
    """
    Render the home page.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    """
    Process an emotion detection request and return a formatted response.
    """
    text_statement = request.form.get("statement", "").strip()
    if not text_statement:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        result = emotion_detector(text_statement)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is 'anger': {result.get('anger')}, "
        f"'disgust': {result.get('disgust')}, 'fear': {result.get('fear')}, "
        f"'joy': {result.get('joy')} and 'sadness': {result.get('sadness')}. "
        f"The dominant emotion is {result.get('dominant_emotion')}."
    )
    return response_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
