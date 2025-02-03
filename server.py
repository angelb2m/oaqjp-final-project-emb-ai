'''
    Flask server for emotion detection.
'''
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    '''
        Endpoint to analyze the dominant emotion from the given text.
    '''
    try:
        data = request.get_json()
        text = data.get("text", "")

        emotions = emotion_detector(text)

        if emotions.get("dominant_emotion") is None:
            return "Invalid text! Please try again!", 400

        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
            f"'sadness': {emotions['sadness']}. "
            f"The dominant emotion is {emotions['dominant_emotion']}."
        )

        return formatted_response

    except KeyError as key_error:
        return jsonify({"error": f"Missing key: {str(key_error)}"}), 400

    except ValueError as value_error:
        return jsonify({"error": f"Invalid value: {str(value_error)}"}), 400

    except TypeError as type_error:
        return jsonify({"error": f"Type error: {str(type_error)}"}), 400

    except RuntimeError as runtime_error:
        return jsonify({"error": f"Runtime error: {str(runtime_error)}"}), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
