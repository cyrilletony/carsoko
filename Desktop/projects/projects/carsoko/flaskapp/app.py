#import pickle5 as pickle
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import UserMixin,login_user,login_required,logout_user,current_user,LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import *
from werkzeug.utils import secure_filename
from datetime import datetime
from models.forms import *
import os, itertools
 
app  = Flask(__name__,template_folder='Templates')

UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = {'txt','pdf','png','jpg','jpeg','gif'}
 
app.config['SECRET_KEY'] = "fjdnefwe4v33bnsjwwfjgyuadvcfqhefrwjrwefs" 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/carsoko'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 60
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 *5
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db
Session(app)
socketio = SocketIO(app)

"""login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"""

from database import *



@app.route('/')
def index():
  return redirect('/home')

@app.route('/home')
def home():
    form = MainSearch()
    types = db.session.query(Listing.description,Listing.condition,Listing.added_date,CarMake.name,CarModel.name,CarType.name,Listing.car_price,Listing.year,FuelType.name,Listing.mileage,Colors.name,Listing.id,Listing.images,Listing.featured)\
            .outerjoin(CarMake,Listing.name == CarMake.id)\
            .outerjoin(CarModel, Listing.car_model_id == CarModel.id)\
            .outerjoin(CarType, Listing.car_type_id == CarType.id)\
            .outerjoin(FuelType, Listing.fuel_type == FuelType.id)\
            .outerjoin(Colors, Listing.color_id == Colors.id)\
            .order_by(Listing.added_date.desc())\
            .limit(16)\
            .all()
    form.make.choices = [(select.id, select.name) for select in CarMake.query.all()]
    form.price.choices = [(100000,'Max - 100,000'), (1000000,'Max - 1,000,000'),(2000000,'Max - 2,000,000'),(5000000,'Max - 5,000,000'),(10000000,'Max - 10,000,000')]
    return render_template('app/home.html',form = form, type = types)
@app.route('/search',methods = ['GET','POST'])
def search():
    form = MainSearch()
    #if form.validate_on_submit():
    if request.method == 'POST':
        print("search..")
        searched = db.session.query(Listing.description,Listing.condition,Listing.added_date,CarMake.name,CarModel.name,CarType.name,Listing.car_price,Listing.year,FuelType.name,Listing.mileage,Colors.name ,Listing.id,Listing.images,Listing.featured,Listing.features,Doors.name,DriveType.name,Transmission.name,Cylinders.name,EngineType.name,Listing.VIN)\
            .filter(Listing.name.like(request.form['make']), Listing.car_model_id.like(request.form['model']))\
            .outerjoin(CarMake,Listing.name == CarMake.id)\
            .outerjoin(CarModel, Listing.car_model_id == CarModel.id)\
            .outerjoin(CarType, Listing.car_type_id == CarType.id)\
            .outerjoin(FuelType, Listing.fuel_type == FuelType.id)\
            .outerjoin(Colors, Listing.color_id == Colors.id)\
            .outerjoin(DriveType, Listing.drive_type_id == DriveType.id)\
            .outerjoin(Transmission, Listing.transmission_id== Transmission.id)\
            .outerjoin(Cylinders, Listing.cylinders_id == Cylinders.id)\
            .outerjoin(EngineType, Listing.engine_size == EngineType.id)\
            .outerjoin(Doors, Listing.doors_id == Doors.id)\
            .all()
        
        """if request.form['model']:
            searched = searched
        if request.form['price']:
            searched = searched.filter(Listing.name.like(request.form['make']), Listing.car_model_id.like(request.form['model']),Listing.car_price <= request.form['price']).all()
        print(searched)"""
        form.make.choices = [(select.id, select.name) for select in CarMake.query.all()]
        form.features.choices = [(select.id, select.name) for select in Features.query.all()]
        form.price.choices = [(100000,'Max - 100,000'), (1000000,'Max - 1,000,000'),(2000000,'Max - 2,000,000'),(5000000,'Max - 5,000,000'),(10000000,'Max - 10,000,000')]
        return render_template('carsoko/search.html', form = form, type = searched)
    return render_template('carsoko/search.html', form = form)

def Car_Features(features):
    feature_list = []
    for feature in features:
        f_name = Features.query.filter_by(id=feature).first()
        feature_list.append(f_name.name)
    return feature_list

