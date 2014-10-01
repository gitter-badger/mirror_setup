'DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above'

import os

class Configuration():

    default_text_editor = "nano"

config = Configuration()

print("DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above")
def bye():

    print("\nYour mirror has been setup!\n")
    print("Thank you for using this tool!\n")
    exit()

def update_status():

    prompt = input("\nChange the 'Status' file to display True records? (Y/n): ")
    if prompt == "yes" or "Yes":
        'Credits to this page here, for helping with the cd command - <http://techie-buzz.com/foss/how-to-go-back-to-previous-directory-and-home-directory-in-linux-shell-or-putty.html>'
        os.system("cd")
        os.system(config.default_text_editor + " Status")
        bye()
    elif prompt == "no" or "No":
        print("'Status' will not be changed. [Skipped]")
        bye()
    else:
        print("'" + prompt + "' is an invalid option, please retry!")
        update_status()

def update_html():

    print("We recommend you change the 'index.html' file to your needs.")
    prompt = input("Change 'index.html' file now?: ")
    if prompt == "yes" or "Yes":
        'Credits to this page here, for helping with the cd command - <http://techie-buzz.com/foss/how-to-go-back-to-previous-directory-and-home-directory-in-linux-shell-or-putty.html>'
        os.system("cd")
        os.system(config.default_text_editor + " index.html")
        update_status()
    elif prompt == "no" or "No":
        print("'index.html' will not be changed. [Skipped]")
        update_status()
    else:
        print("'" + prompt + "' is an invalid option, please retry!")
        update_html()

def get_images():

    print("Reading configuration...")
    if iso_64bit == True:
        print("64-Bit ISO is 'True'!")
        print("=========================")
        print()
        print("Creating directory...")
        os.system("mkdir 64-Bit")
        print("Creating directory... [Done]")
        print("Fetching 64-Bit Image File...")
        os.system("cd 64-Bit")
        os.system("wget https://my-mirror.com/Debian/Debian-64-Bit.iso")
        print("Fetching 64-Bit Image File... [Done]")
        print("Cleaning up...")
        os.system("cd")
        print("Cleaning up... [Done]")
    else:
        print("64-Bit ISO is 'False'!")
        print("=========================")
        print()
        print("This ISO has been ignored!")
        print("Directory creation is null!")
        print("ISO download is null!")
    if iso_32bit == True:
        print("32-Bit ISO is 'True'!")
        print("=========================")
        print()
        print("Creating directory...")
        os.system("mkdir 32-Bit")
        print("Creating directory... [Done]")
        print("Fetching 32-Bit Image File...")
        os.system("cd 32-Bit")
        os.system("wget https://my-mirror.com/Debian/Debian-32-Bit.iso")
        print("Fetching 32-Bit Image File... [Done]")
        print("Cleaning up...")
        os.system("cd")
        print("Cleaning up... [Done]")
    else:
        print("32-Bit ISO is 'False'!")
        print("=========================")
        print()
        print("This ISO has been ignored!")
        print("Directory creation is null!")
        print("ISO download is null!")
finished()

def iso_directory():

    print("List of all isos available:\n")
    print("1. 64-Bit")
    print("2. 32-Bit\n")
    print("Type 'done' when you are done adding the iso image files.\n")
    choose_iso = input("Which of the following would you like to have in your mirror?: ")
    if choose_iso == "1":
        iso_64Bit = True
        iso_directory()
    elif choose_iso == "2":
        iso_32Bit = True
        iso_directory()
    elif choose_iso == "Done" or "done":
        get_images
    else:
        print("'" + prompt + "' is an invalid option, please retry!")
        iso_directory()

def fetch_isos():

  prompt = input("Would you like to fetch the .isos now?")
  if prompt = "yes" or "Yes":
      iso_directory()
      print("Fetching files now (.isos/disk-images)...")
      print("Fetching 64-Bit .iso/disk-image...")
      os.system("cd 64-Bit")
      os.system("wget http://mirror.com/debian-64Bit.iso")
      print("Fetching 32-Bit .iso/disk-image...")
      os.system("cd 32-Bit")
      os.system("wget http://mirror.com/debian-32Bit.iso")
      print("Fetching files now (.isos/disk-images)... [Done]")
  if prompt == "no" or "No"
      print(".isos/disk-images won't be fetched!")
      finished()
  else:
      print("'" + prompt + "' is an invalid option, please retry!")
      fetch_isos()
def getfiles_html():
  prompt = input("Use Wget or Git for fetching files?")
  if prompt == "wget":
      print("fetching files using Wget...")
      os.system("wget https://raw.githubusercontent.com/DeavmiOSS/mirror_service/master/index.html")
      os.system("wget https://raw.githubusercontent.com/DeavmiOSS/mirror_service/master/Status")
      os.system("wget https://raw.githubusercontent.com/DeavmiOSS/mirror_service/master/logo.png")
      print("fetching files using Wget... [Done]")
  elif prompt == "git":
      print("Cloning Git repository...")
      os.system("git clone https://github.com/DeavmiOSS/mirror_service.git \")
      print("Cloning Git repository... [Done]")
  else:
      print("'" + prompt + "' is an invalid option, please retry!")
      getfiles_html()
      fetch_isos()

def app_start():

    prompt = input("Setup miror now? (Y/n): ")
    if prompt == "Y" or "y":
        getfiles_html()
    elif prompt == "N" or "n":
        bye()
    else:
        print("'" + prompt + "' is an invalid option, please retry!")
        app_start()

'Start the application'
app_start()