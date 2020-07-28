from flask import Flask
from snmpget import gather_data

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>SNMP Sucks</h1>"


@app.route('/api/cmts/<string:host>', methods=['GET'])
def cmts_api(host):
    output = gather_data(host, device_type="cmts")
    if output:
        return "cmts worked"
    else:
        return "check log - 'docker logs snmp-poller -f'"


@app.route('/api/cm/<string:host>', methods=['GET'])
def cm_api(host):
    output = gather_data(host, device_type="cm")
    if output:
        return "cm worked"
    else:
        return "check log - 'docker logs snmp-poller -f'"


# if __name__ == "__main___":
app.run(port=9998, debug=True)
