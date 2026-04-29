from datetime import datetime
import time

epoch_time = float(time.time())
print("Seconds since January 1, 1970: "
	  + ('{0:,.4f}'.format(epoch_time))
	  + " or "
	  + ('{:.2e}'.format(epoch_time))
	  + " in scientific notation")

now = datetime.now()
formatted_date = now.strftime("%b %-d, %Y")
print(formatted_date)
