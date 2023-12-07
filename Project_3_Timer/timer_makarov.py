import datetime
from datetime import datetime as dttm
import time as tm
def get_input_for_timer():
    while True:
        input_=input("Please, input timer value in format H24:MI:SI - ")
        try:
            input_transformed=dttm.strptime(input_, '%H:%M:%S')#transfroming to datetime
            break
        except ValueError as er:
            error_=er
            print("There is an error in your input: ",error_)
            print("Try again")
            continue
    return input_transformed
        
def timer():
    dif=1
    start_time=get_input_for_timer()
    finish_time=dttm.strptime("00:00:00", '%H:%M:%S').time()
    time_dif=datetime.timedelta(seconds=dif)
    print("We start our timer:"+str(start_time.time()))
    while start_time.time()!=finish_time:
        start_time-=time_dif
        tm.sleep(dif)#sleep for dif time
        print("Till the end is: "+str(start_time.time()))
        continue
    return print("The time is off!!!")
timer()