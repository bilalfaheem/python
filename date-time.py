from datetime import datetime

now= datetime.now()
print("Today's date:", now)

dt=now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =",dt)

