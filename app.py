from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload_video', methods=['POST'])
def upload_video():
    video_file = request.files['video']
    if video_file:
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
        video_file.save(video_path)
        return 'Video uploaded successfully'
    return 'No video file received'

@app.route('/add_subtitle', methods=['POST'])
def add_subtitle():
    subtitle_data = request.json
    # Implement logic to store subtitle data (e.g., in a database)
    return 'Subtitle added successfully'

if __name__ == '__main__':
    app.run(debug=True)

