import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result.get("dominant_emotion"), "joy", f"Expected 'joy' for: {statement}")
    def test_anger(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result.get("dominant_emotion"), "anger", f"Expected 'anger' for: {statement}")
    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result.get("dominant_emotion"), "disgust", f"Expected 'disgust' for: {statement}")
    def test_sadness(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result.get("dominant_emotion"), "sadness", f"Expected 'sadness' for: {statement}")
    def test_fear(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result.get("dominant_emotion"), "fear", f"Expected 'fear' for: {statement}")
if __name__ == '__main__':
    unittest.main()
