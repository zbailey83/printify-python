from flask import Flask, render_template, request
import pandas as pd
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    text = request.form['user_input']

    # Load the CSV file
    df = pd.read_csv('input.csv', header=None)

    # Write the user input to the second line (index 1)
    df.loc[1] = [text]

    # Save the updated CSV file
    df.to_csv('input.csv', index=False, header=False)

    # Run your Python script here
    subprocess.call(['python upscalecreateimages.py'])

    return 'Text submitted successfully'
if __name__ == '__main__':
    app.run(debug=False)