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
from pymongo import MongoClient
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Text, List, Any, Dict
from rasa_sdk.events import SlotSet

DB_URL = "mongodb://localhost:27017"

client = MongoClient(DB_URL)

db = client["rasa"]
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


def generate_unique_id():
    digit_part = ''.join(secrets.choice(string.digits) for _ in range(5))
    char_part = ''.join(secrets.choice(string.ascii_letters) for _ in range(5))
    unique_id = f"{digit_part}_{char_part}"
    return unique_id


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
        dispatcher.utter_message(f"Hello {name}")
        doc = {
            "_id": "aid_"+str(int(round(time.time() * 10))),
            "name": name,
            "age": age,
            "mobile_no": mobile_no,
            "city": city,
            "bookedOn": str(datetime.datetime.today())
        }
        appointment.insert_one(doc)
        # reset all the slots .........
        slots = [
            SlotSet("name", None),
            SlotSet("age", None),
            SlotSet("mobile_no", None),
            SlotSet("city", None),
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

        if slot_value.lower() not in names:
            dispatcher.utter_message(
                text=f"We only accept name: gaurav/vraj/.rasa.")
            return {"name": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value}.")
        return {"name": slot_value}

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `age` value."""

        if int(slot_value) <= 0 and int(slot_value) > 150:
            dispatcher.utter_message(
                text=f"The entered age should be greater than 0 and less than equal to 150.")
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

        if slot_value.lower() not in CITIES:
            dispatcher.utter_message(
                text=f"{slot_value} is not come in our range ." + "/".join(CITIES))
            return {"city": None}
        dispatcher.utter_message(text=f"Your entered city is {slot_value}.")
        return {"city": slot_value}


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

        if len(slot_value) != 11:
            dispatcher.utter_message(
                text=f"{slot_value} Invalid Appointment ID .")
            return {"aid": None}

        # call API and  Print all the info about the Patient.

        dispatcher.utter_message(text=f"Yes Valid Appointment ID.")
        return {"aid": slot_value}

    # Logic for printing Message for Successfull Cancelation


class ResultForCancel(Action):

    def name(self) -> Text:
        return "action_successfull_cancel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        aid = tracker.get_slot("aid")
        dispatcher.utter_message(
            f"The Appointment for AID({aid}) is been canceled Successfully !")

        # reset all the slots .........
        slots = [
            SlotSet("aid", None)
        ]
        return slots
