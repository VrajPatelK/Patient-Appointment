# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Text, List, Any, Dict
from rasa_sdk.events import SlotSet
from actions.sendMailFunction import sendOtpMail
from actions.dbFun import saveNewAppointmentData,getSingleAppointmentData,updateStatus,allDrNames
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
from  actions.timeSlots import getAvailaleSlotes
import json
class ActionAskAppointmentTime(Action):

    def name(self) -> Text:
        return "action_ask_appointment_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        appointment_date = tracker.get_slot("appointment_date")
        # print(appointment_date)
        all_available_appointment_times = json.loads(tracker.get_slot("allAvailableTimeSlots"))[appointment_date]
        # print(all_available_appointment_times)
        dispatcher.utter_message(text="Enter on which time you want to take appointment ? "+str(all_available_appointment_times))

        return []
    
class ActionAskAppointmentDate(Action):

    def name(self) -> Text:
        return "action_ask_appointment_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dr_name = tracker.get_slot("dr_name")
        timeslot,dates=getAvailaleSlotes(drId=dr_name[0:6])

        dispatcher.utter_message(text="Enter on which date you want to take appointment ? "+str(dates))
        
        return [SlotSet("allAvailableDates",dates),SlotSet("allAvailableTimeSlots",timeslot)]

class ActionAskDrName(Action):

    def name(self) -> Text:
        return "action_ask_dr_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # getting all Dr. names from database
        drNames = allDrNames()
        dispatcher.utter_message(text="Select Dr. Name "+str(drNames))
        
        return []



# generating a unique Appointment Id ->
# def generate_unique_id():
#     digit_part = ''.join(secrets.choice(string.digits) for _ in range(5))
#     char_part = ''.join(secrets.choice(string.ascii_letters) for _ in range(5))
#     unique_id = f"{digit_part}_{char_part}"
#     return unique_id


# printing got appointment


# class ActionDeactivateForm(Action):
#     def name(self) -> Text:
#         return "action_deactivate_form"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         return [SlotSet("requested_slot", None), Form(None)]

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
        dr_name = tracker.get_slot("dr_name")
        appointment_time = tracker.get_slot("appointment_time")
        appointment_date = tracker.get_slot("appointment_date")
        # print("appointment_time :  ",appointment_time)
        # print("appointment_date :  ",appointment_date)
        aid = saveNewAppointmentData(name,age,mobile_no,city,email,appointment_time,appointment_date,dr_name)
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
            SlotSet("dr_name", None),
            SlotSet("sentOTP", None),
            SlotSet("appointment_time", None),
            SlotSet("appointment_date", None),
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

        entities = tracker.latest_message.get("entities",[])
        person = ""
        for entity in entities:
            if entity["entity"] == "PERSON":
                person = entity["value"]
            elif entity["entity"] == "ORG":
                person = entity["value"]
            elif entity["entity"] == "GPE":
                person = entity["value"]
            elif entity["entity"] == "name":
                person = entity["value"]

        if person is None:
            dispatcher.utter_message(
                text=f"Name is not recognized by the me ,Plz enter it  again !")
            return {"name": None}
        
        dispatcher.utter_message(
            text=f"OK! Your entered name is {slot_value}.")
        return {"name": person}

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
        otp = sendOtpMail(slot_value)
        # otp = "123456"
        print(slot_value, otp)
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
    
    
    
    def validate_appointment_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `appointment time` value."""


        appointment_date = tracker.get_slot("appointment_date")
        
        # get all available time slots as per selected date
        all_available_appointment_times = json.loads(tracker.get_slot("allAvailableTimeSlots"))[appointment_date]
        
        if slot_value not in all_available_appointment_times:
            dispatcher.utter_message(
                text=f"Select appointment time from "+str(all_available_appointment_times))
            return {"appointment_time": None}
        else:
            dispatcher.utter_message(text=f"You selected appointment time is "+slot_value)
            return {"appointment_time": slot_value}
    
    def validate_appointment_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `appointment date` value."""
        
        # print("appointment_dates")
        appointment_dates = (tracker.get_slot("allAvailableDates"))
        # print(slot_value)
        if slot_value is None:
            dispatcher.utter_message(
                text=f"Select appointment date from "+str(appointment_dates))
            return {"appointment_date": None}
        else:
            dispatcher.utter_message(text=f"You selected appointment date is "+slot_value)
            return {"appointment_date": slot_value}

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
        dt = getSingleAppointmentData(aid=slot_value)
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
            otp = sendOtpMail(email)
            # otp="123457"
            # print(otp)
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
    
    def validate_dr_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `otp` value."""

        if slot_value is None:
            dispatcher.utter_message(text=f"Select Dr Name "+allDrNames())
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
        if getSingleAppointmentData(aid) is not None:
            if otp == sentOTP:
                updateStatus(aid,status="cancelled")
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

class ValidateStatusForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_status_form"

    def validate_checkaid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `checkaid` value."""

        # print(slot_value)

        # call API and  Print all the info about the Patient.
        dt = getSingleAppointmentData(aid=slot_value)
        if dt == None:
            dispatcher.utter_message(
                text=f"{slot_value} Invalid Appointment ID . or you have not booked the appointment !")
            return {"checkaid": None}
        else:
            email = dt["email"]
            dispatcher.utter_message(text=f"Yes Valid Appointment ID. and your email is {email}")
            return {"checkaid": slot_value}

class ResultForStatus(Action):

    def name(self) -> Text:
        return "action_status_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        aid = tracker.get_slot("checkaid")
        # print(aid)
        dt = getSingleAppointmentData(aid)
        email = dt["email"]
        name = dt["name"]
        status = dt["status"]
        aid = dt["_id"]
        dispatcher.utter_message(f"aid: {aid} ,name: {name} ,email: {email}, status: {status}")

        # reset all the slots .........
        slots = [
            SlotSet("checkaid", None)
        ]
        return slots
