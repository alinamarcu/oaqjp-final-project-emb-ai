from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    text_statement = request.form.get("statement")
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
            "For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
            "'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
        ).format(
            anger=result.get('anger'),
            disgust=result.get('disgust'),
            fear=result.get('fear'),
            joy=result.get('joy'),
            sadness=result.get('sadness'),
            dominant_emotion=result.get('dominant_emotion')
        )
    return response_text
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
