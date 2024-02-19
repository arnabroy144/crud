from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize Flask app
app = Flask(__name__)

# Configure MySQL database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:@127.0.0.1:3306/one_assesment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Employee table
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    status = db.Column(db.Enum('active', 'inactive'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, phone, email, password, status):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.status = status

# Experience table
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    company_name = db.Column(db.String(50), unique=False, nullable=False)
    role = db.Column(db.String(50), unique=False, nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)
    last_date = db.Column(db.Date, nullable=False)

    def __init__(self, employee_id, company_name, role, date_of_joining, last_date):
        self.employee_id = employee_id
        self.company_name = company_name
        self.role = role
        self.date_of_joining = date_of_joining
        self.last_date = last_date



# Import and register CRUD operations from crud.py
from crud import crud_app
app.register_blueprint(crud_app)

if __name__ == '__main__':
    app.run(debug=True)