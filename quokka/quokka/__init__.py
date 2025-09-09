from xml.etree.ElementInclude import default_loader

from flask import Flask
import yaml

app = Flask(__name__)
def import_devices():
    with open("quokka/data/devices.yaml") as devices_file:
        devices = yaml.safe_load(devices_file.read())
        return devices

@app.route("/device/")
def devices():
    devices = import_devices()

    return {"devices":devices}