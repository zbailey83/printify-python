import os
from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text_input = request.form.get('text_input')

        # Write the input string to the second line of input.csv
        with open('input.csv', 'r') as f:
            lines = f.readlines()
            if text_input is not None:
                lines.insert(1, text_input + '\n')
        with open('input.csv', 'w', newline='') as f:
            f.writelines(lines)

    elif 'create' in request.form:
            os.system('python upscalecreateimages.py')
            return 'Images created.'

    elif 'upload' in request.form:
            os.system('python upscaleuploadimages.py')
            return 'Images uploaded.'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)