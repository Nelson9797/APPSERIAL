"""
from flask import Flask, jsonify, render_template
import serial
import threading

app = Flask(__name__)

data = {"temp": 0, "gas": "Bueno"}

def read_serial():
    global data
    with serial.Serial('COM6', 9600, timeout=1) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith("Temp:"):
                    data["temp"] = int(line.split(': ')[1])
                elif line.startswith("Gas:"):
                    data["gas"] = line.split(': ')[1]
            except Exception as e:
                print(f"Error reading serial data: {e}")

threading.Thread(target=read_serial, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
"""

'''  Este código funciona normal moestrando datos de temperatura y de gas no esta mostrando tan bien.
from flask import Flask, jsonify, render_template
import serial
import threading

app = Flask(__name__)

data = {"temp": 0, "gas": "Bueno"}

def read_serial():
    global data
    with serial.Serial('COM6', 9600, timeout=1) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith("Temp:"):
                    data["temp"] = int(line.split(': ')[1])
                elif line.startswith("Gas:"):
                    data["gas"] = line.split(': ')[1]
            except Exception as e:
                print(f"Error reading serial data: {e}")

threading.Thread(target=read_serial, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
'''

from flask import Flask, jsonify, render_template
import serial
import threading

app = Flask(__name__)

data = {"temp": 0, "gas": "Bueno"}

def read_serial():
    global data
    with serial.Serial('COM6', 9600, timeout=1) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith("Temp:"):
                    data["temp"] = int(line.split(': ')[1])
                elif line.startswith("Gas:"):
                    data["gas"] = line.split(': ')[1]
            except Exception as e:
                print(f"Error reading serial data: {e}")

threading.Thread(target=read_serial, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
