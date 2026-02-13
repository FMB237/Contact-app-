'''Let Build a Crud app so we will need some basics opearions and end routes for our app  which is Creation,Updataing,reading and Delecting 
In other  to create a new user we need the following pieces of informations.
first_name, last_name and email of the person
So when a request is been submitted to the endpoint we will submit a post Create because the are mainly used to create
We have many other types of requests depending on what we wanna do 
The Get request are the request made to access something we alos have a PATCH request which is mainly used to Update our informations
So from this illustration our request from our Frontend will be Send to the backend so that it reponse to it.
You should also takes into consideration that the Repsonse can have a status 
Like the traditional 404 error which means not found

'''

#Let start building our Api 
#1. Let import out modules
from flask import request,jsonify # Jsonify to convert and manage json data 
from config import app,db
from model import Contact


#Let start building our endpoints
#1.Our home directoty
@app.route('/')
def index():
    return'<h1>Bruce Contact app</h1>'

@app.route("/Contacts",methods=["GET"])
def get_contacts():
    contacts =Contact.query.all() #To get all the query contacts inside our database sinnce we can retuen a python object we will return our data as json
    json_contacts=list(map(lambda x: x.to_json(),contacts)) #But this will return a map obejct which can easily be converted into a list
    return jsonify({"contacts":json_contacts})
    
#Now let app the route for creating the contact
@app.route("/Create_Contact",methods=["POST"])
def create_contact(): #Let request for all the data that we will enter
    first_name=request.json.get('firstName')
    last_name=request.json.get('lastName')
    email=request.json.get('email') #Note return the json data as it was in the json table

    #Now let ensure all this values exist
    if not first_name or not last_name or not email:
        return( 
            jsonify({"message":"You must include a first_name,last_name and email"}),
            400 
            )
    new_contact=Contact(first_name=first_name,last_name=last_name,email=email) #This is the format of our new contact now let add it to oour db using the try and except method
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message":str(e)}),400    

    return jsonify({"message":"User Created"}),201  
#Now create the route to update our users

@app.route('/update_contact/<int:user_id>',methods=["PATCH"])
def update_contact(user_id):
    contact= Contact.query.get(user_id)

    if not contact:
        return jsonify({"message":"User not found"}),404

    data=request.json
    contact.first_name = data.get("firstName",contact.first_name)    #This will check if the first_name exist and modified it if the is no update it will leave it like that 
    contact.last_name  = data.get("lastName",contact.last_name)
    contact.email = data.get("email",contact.email)
     
     #Add the new data into the db 
    db.session.commit()
    return jsonify({"message":"User updated"}),200


#Now let delect our users
@app.route('/delete_contact/<int:user_id>',methods=["DELETE"])
def delete_contact(user_id):
    contact= Contact.query.get(user_id)

    if not contact:
        return jsonify({"message":"User not found"}),404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message":"User deleted"}),200



# let initialse our server
if __name__=="__main__": #Let instant our db  
    with app.app_context():
     db.create_all()
   # This will all our the db model inside our model.py
    app.run(debug=True,host="0.0.0.0") #The host used so that even the address localhost and 127.0.0.1 should be consider
