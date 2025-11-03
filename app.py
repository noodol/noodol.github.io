from flask import Flask, render_template, request, jsonify, send_file
import io
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-chart', methods=['POST'])
def generate_chart():
    # Get data (JSON from frontend)
    data = request.get_json()
    x = data['x']
    y = data['y']

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title("Input Data Chart")
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")

    # Save to memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
