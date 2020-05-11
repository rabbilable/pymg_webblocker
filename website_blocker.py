import time
import datetime
from datetime import datetime as dt


hosts_tmp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com",
                 "youtube.com", "www.youtube.com"]

nw = dt.now()
d = dt.now().day
m = dt.now().month
y = dt.now().year


while True:
    if dt(y, m, d, 8) < nw < dt(y, m, d, 18):
        print("working hour")
        with open(hosts_tmp, 'r+') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
            # print(content)
    else:
        with open(hosts_tmp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
        print("fun hours")
    time.sleep(5)
