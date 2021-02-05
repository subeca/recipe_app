#!/usr/bin/python3

from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length
from datetime import datetime


class Recipes(db.Model):
    title = db.Column(db.String(300), pimary_key=True)
    description = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    method = db.Column(db.String(5000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    creator_name = db.Column(db.String(30), nullable=False)
    reviews= db.relationship("Reviews", backref="recipes")

class Reviews(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_title= db.Column(db.String(300), db.ForeignKey('Recipes.title'), nullable=False)
    title= db.Column(db.String(300), nullable=False)
    date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reviewer_name=db.Column(db.String(30))
    review=db.Column(db.String(3000), nullable=False)
    rating=db.Column(db.Integer, nullable=False)


class myForm_Add(FlaskForm):
    title = StringField('Title', [Length(min=1, max=300)])
    description = StringField("Description", [Length(min=1, max=300)])
    category = StringField ("Category",  [Length(min=1, max=30)])
    ingredients = StringField("Ingredients", [Length(min=1, max=200)])
    method = StringField("Method", [Length(min=1, max=5000)])
    date_created = DateField('Date Created', validators=[DataRequired()])
    create_name = StringField('Name', [Length(min=1, max=20)])

class myForm_Review(FlaskForm):
    title= StringField("Review title", [Length(min=1, max=300)])
    reviewer_name = StringField('Reviewer name', [Length(min=0, max=30)])
    review=StringField ("Review - 3000 characters max.", [Length(min=1, max=3000)])
    rating= IntegerField("Rating out of 5", validators=[DataRequired(), NumberRange(1,5)])
    submit = SubmitField('Add Review')

class myForm_Update(FlaskForm):
    submit= SubmitField("Update Review")

class myForm_Delete(FlaskForm):
    submit= SubmitField("Delete Review")


