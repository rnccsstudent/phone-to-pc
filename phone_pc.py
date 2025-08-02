from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receive_text():
    if request.method == 'POST':
        text = request.form.get('text', '')
        with open('received_text.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        return "<h2> Text received and saved!</h2><pre>{}</pre>".format(text)

    return '''
    <h2>Send Text from Mobile: </h2>
    <form method="POST">
      <textarea name="text" rows="10" cols="50" placeholder="paste or type text here..."></textarea><br>
      <button type="submit">Send to Laptop</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)