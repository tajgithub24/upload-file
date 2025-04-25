from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Set the max upload size to 1GBB for testing
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1GB
UPLOAD_FOLDER = '/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({'message': f'File {file.filename} uploaded successfully.'}), 200

@app.route('/')
def index():
    return '''
    <h1>Upload File</h1>
    <form method="POST" action="/upload" enctype="multipart/form-data">
      <input type="file" name="file"/>
      <input type="submit"/>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

