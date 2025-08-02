from flask import Flask, request

import os

from datetime import datetime



app = Flask(__name__)



SAVE_DIR = "received_texts"  # ফাইলগুলো এখানে সেভ হবে

if not os.path.exists(SAVE_DIR):

    os.makedirs(SAVE_DIR)



@app.route('/', methods=['GET', 'POST'])

def receive_text():

    if request.method == 'POST':

        text = request.form.get('text', '')

        

        # Timestamp দিয়ে filename তৈরি

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"text_{timestamp}.txt"

        filepath = os.path.join(SAVE_DIR, filename)



        with open(filepath, 'w', encoding='utf-8') as f:

            f.write(text)



        return f"<h2>✅ Text saved as <code>{filename}</code></h2><pre>{text}</pre>"



    return '''

    <h2>Send Text from Mobile:</h2>

    <form method="POST">

      <textarea name="text" rows="10" cols="50" placeholder="Paste or type text here..."></textarea><br>

      <button type="submit">Send to Laptop</button>

    </form>

    '''



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)