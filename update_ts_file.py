import time

with open("latest_phone_home", "w") as f:
  f.write(str(int(time.time())))
