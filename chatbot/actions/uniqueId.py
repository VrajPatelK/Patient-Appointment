import time
def unique_aid():
    def get_ist_datetime():
        current_time = time.time()
        ist_time = time.localtime(current_time )#+ (ist_offset * 3600))
        return ist_time

    # Usage example
    current_datetime = get_ist_datetime()
    formatted_date = time.strftime("%d-%m-%y", current_datetime)
    formatted_time = time.strftime("%H:%M:%S", current_datetime)

    return "HOS_AID_"+(formatted_date.replace("-","")+formatted_time.replace(":",""))

