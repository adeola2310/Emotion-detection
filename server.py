''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    label = response['label']
    score = response['score']
    if label == None:
         return 'Invalid input'
    return "For the given statement, the system response is {} : {}. The dominant emotion is joy".format(label.split('_')[1], score)


@app.route("/")
def render_index_page():
      ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
      return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
