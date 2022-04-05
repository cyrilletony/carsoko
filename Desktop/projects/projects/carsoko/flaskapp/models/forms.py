from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from wtforms.fields.html5 import *

class MultipleCheckboxField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()
	
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    select = SelectMultipleField('Select', choices=[], validators=[InputRequired()])

class MainSearch(FlaskForm):
    make = SelectField('Make', choices = [])
    model = SelectField('Model', choices = [])
    price = SelectField('Price Range', choices = [])
    car_type = SelectField('Car Type', choices = [])
    fuel_type = SelectField('Car Type', choices = [])
    mileage = SelectField('Mileage', choices = [])
    drive_type = SelectField('Drive Type', choices = [])
    features = SelectField('Features', choices = [])

    
class Message(FlaskForm):
    name = StringField("Name",validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(),Email()])
    phone = StringField("Phone", validators=[InputRequired()])
    message = TextAreaField("Message", validators=[InputRequired()])
                


class AddListing(FlaskForm):
    name = StringField('Car Name', validators=[InputRequired()])
    description = TextAreaField('Description')
    #featured = SelectField('Featured', choices=[], )
    condition = SelectField('Condition', choices=[('one','New'),('two','Used'),('three','Foreign Used')], validators=[InputRequired()])
    car_type = SelectField('Car Type', choices=[], validators=[InputRequired()])
    make = SelectField('Make', choices=[], validators=[InputRequired()])
    model = SelectField('Model', validators=[InputRequired()])
    price = IntegerField('Price(Kshs. )', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    offer_type = SelectField('Offer Type',choices=[], validators=[InputRequired()])
    drive_type = SelectField('Drive Type',choices=[], validators=[InputRequired()])
    transmission = SelectField('Transmission',choices=[], validators=[InputRequired()])
    fuel_type = SelectField('Fuel Type',choices=[], validators=[InputRequired()])
    mileage = IntegerField('Mileage(Kms)', validators=[InputRequired()])
    engine_type = SelectField('Engine Type',choices=[], validators=[InputRequired()])
    cylinders = SelectField('Cylinders', choices=[], validators=[InputRequired()])
    color = SelectField('Colours', choices=[], validators=[InputRequired()])
    doors = SelectField('Doors', choices=[], validators=[InputRequired()])
    features = MultipleCheckboxField('Features', choices=[])
    VIN = StringField('Plate Number')
    gallery = MultipleFileField('Car Images', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])

class TypeField(FlaskForm):
	name = StringField('Name', validators=[InputRequired()])
	description = TextAreaField('Description')

class ModelForm(FlaskForm):
	name = StringField('Name', validators=[InputRequired()])
	description = TextAreaField('Description')
	make = SelectField('Make', choices=[], validators=[InputRequired()])

class FeatureForm(FlaskForm):
	description = TextAreaField('Feature',validators=[InputRequired()])
	
		