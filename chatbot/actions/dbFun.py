import datetime
from pymongo import MongoClient
import ssl

# mongodb+srv://gauravteli:gauravteli@cluster0.iykzyey.mongodb.net/?retryWrites=true&w=majority
DB_URL = "mongodb://localhost:27017"
# DB_URL = "mongodb+srv://gauravteli:gauravteli@cluster0.iykzyey.mongodb.net/?retryWrites=true&w=majority"

# adding not adding the security by Secure Socket Layer
client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)


print("connected successfully")

db = client["RasaDb"]

doctors = db["doctors"]
appointments = db["appointments"]
bookedSlots = db["bookedSlots"]

def saveNewAppointmentData(name,age,mobile_no,city,email,appointment_time,appointment_date,drName):
    drId = drName[:6]
    # get the datetime to milliseconds
    aid = drId+"_AP_"+ str(int(datetime.datetime.now().timestamp() * 1000))
    doc = {
        "_id": aid,
        "name": name,
        "age": age,
        "mobile_no": mobile_no,
        "city": city,
        "email": email,
        "appointmentData":{           
            "time":appointment_time,
            "date":appointment_date,
        },
        "status": "pending",
        "bookedOn": str(datetime.datetime.today())
    }
    appointments.find_one_and_update({"_id":drId+"_AP"},{"$push":{"appointments":doc}})
    
    # Storing Booked Slotes
    addBookingtTimeToBookedSlotsCollection(date=appointment_date,timeSlot=appointment_time,drId=drId)
    return aid

def getSingleAppointmentData(aid):
    try:
        return appointments.find_one(
                {"_id": aid[:9]},
                { "appointments": { "$elemMatch": { "_id": aid } } }
            )["appointments"][0]
    except:
        return "No Record Found! Check Your aid (apppointment id)"

def updateStatus(aid, status):
    appointments.update_one(
            {"_id": aid[:9], "appointments._id": aid },
            { "$set": { "appointments.$.status": status } }    
        )

def allDrNames():
    return  str([i["_id"]+" "+i["name"] +" - specialist of "+i["specialistFor"] for i in doctors.find({})])

def addNewDr(name:str,email:str,specialistFor:str,availibilityTime:list,availibilityDays:list,slotDuration:int):
    id="dr_"+str(doctors.count_documents({})+1).zfill(3)
        
    doctors.insert_one({
        "_id":id,
        "name":name,
        "email":email,
        "specialistFor":specialistFor,
        "availibility":{
            "days":availibilityDays,
            "times":availibilityTime,
            "slotDuration":slotDuration
        }
        ,"dataUpdatedOn":str(datetime.datetime.today())
    })
    appointments.insert_one({
        "_id":id+"_AP",
        "appointments":[]
    })

def getAvailablityTimesAndDays(drId):
    try:
        drData=doctors.find_one({"_id":drId})
        return drData["availibility"]
    except:
        return "Dr. Id doesn't matched"
    
# print(getAvailablityTimesAndDays("dr_001"))
# def updateDrData(_id:str,name:str,email:str,specialistFor:str,availibilityTime:list,availibilityDays:list,slotDuration:int):
#     doctors.insert_one({
#         "_id":_id,
#         },{
#             "$set":{
#                 "name":name,
#                 "email":email,
#                 "specialistFor":specialistFor,
#                 "availibility":{
#                     "days":availibilityDays,
#                     "times":availibilityTime,
#                   "slotDuration":slotDuration
#                 },
#                 "dataUpdatedOn":str(datetime.datetime.today())
#             } 
#    })

# addNewDr(name="Dr. Sarah Johnson",email="Sarah.gmail.com",specialistFor="heart",availibilityDays=[1,3,5],availibilityTime=["07:00-10:00","15:00-18:00"],slotDuration=45)
# addNewDr(name="Dr. David Smith",email="David.gmail.com",specialistFor="dental",availibilityDays=[1,3,5],availibilityTime=["07:00-12:00","13:00-17:00"],slotDuration=30)
# addNewDr(name="Dr. Emily Williams",email="Emily.gmail.com",specialistFor="heart",availibilityDays=[1,3,5],availibilityTime=["07:00-10:00","13:00-17:00","18:00-19:00"],slotDuration=60)


# print("dr_Sarah_001_AP"[:-3])
# print(saveNewAppointmentData(  "name", "age", "mobile_no", "city", "email","appointment_time","appointment_date",   drName="Dr. Sarah Johnson - specialist of heart"))

def addBookingtTimeToBookedSlotsCollection(date,timeSlot,drId):
    qry={"_id":date}
    data=bookedSlots.find_one(qry)
    if not data:
        for x in  doctors.distinct("_id"):
            qry[x]=[]
        qry[drId]=[timeSlot]
        bookedSlots.insert_one(qry)
    else:
        update={"$push":{drId:timeSlot}}
        bookedSlots.update_one(qry,update)

def getBookedData(date,drId):
    data=bookedSlots.find_one({"_id":date})    
    return [] if data is None else data[drId]

# print(getBookedData(date="2023-06-30",drId="dr_002"))

# bkd = {'2023-06-18': ['09:00-10:00', '10:00-11:00', '11:00-12:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00']} 
# addBookingtTimeToBookedSlotsCollection('2023-06-15',"09:00-10:00",drId="dr_003")
# x=['09:00-10:00', '10:00-11:00', '11:00-12:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00']
# y=['09:00-10:00', '10:00-11:00']
# result = list(set(x) - set(y))
# print(result)