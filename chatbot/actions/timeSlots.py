from datetime import datetime, timedelta
from collections import defaultdict
from actions.dbFun import getAvailablityTimesAndDays,getBookedData

class TimeArray:
    def __init__(self):
        self.formatter = "%H:%M"

    def create_time_array(self,availableTimeSlots, availableDays=[0,1,2,3,4], appointment_time=60,drId=None):
        all_time_slots = []
        
        # Convert each available time slot to a list of time intervals
        for slot in availableTimeSlots:
            all_time_slots.extend(self.time_array(appointment_time, slot[:5],slot[6:]))
        today = datetime.now().date()
        obj = defaultdict(list)
        
        # Iterate over the next 7 days
        for _ in range(7):
            today += timedelta(days=1)
            
            # Check if the current day is within the available days
            if today.weekday() in availableDays:
                dt = str(today)
                slots = []
                # Get booked data for the current day and doctor (if provided)
                bkd = [] if drId is None  else getBookedData(dt,drId)
                # print(bkd)
                if len(bkd)==0:
                    # If no booked data, add all time slots to the available slots
                    slots.extend(all_time_slots)
                else:
                    # Check each time slot and add it to the available slots if it's not booked
                    for f in all_time_slots:
                        if f not in bkd:
                            slots.append(f)
                
                # Store the available slots for the current day
                obj[dt] = slots
        
        return obj

    def time_array(self, x, start_time, end_time):
        start_time = datetime.strptime(start_time, self.formatter)
        end_time = datetime.strptime(end_time, self.formatter)
        time_stops = []
        
        # Generate time intervals based on the appointment time, start time, and end time
        while start_time <= end_time:
            tp = start_time.strftime(self.formatter)
            start_time += timedelta(minutes=x)
            tp2 = start_time.strftime(self.formatter)
            
            if start_time > end_time:
                break
            
            time_stops.append(f"{tp}-{tp2}")
        
        return time_stops


# Example usage
def getAvailaleSlotes(drId):
    # print("get avail slots")
    time_array = TimeArray()
    # TO GET AVAILABLE DAYS AND TIME DURATION OF A DOCTOR BY HIS ID
    drTimeSlots = getAvailablityTimesAndDays(drId)
    
    # Add the booked appointments dictionary
    result = time_array.create_time_array(
        appointment_time=drTimeSlots["slotDuration"],
        availableTimeSlots=drTimeSlots["times"],
        availableDays=drTimeSlots["days"],
        drId=drId
    )
    # print(result)
    dates=[]
    for i in result:
        if len(result[i])!=0:
            dates.append(i)
    return str(dict(result)).replace("'",'"'),str(dates).replace("'",'"')
