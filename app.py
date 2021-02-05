#!/usr/bin/python3

from application import app
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


