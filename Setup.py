'DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above'
print("DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above")
print("Making directories...")
cmd = "mkdir 64-Bit"
cmd = "mkdir 32-Bit"
def bye():
    print("Thank you for uisng this tool!")
def finished():
    print("Your mirror has been setup!")
    print("We recommend you change the 'index.html' file to your needs.")
    prompt = input("Change 'index.html' file now?: ")
    if prompt == "yes" or "Yes":
        'Credits to this page here, for helping with the cd command - <http://techie-buzz.com/foss/how-to-go-back-to-previous-directory-and-home-directory-in-linux-shell-or-putty.html>'
        cmd = "cd"
        cmd = "nano index.html"
    elif prompt == "no" or "No":
        bye()
    else:
        print("'" + prompt + "' is an invalid option, please retry!")
        finished()
def get_isos_online():
    print("Reading configuration...")
    if get_64bit == True:
        print("64-Bit ISO is 'True'!")
        print("=========================")
        print()
        print("Creating directory...")
        cmd = "mkdir 64-Bit"
        print("Creating directory... [Done]")
        print("Fetching 64-Bit Image File...")
        cmd = "cd 64-Bit"
        cmd = "wget https://my-mirror.com/Debian/Debian-64-Bit.iso"
        print("Fetching 64-Bit Image File... [Done]")
        print("Cleaning up...")
        cmd = "cd"
        print("Cleaning up... [Done]")
    else:
        print("64-Bit ISO is 'False'!")
        print("=========================")
        print()
        print("This ISO has been ignored!")
        print("Directory creation is null!")
        print("ISO download is null!")
    if get_32bit == True:
        print("32-Bit ISO is 'True'!")
        print("=========================")
        print()
        print("Creating directory...")
        cmd = "mkdir 32-Bit"
        print("Creating directory... [Done]")
        print("Fetching 32-Bit Image File...")
        cmd = "cd 32-Bit"
        cmd = "wget https://my-mirror.com/Debian/Debian-32-Bit.iso"
        print("Fetching 32-Bit Image File... [Done]")
        print("Cleaning up...")
        cmd = "cd"
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
    print("List of all isos available:")
    print()
    print("")
def fetch_isos():
  prompt = input("Would you like to fetch the .isos now?")
  if prompt = "yes" or "Yes":
      iso_directory()
      print("Fetching files now (.isos/disk-images)...")
      print("Fetching 64-Bit .iso/disk-image...")
      cmd = "cd 64-Bit"
      cmd = "wget http://mirror.com/debian-64Bit.iso"
      print("Fetching 32-Bit .iso/disk-image...")
      cmd = "cd 32-Bit"
      cmd = "wget http://mirror.com/debian-32Bit.iso"
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
      cmd = "wget https://raw.githubusercontent.com/DeavmiOSS/mirror_service/master/index.html"
      cmd = "wget https://raw.githubusercontent.com/DeavmiOSS/mirror_service/master/Status"
      cmd = "wget https://raw.githubusercontent.com/DeavmiOSS/mirror_service/master/logo.png"
      print("fetching files using Wget... [Done]")
  elif prompt == "git":
      print("Cloning Git repository...")
      cmd = "git clone https://github.com/DeavmiOSS/mirror_service.git"
      print("Cloning Git repository... [Done]")
  else:
      print("'" + prompt + "' is an invalid option, please retry!")
      getfiles_html()
  fetch_isos()
'Start the getting the files'
getfiles_html()
