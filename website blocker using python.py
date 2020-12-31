# Import libraries
import time
from datetime import datetime

# Path  to the host file, redirect to local host, list of websites to block
host_path = r"C:\Windows\System32\drivers\etc\hosts" #r is for raw string
redirect = "127.0.0.1"
websites = ["www.facebook.com", "https://www.facebook.com/", "facebook.com",  "www.instagram.com", "https://www.instagram.com/", "instagram.com", "https://www.youtube.com/", "youtube.com", "www.youtube.com"] # Users can modify the list of websites they want to block

#start_date = datetime(YYYY,MM,DD)
#end_date = datetime(YYYY,MM,DD)
#today_date = datetime(datetime.now().year,datetime.now.month,datetime.now().day)

while True:
    
    #if start_date <= today_date < end_date:
    
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,8) < datetime.now() < datetime(datetime.now().year,datetime.now().month,datetime.now().day,16):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+website+"\n")
        print("The required websites are blocked")
        break

    
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0) # reset the pointer to the top of the text file 
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

        print("The websites are unblocked! Now you are free to surf")
        break

