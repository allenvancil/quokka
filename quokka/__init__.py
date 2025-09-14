from xml.etree.ElementInclude import default_loader

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Device(db.Model):
##  creates data column in anticipation of data to enter

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique = True, nullable=False)
    ip_address = db.Column(db.Text)
    vendor = db.Column(db.Text)
    os = db.Column(db.Text)
    hostname = db.Column(db.Text)

import quokka.views.ui_views
from quokka.controller.util import import_devices

with app.app_context():
    db.create_all()

    for device in import_devices():
        device_obj = Device(**device)
        db.session.add(device_obj)
    db.session.commit()