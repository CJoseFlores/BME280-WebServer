from flask import request
from flask_api import FlaskAPI
from datetime import datetime
import json

# Rest API
app = FlaskAPI(__name__)

# Used to load output (later to be loaded from DB).
def load_data():
    f = open('output.json', 'r')
    data = json.loads(f.read())
    f.close()
    return data

# Used to save JSON to output file (later to be saved to DB).
def store_data(sensor_data):
    f = open('test.json', 'w')
    f.write(json.dumps(sensor_data, indent=2))
    f.close()

# Used to send data to Android app.
@app.route('/getsensorvalues', methods=['GET'])
def get_data():
    return load_data()

# Used to grab data from the LPC1768 and output to file (later to DB).
@app.route('/sendsensorvalue', methods=['POST'])
def put_data():
    sensor_data = request.data # Grabbing JSON Dict sent from POST Request.
    store_data(sensor_data)
    print "+++++++++++++++++++++++++++++++++++++++++++++++\n"
    print "The Following JSON Packet was saved and stored: \n"
    print json.dumps(sensor_data, indent=2)
    print "\n++++++++++++++++++++++++++++++++++++++++++++++"
    return "Packet was recieved and stored.\n" 

try:
    app.run(host="0.0.0.0") # Setting host to default route to allow LAN access.
except KeyboardInterrupt:
    print("Exiting web service...")
