from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy


# Create a Blueprint 
database_app = Blueprint('database_app', __name__)


db = SQLAlchemy()




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
