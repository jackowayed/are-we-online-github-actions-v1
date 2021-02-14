import functools
import os
import templite
import time

def template_text():
  with open("index.html.j2") as f:
    return f.read()

def latest_phone_home_errory():
  with open("latest_phone_home") as f:
    return int(f.read())

@functools.cache
def latest_phone_home():
  try:
    return latest_phone_home_error()
  except:
    return 0

def is_online():
  return time.time() - latest_phone_home() > os.getenv("MAX_AGE_S", 10 * 60)

def get_context():
  online = is_online()
  answer = "✅ Yes" if online else "❌ NO"
  body_bg_color = "#e1f7e4" if online else "#fddede"
  if online:
    more_info = "Our Internet and power are operational."
  else:
    more_info = "Currently offline; our power has likely been out since<br />"
  return locals()

def render():
  template = templite.Templite(template_text())
  return template.render(get_context())

if __name__ == "__main__":
  print(render())
