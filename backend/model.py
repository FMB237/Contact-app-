from config import db #imporing our db from config.py
#Now let us create a class for our database model 
#Note that each represent a database file 

class Contact(db.Model): #All database instants should have and id first 
    id=db.Column(db.Integer,primary_key=True) # For our contact we will have a first_name and last_name and an email
    first_name=db.Column(db.String(50),nullable=False,unique=False)
    last_name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True) # unique since each personne need to have an unique email

    def to_json(self): #This is a function build to turn up all our data from the contact into a Json format so that our javascript front can used it 
        return{
            "id":self.id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email #We use pass json data 
        }


