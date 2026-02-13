# This is a Simple Full-Stack App i will build using Javascript for the Frontend and Python for the Backend
**So for the Frontend we will using React Js and For the Backend we will used Flask which is a python framework**
---
**This course is mainly coming from the Youtube channel of Tech with Tim with Tim and it main aim is to build Full-stack application**
---
# Step 1 : Setting up the application 
Let create a python environment 

***python3 -m vevn venv*** This command will create our python virtual env then install flask and some other modules for our app.The fisrt module to install for our app developpement is Flask 
So let install it using tje command **pip install flask and some other package like SQLAlchemy and flask-cors**
1. Flask is the basics package framework we will install for our app
2. Flask-Sqlachemy will permit us to handle the database of our app using Sqlite 
3. flask-cors will permit us to handle cross requests for our app.


---
**We will create 2 folders one for the backend and the other one for the frontend**
This app is the contact list app so it is mainly CRUD 
The Folder call Backend is where all the backend of our is going to live.
The folder with name frontend will whole all our frontend code.

For the Frontend we will install React + vite
For that we need to ensure that nodejs is been install on our machine using the command **node -v && npm -v** into our terminal if not install them 
For Linux apt distos need the command **sudo apt install nodejs npm** this will install and LTS version of nodejs that  will be used for our project building 
Then we will create a new project with using the command **npm create vite@latest frontend -- template react**
This will create a simple react+vite project into a folder know as frontend for the Frontend of our app.
Then we will enter inside the fronend folder and used the command npm install in other to install all the dependencies we need for working with our app.
Then run our project with the command **npm run dev**

---

**Step2:Building the Backend**
Move on to our backend folder and create some files
1. main.py : Will contains all the main routes of our app.
2. model.py : Contains our file database configs
3. config.py :This file will contain our app main configuaraions

**The first time to is to build the API first so move on to the config.py file.**
1. Import our flask mogules
2. initiase our app
3. Initialsie our database
4. Create a database intsant 
   
**Second move to the model.py for database settings**
1. imporing our db from config.py
2. Creating our Contact db model which have an id,first_name,lastname,email.
3. Then create a function which will convert this data into json to be use after for our frontend

**Third move to main.py for our routes and mode app configs**
Let Build a Crud app so we will need some basics opearions and end routes for our app  which is Creation,Updataing,reading and Delecting.
In other  to create a new user we need the following pieces of informations which are :
1. first_name
2. last_name 
3. email of the person
So when a request is been submitted to the endpoint we will submit a post Create because the are mainly used to create
We have many other types of requests depending on what we wanna do 
The Get request are the request made to access something we alos have a PATCH request which is mainly used to Update our informations
So from this illustration our request from our Frontend will be Send to the backend so that it reponse to it.
You should also takes into consideration that the Repsonse can have a status 
Like the traditional 404 error which means not found or our 400 response meaning fails or when the 200 responsev for good 
So all this is the structure for building an API

---
The Api is now build

**Fouth move building our Frontend**