@app.route('/listing/<car>')
def car_listing(car):
    car_details = db.session.query(
                Listing.description,    
                Listing.condition,      
                Listing.added_date,      
                CarMake.name,           
                CarModel.name,          
                CarType.name,           
                Listing.car_price,       
                Listing.year,           
                FuelType.name,           
                Listing.mileage,         
                Colors.name ,            
                Listing.id,
                Listing.images,
                Listing.featured,
                Listing.features,
                Doors.name,
                DriveType.name,
                Transmission.name,
                Cylinders.name,
                EngineType.name,
                Listing.VIN
                )\
            .filter((Listing.id == car))\
            .outerjoin(CarMake,Listing.name == CarMake.id)\
            .outerjoin(CarModel, Listing.car_model_id == CarModel.id)\
            .outerjoin(CarType, Listing.car_type_id == CarType.id)\
            .outerjoin(FuelType, Listing.fuel_type == FuelType.id)\
            .outerjoin(Colors, Listing.color_id == Colors.id)\
            .outerjoin(DriveType, Listing.drive_type_id == DriveType.id)\
            .outerjoin(Transmission, Listing.transmission_id== Transmission.id)\
            .outerjoin(Cylinders, Listing.cylinders_id == Cylinders.id)\
            .outerjoin(EngineType, Listing.engine_size == EngineType.id)\
            .outerjoin(Doors, Listing.doors_id == Doors.id)\
            .first()
    #print(car_details)
    features = Car_Features(car_details[14])
    desc = "<div class='note note-success'>"+str(car_details[0])+"</div>"
    messageform = Message()
    form = MainSearch()
    form.make.choices = [(select.id, select.name) for select in CarMake.query.all()]
    return render_template('carsoko/car.html', car = car_details, features = features, desc = desc,form = form, form1 = messageform)

@app.route("/message/<back>", methods = ['GET', 'POST'])
def message(back):
    messageform = Message()
    if messageform.validate_on_submit():
        print("we are okay")
        flash("It's Okay here....")
        return redirect("/listing/{}".format(back))
    
    print("an issue occured")
    flash("problems encoutered")
    return redirect("/listing/{}".format(back))

@app.route("/admin")
def admin():
    return render_template('app/admin.html')

@app.route('/login' , methods = ['GET', 'POST'])
def Login():
    form = LoginForm()

    form.select.choices = [(str(select.id), select.name) for select in CarType.query.all()]
    if form.validate_on_submit():
          if request.form['username'] != 'tony' or request.form['password'] != '12345':
                flash("Invalid Credentials, Please Try Again")
          else:
                print(request.form.getlist('select'))
                return redirect(url_for('index'))

    return render_template('app/login.html', form = form)
@app.route('/admin/<page>',methods = ['GET','POST'])
def listing(page):
    return render_template('admin/{}.html'.format(page))

@app.route('/admin/listing/<page>',methods = ['GET','POST'])
def listing_index(page):
        now = datetime.now()
        Array = {'condition':Condition,'make':CarMake,"doors":Doors,"fuel_type":FuelType,
        'safety_features':SafetyFeatures,'offer_type':OfferType,
        'transmission':Transmission,'type':CarType,"color":Colors,"drive_type":DriveType,
        "cylinders":Cylinders,"engine_type":EngineType}
        if page == "new_listing":
            form = AddListing()
            form.make.choices = [(select.id, select.name) for select in CarMake.query.all()]
            form.doors.choices = [(select.id, select.name) for select in Doors.query.all()]
            form.color.choices = [(select.id, select.name) for select in Colors.query.all()]
            form.cylinders.choices = [(select.id, select.name) for select in Cylinders.query.all()]
            form.fuel_type.choices = [(select.id, select.name) for select in FuelType.query.all()]
            form.transmission.choices = [(select.id, select.name) for select in Transmission.query.all()]
            form.drive_type.choices = [(select.id, select.name) for select in DriveType.query.all()]
            form.offer_type.choices = [(select.id, select.name) for select in OfferType.query.all()]
            form.condition.choices = [(select.id, select.name) for select in Condition.query.all()]
            form.car_type.choices = [(select.id, select.name) for select in CarType.query.all()]
            form.features.choices = [(select.id, select.name) for select in Features.query.all()]
            form.doors.choices = [(select.id, select.name) for select in Doors.query.all()]
            form.engine_type.choices = [(select.id, select.name) for select in EngineType.query.all()]

            return render_template('listing/{}.html'.format(page),form=form)
        
        if page == "cars":
            types = db.session.query(
                Listing.description,    #0
                Listing.condition,      #1
                Listing.added_date,     #2 
                CarMake.name,           #3
                CarModel.name,          #4
                CarType.name,           #5
                Listing.car_price,      #6 
                Listing.year,           #7
                FuelType.name,          #8 
                Listing.mileage,        #9 
                Colors.name ,            #10
                Listing.id
                )\
            .outerjoin(CarMake,Listing.name == CarMake.id)\
            .outerjoin(CarModel, Listing.car_model_id == CarModel.id)\
            .outerjoin(CarType, Listing.car_type_id == CarType.id)\
            .outerjoin(FuelType, Listing.fuel_type == FuelType.id)\
            .outerjoin(Colors, Listing.color_id == Colors.id)\
            .all()
            #print(types)
            return render_template('listing/{}.html'.format(page), type = types)
        if page == "model":
            form = ModelForm()
            form.make.choices = [(str(select.id), select.name) for select in CarMake.query.all()]
            models = CarModel.query.all()
            if form.validate_on_submit():
                return render_template('listing/{}.html'.format(page),form=form,model= models)
            return render_template('listing/{}.html'.format(page),form=form,model= models)
        if page == "features":
            form = FeatureForm()
            makes = Features.query.all()
            return render_template('listing/{}.html'.format(page),form=form,make = makes)
        if Array[page]:
            print("hello")
            form = TypeField()
            types = Array[page].query.all() 
            return render_template('listing/{}.html'.format(page),form=form,type=types)
        else:
            return render_template('listing/{}.html'.format(page))



