from flask_login import UserMixin,login_user,login_required,logout_user,LoginManager,current_user
from datetime import datetime
from app import db 

#class FormattedDateTime(db.DateTime):
#	def self.__set__(self,value):
#		return dateutil.parser.parse(value)
		
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
 
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Listing(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Integer)
	description = db.Column(db.PickleType())
	featured = db.Column(db.String(100))
	condition = db.Column(db.String(100))
	car_type_id = db.Column(db.Integer)
	car_model_id = db.Column(db.Integer)
	car_price = db.Column(db.Integer)
	year = db.Column(db.String(100))
	offer_type = db.Column(db.String(100))
	drive_type_id = db.Column(db.Integer)
	transmission_id = db.Column(db.Integer)
	fuel_type = db.Column(db.String(100))
	mileage = db.Column(db.String(500))
	engine_size = db.Column(db.String(100))
	cylinders_id = db.Column(db.Integer)
	color_id = db.Column(db.Integer)
	doors_id = db.Column(db.Integer)
	features = db.Column(db.PickleType())
	safety_features = db.Column(db.String(100000000))
	VIN = db.Column(db.String(100))
	images = db.Column(db.PickleType())
	location = db.Column(db.String(100000000))
	attachments = db.Column(db.String(100000000))
	author_id = db.Column(db.String(100))

	added_date = db.Column(db.DateTime, default=datetime.now)
	updated = db.Column(db.DateTime, default=datetime.now,  onupdate=datetime.now)

	def __repr__(self):
		return 'Listing {}'.format(self.id)

class Condition(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class CarType(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class CarMake(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)
class EngineType(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class CarModel(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	car_make_id = db.Column(db.Integer)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class OfferType(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class DriveType(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class Transmission(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class FuelType(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class Cylinders(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class Colors(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class Doors(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class Features(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)

class SafetyFeatures(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100000000))
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now)



	
		