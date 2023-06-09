from datetime import datetime, timedelta
from collections import defaultdict


class TimeArray:
    def __init__(self):
        self.formatter = "%H:%M"

    def create_time_array(self, appointment_time, serv_start_time, serv_end_time, break_start_time, break_end_time, bkd):
        all_time_slots = []
        all_time_slots.extend(self.time_array(appointment_time, serv_start_time, break_start_time))
        all_time_slots.extend(self.time_array(appointment_time, break_end_time, serv_end_time))

        today = datetime.now().date()
        obj = defaultdict(list)
        for _ in range(7):
            today += timedelta(days=1)
            dt = str(today)
            slots = []
            if dt not in bkd:
                slots.extend(all_time_slots)
            else:
                for f in all_time_slots:
                    if f not in bkd[dt]:
                        slots.append(f)
            obj[dt] = slots
        return obj

    def time_array(self, x, start_time, end_time):
        start_time = datetime.strptime(start_time, self.formatter)
        end_time = datetime.strptime(end_time, self.formatter)
        time_stops = []
        while start_time <= end_time:
            tp = start_time.strftime(self.formatter)
            start_time += timedelta(minutes=x)
            tp2 = start_time.strftime(self.formatter)
            if start_time > end_time:
                break
            time_stops.append(f"{tp}-{tp2}")
        return time_stops


# Example usage
time_array = TimeArray()
bkd = {'2023-06-14': ['09:00-10:00']}  # Add the booked appointments dictionary
result = time_array.create_time_array(
    appointment_time=60,
    serv_start_time="09:00",
    break_start_time="12:00",
    break_end_time="13:00",
    serv_end_time="18:00",
    bkd=bkd
)
print(result)
