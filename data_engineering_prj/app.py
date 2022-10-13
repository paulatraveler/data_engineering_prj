from flask import Flask, request
import csv
import io
import pandas as pd
from calculate import calculate


app = Flask(__name__)


@app.route('/')
def index():
    return """
        <html>
            <body>
                <form action="/process" method="post" enctype="multipart/form-data">
                    <input type="file" name="input_csv"/>
                    <input type="submit"/>
                    </form>
                </body>
            </html>
    """


@app.route('/process', methods=['POST'])
def process():
    f = request.files['input_csv']
    if not f:
        return "Please provide a file"
    stream = io.StringIO(f.stream.read().decode("UTF-8"), newline=None)

    csv_data = [row for row in csv.reader(stream)]

    data = {
        'bone': [row[0] for row in csv_data],
        'muscle': [row[1] for row in csv_data],
        'number': [float(row[2]) for row in csv_data]
    }

    df = pd.DataFrame(data)

    result = calculate(df)
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