@app.route('/adding/<page>',methods = ['GET','POST'])
def adding(page):
    Array = {'condition':Condition,'make':CarMake,"doors":Doors,"fuel_type":FuelType,
    'features':Features,'safety_features':SafetyFeatures,'offer_type':OfferType,
    'transmission':Transmission,'type':CarType,"color":Colors,"drive_type":DriveType,
    "cylinders":Cylinders,"engine_type":EngineType}
    #print(Array[page])
    now = datetime.now()
    form = TypeField()
    types = Array[page].query.all()
    new = Array[page](name = request.form.get('name'),
        description = request.form.get('description'),
        created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        )
    print('there')
    try:
        db.session.add(new)
        db.session.commit()
        flash("Condition added succefully")
        print('there2')
        types = Array[page].query.all()
        return redirect('/admin/listing/{}'.format(page))
    except:
        print('there3')
        flash("An issue occured while saving your data")
        return redirect('/admin/listing/{}'.format(page))
    flash("Your details was not submitted!")
    return redirect('/admin/listing/{}'.format(page))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploadimages(images,name,file):
    image = {}
    if file.filename == '':
        return images
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image['view'] = name
        image['filename'] = filename
        images.append(image)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return images
   
@app.route('/addlisting',methods = ['GET','POST'])
def addlisting():
    now = datetime.now()
    images = []
    images = uploadimages(images,'front',request.files['front'])
    images = uploadimages(images,'back',request.files['back'])
    images = uploadimages(images,'frontright',request.files['frontright'])
    images = uploadimages(images,'frontleft',request.files['frontleft'])
    images = uploadimages(images,'backright',request.files['backright'])
    images = uploadimages(images,'backleft',request.files['backleft'])
    images = uploadimages(images,'left',request.files['left'])
    images = uploadimages(images,'right',request.files['right'])
    print(images)
    print(request.form.get('model'))
    new = Listing(name = request.form.get('make'),
    description = request.form.get('description'),
    featured = request.form.get('featured'),
    condition = request.form.get('condition'),
    car_type_id = request.form.get('car_type'),
    car_model_id = request.form.get('model'),
    car_price = request.form.get('price'),
    year = request.form.get('year'),
    offer_type = request.form.get('offer_type'),
    drive_type_id = request.form.get('drive_type'),
    transmission_id = request.form.get('transmission'),
    fuel_type = request.form.get('fuel_type'),
    mileage = request.form.get('mileage'),
    engine_size = request.form.get('engine_type'),
    cylinders_id = request.form.get('cylinders'),
    color_id = request.form.get('color'),
    doors_id = request.form.get('doors'),
    features = request.form.getlist('features'),
    VIN = request.form.get('VIN'),
    images = images,
    author_id = "ADMIN 1",
    added_date = now.strftime("%Y-%m-%d %H:%M:%S"),
    updated = now.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        db.session.add(new)
        db.session.commit()
        print('there2')
        flash("Car added succefully")
        return redirect('/admin/listing/new_listing')
    except:
        print('there3')
        flash("An issue occured while saving your data")
        return redirect('/admin/listing/new_listing')

    flash("Internal Error while Uploadig details!")
    return redirect('admin/listing/new_listing')
@app.route('/addingmodel',methods = ['GET','POST'])
def addingmodel():
    now = datetime.now()
    form = ModelForm()
    types = CarModel.query.all()
    print(request.form.get('make'))
    new = CarModel(name = request.form.get('name'),
        description = request.form.get('description'),
        car_make_id = request.form.get('make'),
        created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        )
    print('there')
    try:
        db.session.add(new)
        db.session.commit()
        flash("Condition added succefully")
        print('there2')
        types = CarModel.query.all()
        return redirect('/admin/listing/model')
    except:
        print('there3')
        flash("An issue occured while saving your data")
        return redirect('/admin/listing/model')
    #print("nothung")
    #return redirect('/listing/model')
@app.route('/updater/<item>',methods = ['GET','POST'])
def dynamic(item):
    models = CarModel.query.filter_by(car_make_id=item).all()
    modelArray = []
    for model in models:
        modelObj = {}
        modelObj['id'] = model.id
        modelObj['name'] = model.name
        modelArray.append(modelObj)
    return jsonify({'models':modelArray})

@app.route('/cars',methods = ['GET','POST'])
def cars():
    make = CarMake.query.all()
    carArray = []
    for car in make:
        carObj = {}
        carObj['id'] = car.id
        carObj['name'] = car.name
        carArray.append(carObj)
    return jsonify({'models':carArray})

@socketio.on('message')
def handle_message(data):
    print(request.sid)
    print('received message: ' + data['data'])
    emit('received', "message received....")

@socketio.on('tally')
def tally(data):
    print(data)
    emit('retally', "message received....")

if __name__ == "__main__":
    
    socketio.run(app, debug=True)