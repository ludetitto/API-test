from flask import Flask, send_file
import addTicket
import deleteTicket
import getNetworkDevices
import updateNetworkDevice
import io

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/addTicket')
def add_ticket():
    try:
        result = addTicket.main()
        return str(result)
    except Exception as e:
        return str(e), 500

@app.route('/api/deleteTicket')
def delete_ticket():
    try:
        result = deleteTicket.main()
        return str(result)
    except Exception as e:
        return str(e), 500

@app.route('/api/getNetworkDevices')
def get_network_devices():
    try:
        result = getNetworkDevices.main()
        return str(result)
    except Exception as e:
        return str(e), 500

@app.route('/api/updateNetworkDevice')
def update_network_device():
    try:
        result = updateNetworkDevice.main()
        return str(result)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
