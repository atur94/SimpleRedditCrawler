count = 0
import sys
def wait_message(status_code):
    message = "\rWaiting for correct response"
    global count
    if count == (1):
        print(message + ".\t" + " status code = " + status_code,end="")

    if count == (2):
        print(message + "..\t" + " status code = " + status_code,end="")
    if count == (3):
        print(message + "...\t" + " status code = " + status_code, end="")
    count += 1
    if count == 4:
        count = 1


