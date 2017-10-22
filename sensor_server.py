from flask import Flask
import json

# Rest API
app = Flask(__name__)

# Used to load output (later to be loaded from DB).
def load_data():
    f = open('output.json', 'r')
    data = json.dumps(f.read())
    f.close()
    return data

# Used to send data to Android app.
@app.route('/getsensorvalues', methods=['GET'])
def get_data():
    return load_data()

# Used to grab data from the LPC1768 and output to file (later to DB).
@app.route('/sendsensorvalue', methods=['PUT'])
def put_data():
    print("This will eventually be filled by something.")

try:
    app.run()
except KeyboardInterrupt:
    print("Exiting web service...")
