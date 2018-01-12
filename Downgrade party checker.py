#Import modules
import urllib.request, urllib.parse
import time

#Intoduction
print("""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the downgrade party checker!
        Created by @ImNathsnTech
       Thanks to iNeal for the API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")

time.sleep(2)

#Set up environment
device = "iPhone3,1"
device1 = "iPhone5,4"
device2 = "iPhone6,2"
device3 = "iPhone8,4"

#Start program
while True:
    #Set success variable
    success = int("0")
    #Set URL for requests
    url = 'http://api.ineal.me/tss/%s/includebeta' % (device)
    #Get request from API
    request_text = urllib.request.urlopen(url)
    #Turn request into string
    returned_values = request_text.read()
    #Decode string into UTF-8
    current_firmware = returned_values.decode('utf-8')
    #Split the string to get the latest firmware
    current_signed_version = current_firmware.split('"')[31]
    if current_signed_version == "7.1.2":
        success = success + 1

    #Repeat previous
    url = 'http://api.ineal.me/tss/%s/includebeta' % (device1)
    request_text = urllib.request.urlopen(url)
    returned_values = request_text.read()
    current_firmware = returned_values.decode('utf-8')
    current_signed_version = current_firmware.split('"')[31]
    
    if current_signed_version == "10.3.3":
        success = success + 1

    if success == int("2"):
        print("TSS is fine")
    else:
        print("Downgrade party!")
