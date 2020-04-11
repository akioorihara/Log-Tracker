import datetime, os, time, stat, glob

today = datetime.datetime.today()

#Write a mod time of the log file
fileCreated = os.stat('log.txt')

#current time 
currentTime = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")

#file_mod_time = os.stat('log.txt').st_mtime
#print(time.ctime(os.path.getmtime('log.txt')))

def modi_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


if (t - currentTime) <= datetime.timedelta(hours= 1):
    print("This is older than an hour")
else:
    print("Error! ")


#t = (time.ctime(os.path.getmtime('log.txt')))  #This is last modified date 

d = datetime.datetime.today() - datetime.timedelta(hours=8760) #diff a year 
#compare the differece 
#diff = currentTime - file_mod_time

#print(currentTime)
#print(d)


#glob to scan through files within the GitHub folder 
pathDir = r"C:\Users\aorihara\Documents\GitHub"

for root, dirs, files in os.walk(pathDir):
    for file in files:
            if not file.startswith(".") and file.endswith(".txt"):
                #check if file is older than x date(s)
                #lastModTime = time.ctime(file)
                
                print(os.path.join(root, file))

