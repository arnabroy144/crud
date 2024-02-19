# Create a new employee
from flask import Blueprint, jsonify, request
#from flask_marshmallow import Marshmallow
#from flask_sqlalchemy import SQLAlchemy
from app import db, Employee, ma


# Create a Blueprint for CRUD operations
crud_app = Blueprint('crud_app', __name__)



#db = SQLAlchemy()
#ma = Marshmallow()


# Define Employee Schema
class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone', 'email', 'password', 'status', 'created_on')

# Initialize Employee schema
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)



# Create a new employee
@crud_app.route('/employee', methods=['POST'])
def add_employee():
    name = request.json['name']
    phone = request.json['phone']
    email = request.json['email']
    password = request.json['password']
    status = request.json['status']

    new_employee = Employee(name=name, phone=phone, email=email, password=password, status=status)

    db.session.add(new_employee)
    db.session.commit()

    return jsonify({'message': ' employee created successfully.', 'name': name}), 201

# Get all employees
@crud_app.route('/employee', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = employees_schema.dump(employees)
    return jsonify(result)

# Get single employee by ID
@crud_app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    return employee_schema.jsonify(employee)

# Update an employee
@crud_app.route('/employee/<id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)

    name = request.json['name']
    phone = request.json['phone']
    email = request.json['email']
    password = request.json['password']
    status = request.json['status']

    employee.name = name
    employee.phone = phone
    employee.email = email
    employee.password = password
    employee.status = status

    db.session.commit()

    return jsonify(f"message : 'okey', name : {name}")

# Delete an employee
@crud_app.route('/employee/<id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully.',})
