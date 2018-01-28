from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import os
from json import dumps

# Assuming salaries.db is in your app root folder
e = create_engine('sqlite:///salaries.db')  # loads db into memory

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

class Departments_Meta(Resource):
	def get(self):
		conn = e.connect()  # open connection to memory data
		query = conn.execute("select distinct DEPARTMENT from salaries")  # query
		return {'departments': [i[0] for i in query.cursor.fetchall()]}  # format results in dict format

class Departmental_Salary(Resource):
    def get(self, department_name):  # param is pulled from url string
    	conn = e.connect()
    	query = conn.execute("select * from salaries where Department='%s'"%department_name.upper())
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class multiply(Resource):
    '''dummy function to test apis'''
    def get(self, number):  # param must match uri identifier
        return number * 2

# once we've defined our api functionalities, add them to the master API object
api.add_resource(Departments_Meta, '/departments')  # bind url identifier to class
api.add_resource(Departmental_Salary, '/dept/<string:department_name>')  # bind url identifier to class; also make it querable
api.add_resource(multiply, '/multiply/<int:number>')  # whatever the number is, multiply by 2

if __name__ == '__main__':
        # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
        app.run(debug=True)
