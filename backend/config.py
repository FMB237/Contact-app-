#importing the flask module
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS #CORS(Cross origin requests) So is allows us to send requests to this backend from a differcent URL
# SO in app using simple Html page for our Frontend we does need cors.

app =Flask(__name__) #To initialise our flask app
CORS(app) # Then Put our app into cors

#Now let initialise our DB

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"# Note we can give any name for our db 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False  #Let not just track all the modifications inside our db for now so this will be optional for now 

#Let now create and instant of the database
db =SQLAlchemy(app) # Which will give us access to our database

