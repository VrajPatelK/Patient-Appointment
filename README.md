## Patient Appointment Chatbot

### Puropose

* This project is a NLU based chatbot application developed for managing patient appointments. It utilizes various technologies and frameworks to provide an efficient and user-friendly experience. 

### Functionality
##### The chatbot application provides the following functionality:

* Book Appointment: Users can schedule appointments through the chatbot interface.
* Cancel Appointment: Users can cancel their existing appointments.
* The chatbot utilizes API calls to store appointment data in MongoDB and fetch data from the database. It also includes functionality for generating OTPs (One-Time Passwords) for verification purposes and generating unique appointment IDs for each appointment booked.

### Technology Used

##### Frontend Development

<img src="https://img.shields.io/badge/-React.js-61DAFB.svg" alt="React.js" style="margin-right:1rem">

<img src="https://img.shields.io/badge/-CSS-1572B6.svg" alt="CSS" style="margin-right:1rem">

##### Backend Development

<img src="https://img.shields.io/badge/-Python-3776AB.svg" alt="Python" style="margin-right:1rem">

<img src="https://img.shields.io/badge/-PyMongo-47A248.svg" alt="PyMongo" style="margin-right:1rem">

##### Frameworks

<img src="https://img.shields.io/badge/-RASA%20Framework-FF4088.svg" alt="RASA Framework" style="margin-right:1rem">

##### Database

<img src="https://img.shields.io/badge/-MongoDB-green.svg" alt="MongoDB" style="margin-right:1rem">

##### Tools

<img src="https://img.shields.io/badge/-GitHub-181717.svg" alt="GitHub" style="margin-right:1rem">

<img src="https://img.shields.io/badge/-Postman%20API-FF6C37.svg" alt="Postman API" style="margin-right:1rem">


## Setup Environment

### Option 1: Python version
- [python 3.9.13](https://www.python.org/downloads/release/python-3913/) 

### Option 2: Verrual environment & Download modules
- Create a virtual environment:
  ```bash
  python -m venv venv

- download modules:
  ```bash
  pip install -r requirements.txt


### Getting Started



1. Train the model

```
rasa train
```

2. To run action.py file

```
rasa run actions
```

3. To run the project and test using shell

```
rasa shell

4. to start rasa server to access on client side 

```
rasa run -m models --enable-api --cors "*"

- access on client side using .env file (add following key-value into .env)

REACT_APP_RASA="http://localhost:5005/webhooks/rest/webhook"


5. To reset the conversation state and starts a new dialogue session with the chatbot.

```
/restart
```

<hr>

###### Note: 

You can also use `rasa interactive` instead of `rasa shell`. By using `rasa interactive` command you can see the exchanged dialouges between bot and user.

<hr>

### Certificate

This is to certify that the project entitled <b>“Patient Appointment Chatbot”</b> is a Bonafide report of the work carried out by  ```Dhruv Patel (Roll No. IT098 ID No: 20ITUBS065) ``` | ```Gaurav Teli(Roll No. IT154 ID No: 20ITUBS007) ``` | ```Vraj Patel (Roll No. IT117 ID No: 20ITUOS071) ``` 
of the Department of Information Technology, semester VI. They were involved in Project work during the academic year ```2022-2023```.

### Contributers
The project was developed by the following individuals:

* ##### Dhruv Patel
* ##### Gaurav Teli
* ##### Vraj Patel
<br>

##### Project Guide

Prof. (Dr.) V. K. Dabhi and Prof. Harshad Prajapati<br>
Department of Information Technology<br>
Faculty of Technology<br>
Dharmsinh Desai University, Nadiad<br>

##### Head, Department of Information Technology

Prof. (Dr.) V. K. Dabhi<br>
Faculty of Technology<br>
Dharmsinh Desai University, Nadiad<br>
