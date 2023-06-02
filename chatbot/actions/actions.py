# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import datetime
import time
import string
import secrets
import certifi
import ssl
from pymongo import MongoClient
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Text, List, Any, Dict
from rasa_sdk.events import SlotSet
from actions.sendMailFunction import sendMail

# mongodb+srv://gauravteli:gauravteli@cluster0.iykzyey.mongodb.net/?retryWrites=true&w=majority
# DB_URL = "mongodb://localhost:27017"
DB_URL = "mongodb+srv://gauravteli:gauravteli@cluster0.iykzyey.mongodb.net/?retryWrites=true&w=majority"

# adding not adding the security by Secure Socket Layer
client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)

print("connected successfully")

db = client["Rasa"]
appointment = db["appointment"]

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

names = ["gaurav", "vraj", ".rasa"]
CITIES = [
    "mumbai",
    "delhi",
    "bangalore",
    "kolkata",
    "chennai",
    "hyderabad",
    "ahmedabad",
    "pune",
    "surat",
    "jaipur",
    "lucknow",
    "kanpur",
    "nagpur",
    "indore",
    "thane"
]


# generating a unique Appointment Id ->
def generate_unique_id():
    digit_part = ''.join(secrets.choice(string.digits) for _ in range(5))
    char_part = ''.join(secrets.choice(string.ascii_letters) for _ in range(5))
    unique_id = f"{digit_part}_{char_part}"
    return unique_id

from actions.uniqueId import unique_aid
# printing got appointment
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_get_form_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        age = tracker.get_slot("age")
        mobile_no = tracker.get_slot("mobile_no")
        city = tracker.get_slot("city")
        email = tracker.get_slot("email")
        aid = unique_aid()
        print(aid)
        doc = {
            "_id": aid,
            "name": name,
            "age": age,
            "mobile_no": mobile_no,
            "city": city,
            "email": email,
            "status": "pending",
            "bookedOn": str(datetime.datetime.today())
        }
        appointment.insert_one(doc)
        dispatcher.utter_message(
            f"Hello {name} your appointment ID is {aid}. Remember your appointment ID for future reference !")
        # reset all the slots .........
        slots = [
            SlotSet("name", None),
            SlotSet("age", None),
            SlotSet("mobile_no", None),
            SlotSet("city", None),
            SlotSet("email", None),
            SlotSet("otp", None),
            SlotSet("sentOTP", None),
        ]
        return slots

# validation logic for appointment


class ValidateAppForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_app_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""

        if slot_value is None:
            dispatcher.utter_message(
                text=f"Enter name again")
            return {"name": None}
        dispatcher.utter_message(
            text=f"OK! Your entered name is {slot_value}.")
        return {"name": slot_value}

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `age` value."""

        if int(slot_value) <= 5 and int(slot_value) > 100:
            dispatcher.utter_message(
                text="Your age must be in between 5 and 100 !")
            return {"age": None}
        dispatcher.utter_message(text=f"OK! Your entered age is {slot_value}.")
        return {"age": slot_value}

    def validate_mobile_no(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        if len(slot_value.lower()) != 10:
            dispatcher.utter_message(
                text=f"We only accept mobile no. with 10 digits .")
            return {"mobile_no": None}
        dispatcher.utter_message(
            text=f"OK! your mobile number is {slot_value}.")
        return {"mobile_no": slot_value}

    def validate_city(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `city` value."""

        if slot_value is None:
            dispatcher.utter_message(
                text="Please Enter City name again")
            return {"city": None}
        dispatcher.utter_message(text=f"Your entered city is {slot_value}.")
        return {"city": slot_value}

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email` value."""

        dispatcher.utter_message(
            text=f"Your entered Email ID is {slot_value}.")
        # otp = sendMail(slot_value)
        otp = "123456"
        print(slot_value,otp)
        return {"email": slot_value, "sentOTP": otp}

    def validate_otp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `otp` value."""

        sentOTP = tracker.get_slot("sentOTP")

        if slot_value != sentOTP:
            dispatcher.utter_message(
                text=f"Inavlid OTP Entered, Plz enter the valid OTP 😤!")
            return {"otp": None}
        else:
            dispatcher.utter_message(text=f"OTP Validation Successfull 🫡 !")
            return {"otp": slot_value}

#  for cancelation of form ..


class ValidateCancelForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_cancel_form"

    def validate_aid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aid` value."""

        # call API and  Print all the info about the Patient.
        dt = appointment.find_one({"_id": slot_value})
        if dt == None:
            dispatcher.utter_message(
                text=f"{slot_value} Invalid Appointment ID .")
            return {"aid": None}
        elif dt["status"] == "cancelled":
            dispatcher.utter_message(
                text=f"Already Cancelled the Appointment for AID {slot_value} ")
            return {"aid": slot_value, "requested_slot": None}
        else:
            email = dt["email"]
            otp = sendMail(email)
            # otp="123457"
            print(otp)
            dispatcher.utter_message(
                text=f"Yes Valid Appointment ID. and OTP is send to your registered email "+email)
            return {"aid": slot_value, "sentOTP": otp}

    def validate_otp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `otp` value."""

        sentOTP = tracker.get_slot("sentOTP")

        if slot_value != sentOTP:
            dispatcher.utter_message(
                text=f"Inavlid OTP Entered, Plz enter the valid OTP 😤!")
            return {"otp": None}
        else:
            dispatcher.utter_message(text=f"OTP Validation Successfull 🫡 !")
            return {"otp": slot_value}

    # Logic for printing Message for Successfull Cancelation


class ResultForCancel(Action):

    def name(self) -> Text:
        return "action_successfull_cancel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        aid = tracker.get_slot("aid")
        otp = tracker.get_slot("otp")
        sentOTP = tracker.get_slot("sentOTP")
        if appointment.find_one({"_id": aid}) is not None:
            if otp == sentOTP:
                appointment.update_one(
                    {"_id": aid}, {"$set": {"status": "cancelled"}})
                data = "Your Appointment has been cancelled for AID : " + aid
            else:
                data = ("Wrong OTP")
        else:
            data = "No record match with aid: "+aid
        dispatcher.utter_message(text=data)

        # reset all the slots .........
        slots = [
            SlotSet("aid", None),
            SlotSet("otp", None),
            SlotSet("sentOTP", None)
        ]
        return slots

    # ###############################


#  for status check form ..

# class ValidateStatusForm(FormValidationAction):

#     def name(self) -> Text:
#         return "validate_status_form"

#     def validate_aid(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `aid` value."""


#         # call API and  Print all the info about the Patient.
#         dt = appointment.find_one({"_id": slot_value})
#         if dt == None:
#             dispatcher.utter_message(
#                 text=f"{slot_value} Invalid Appointment ID . or you have not booked the appointment !")
#             return {"aid": None}
#         else:
#             email = dt["email"]
#             dispatcher.utter_message(text=f"Yes Valid Appointment ID. and your email is {email}")
#             return {"aid": slot_value}

# class ResultForStatus(Action):

#     def name(self) -> Text:
#         return "action_status_information"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


#         aid = tracker.get_slot("aid")
#         print(aid)
#         dt = appointment.find_one({"_id": aid})
#         email = dt["email"]
#         name = dt["name"]
#         status = dt["status"]
#         aid = dt["_id"]
#         dispatcher.utter_message(f"aid: {aid} ,name: {name} ,email: {email}, status: {status}")

#         # reset all the slots .........
#         slots = [
#             SlotSet("aid", None)
#         ]
#         return slots
