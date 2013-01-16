from cloud import Cloud
from Feedback import Feedback
from time import strptime, strftime, mktime
from subprocess import Popen, PIPE
import urlparse
import json
import os

# Globals
settings = None
mycloud = None

# Create a bookmark.
def create_bookmark(url):
  global settings, mycloud
  try:
    if not urlparse.urlparse(url).scheme:
       url = "http://%s" % (url)
    response = mycloud.create_bookmark(url, url)
    url = response["url"]
    name = response["name"]
    if settings["copy_to_clipboard"] is True:
      copy_to_clipboard(url)
    return "Bookmark for '%s' was created." % (name)
  except Exception as e:
    return "An error ocurred. Sorry!"
  return None
  
# Upload a file to CloudApp.
def upload_file(path, private = None):
  global settings, mycloud
  try:
    response = mycloud.upload_file(path, private)
    url = response["url"]
    name = response["name"]
    if settings["copy_to_clipboard"] is True:
      copy_to_clipboard(url)
    return "File '%s' was uploaded." % (name)
  except Exception as e:
    return "An error ocurred. Sorry!"
  return None

# Deletes a file from CloudApp.
def delete_file(href):
  global mycloud
  try:
    mycloud.delete_file(href)
    return "Item deleted."
  except Exception as e:
    return href
    return "An error ocurred. Sorry!"
  return None

# Returns the users last uploads as XML.
def xml_items(amount = 10):
  feedback = Feedback()
  myitems = items(amount)
  for item in myitems:
    feedback.add_item(item["name"], str_date(item["created_at"]), item["url"], "", "", icon_for_type(item["item_type"]))
  return feedback
  
# Returns the users last uploads as XML. This list is meant for deleting an item.
def xml_items_deletion(amount = 10):
  feedback = Feedback()
  myitems = items(amount)
  for item in myitems:
    feedback.add_item(item["name"], str_date(item["created_at"]), item["href"], "", "", icon_for_type(item["item_type"]))
  return feedback
  
# Returns the users last uploads.
def items(amount = 10):
  return mycloud.list_items(page = 1, per_page = amount)

# Returns the name of the icon for a given type
def icon_for_type(type):
  filename = "images/%s.png" % (type)
  if os.path.isfile(filename) == False:
    filename = "images/unknown.png"
  return filename
  
# Returns a date as a string
def str_date(formatted_date):
  created = strptime(formatted_date, "%Y-%m-%dT%H:%M:%SZ")
  day = (int) (strftime("%d", created))
  return "%s, %d%s of %s" % (strftime("%A", created), day, ordinal(day), strftime("%B %Y", created))

# Returns the ordinal for a day
def ordinal(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
      suffix = "th"
  else:
      suffix = ["st", "nd", "rd"][day % 10 - 1]
  return suffix
  
# Copies a string to the clipboard.
def copy_to_clipboard(string):
  script = """
  tell application "Finder"
    set the clipboard to "%s"
  end tell
  """ % (string)
  run_applescript(script)
  
# Executes an AppleScript.
def run_applescript(script):
  p = Popen(["osascript", "-"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  stdout, stderr = p.communicate(script)
  return stdout
  
# Load configurations.
def load_config():
  global settings
  settings = json.load(open("config.json"))
  
# Initial setup.
def start_your_engines():
  global settings, mycloud
  load_config()
  mycloud = Cloud()
  mycloud.auth(settings["username"], settings["password"])
  
# Ladies and gentlemen... Start your engines!
start_your_engines()

if __name__ == "__main__":
  print xml_items()