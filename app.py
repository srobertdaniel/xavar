from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

# app.run(host='192.168.1.199', port=5000, debug=False)