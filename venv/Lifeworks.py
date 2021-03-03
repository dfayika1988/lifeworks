import flask
import os
from flask import request,jsonify, make_response, render_template
from flask import Flask

os.chdir('/Users/demilsonfayika/Desktop/lifeworks/venv')


app = Flask (__name__)

Data={}

Data['1'] = {
    "forename": "Jane",
    "surname": "Smith",
    "full_name": "Jane Smith",
    "date_of_birth": "2001/10/12",
    "location": "London",
    "company_id": 3
     }



Data['2'] = {

    "under30": {
        "forename": "Jane",
        "surname": "Smith",
        "date_of_birth": "2001/10/12",
        "location": "London",
        "company_id": 3,
         "forename": "Devika",
        "surname": "Patel",
        "date_of_birth": "1993/07/01",
        "location": "Manchester",
        "company_id": 3,
         "forename": "Tiago",
        "surname": "Silva",
        "date_of_birth": "1999/09/03",
        "location": "Lisbon",
        "company_id": 2,
          "forename": "Patrick",
        "surname": "Long",
        "date_of_birth": "1991/03/30",
        "location": "Hong Kong",
        "company_id": 3
     }
}



Data['3'] = {
    "forename": "Jane",
    "surname": "Smith",
    "date_of_birth": "2001/10/12",
    "location": "London",
    "company": {
        "id": 3,
        "name": "Solomon Sisters Bank",
        "headquarters": "London",
        "industry": "Finance"
     }
}



@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/all',methods=['GET'])
def display():
    return jsonify(Data)


@app.route('/data/<obj>',methods=['GET'])
def display_part(obj):
    if obj in Data:
        res = make_response(jsonify(Data[obj]),200)
        return res
    else:
        res =res = make_response(jsonify({"Error":"Object not found"}),404)
        return res
    

if __name__=="__main__":
    app.run()

