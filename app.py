from flask import Flask, render_template, redirect, url_for, request, session, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/', methods = ["GET", 'POST'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)