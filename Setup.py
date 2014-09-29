'DeavmiOSS Mirror Python Setup Script - GNU GPL v3.0 or above'
print("DeavmiOSS  Mirror Python Setup Script - GNU GPL v3.0 or above")
print("Making directories...")
cmd = "mkdir 64-Bit"
cmd = "mkdir 32-Bit"
def fetch_isos()
  prompt = input("Would you like to fetch the .isos now?")
  if prompt = "yes" or "Yes":
      print("Fetching files now (.isos/disk-images)...")
      print("")
      print("Fetching files now (.isos/disk-images)... [Done]")
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
