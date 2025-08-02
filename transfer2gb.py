from flask import Flask, request, render_template_string

import os

import time

from datetime import datetime



app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024  # 2GB



if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)



HTML_PAGE = '''

<!DOCTYPE html>

<html>

<head>

  <title>📁 Upload File to Laptop</title>

</head>

<body style="font-family: Arial; text-align: center; padding-top: 50px;">

  <h2>📲 Upload File from Mobile to Laptop</h2>

  <form method="POST" enctype="multipart/form-data">

    <input type="file" name="file"><br><br>

    <button type="submit">Upload</button>

  </form>

</body>

</html>

'''



@app.route('/', methods=['GET', 'POST'])

def upload_file():

    if request.method == 'POST':

        uploaded_file = request.files.get('file')

        if uploaded_file:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"{timestamp}_{uploaded_file.filename}"

            save_path = os.path.join(UPLOAD_FOLDER, filename)



            start_time = time.time()

            uploaded_file.save(save_path)

            end_time = time.time()



            size_bytes = os.path.getsize(save_path)

            size_mb = size_bytes / (1024 * 1024)

            duration = end_time - start_time

            speed = size_mb / duration if duration > 0 else 0



            return f"""

            <h2>✅ File uploaded: <code>{filename}</code></h2>

            <p>🗂️ Size: {size_mb:.2f} MB</p>

            <p>⏱️ Time: {duration:.2f} seconds</p>

            <p>🚀 Upload Speed: <strong>{speed:.2f} MB/s</strong></p>

            <a href="/">⬅ Upload Another</a>

            """

        return "<h3>❌ No file selected!</h3>"

    return render_template_string(HTML_PAGE)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)