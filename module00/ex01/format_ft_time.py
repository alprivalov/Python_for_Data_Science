import time

from datetime import datetime
seconds = time.time()
date_time = datetime.fromtimestamp(seconds)

print("Seconds since January 1, 1970:","{:,.4f}".format(seconds),"or","{:.2e}".format(seconds)," in scientific notation")

d = date_time.strftime("%b %d %Y")
print(d)