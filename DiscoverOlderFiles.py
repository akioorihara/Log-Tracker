import datetime, os, time, stat, glob

currentTime = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y") # current time 

def modi_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def check_the_diff(filename):
    if  (modi_date(filename) - currentTime <= datetime.timedelta(hours= 1)):  
        return filename
    else: 
        print("here")
        #does not get here 
        return None


#glob to scan through files within the GitHub folder 
pathDir = r"C:\Users\aorihara\Documents\GitHub"

for root, dirs, files in os.walk(pathDir):
    for file in files:
            if not file.startswith(".") and file.endswith(".txt"):
                if check_the_diff(file) == None: #check if file is older than x date(s)
                    #Does not run till here 
                    continue
                else:
                    print(os.path.join(root, file))

