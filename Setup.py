'DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above'
print("DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above")
print("Making directories...")
cmd = "mkdir 64-Bit"
cmd = "mkdir 32-Bit"
def finished():
    print("Your mirror has been setup!")
def fetch_isos()
  prompt = input("Would you like to fetch the .isos now?")
  if prompt = "yes" or "Yes":
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
