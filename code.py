# NOTE: Make sure you've created your secrets.py file before running this example
# https://learn.adafruit.com/adafruit-pyportal/internet-connect#whats-a-secrets-file-17-2
import board
from adafruit_pyportal import PyPortal

# Set a data source URL
NODE_JS_RELEASE_API_URL = "https://raw.githubusercontent.com/nodejs/Release/master/schedule.json"
JSON_PATH = ["v10", "end"]

# Create the PyPortal object
pyportal = PyPortal(url=NODE_JS_RELEASE_API_URL, json_path=JSON_PATH, status_neopixel=board.NEOPIXEL)

# Set display to show REPL
board.DISPLAY.show(None)

# Go get that data
print("Fetching data from", NODE_JS_RELEASE_API_URL)
data = pyportal.fetch()

# Print out what we got
print('-'*40)
print(data)
print('-'*40)
