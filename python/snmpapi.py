from flask import Flask
from snmpget import gather_data

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>SNMP Sucks</h1>"


@app.route('/api/cmts/<string:host>', methods=['GET'])
def cmts_api(host):
    result = gather_data(host, device_type="cmts")
    if result:
        return "cmts worked"
    else:
        return "check log - 'docker logs snmp-poller -f'"


@app.route('/api/cm/<string:host>', methods=['GET'])
def cm_api(host):
    result = gather_data(host, device_type="cm")
    if result:
        return "cm worked"
    else:
        return "check log - 'docker logs snmp-poller -f'"


# if __name__ == "__main___":
app.run(host="0.0.0.0", port=9998, debug=True)
