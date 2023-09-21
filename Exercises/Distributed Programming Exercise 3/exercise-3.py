# Calculate current Date time by python

from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%H:%M:%S")

print(formatted_now)