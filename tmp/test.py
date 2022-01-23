from datetime import *

currenttime = datetime.now().time().strftime("%H:%M")

if currenttime >= "20:00":
    print("hoooo")
