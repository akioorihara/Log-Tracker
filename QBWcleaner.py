import datetime, os, time, stat, glob
from math import log2

#currentTime = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y") # current time 
currentTime = datetime.datetime.now()
a = datetime.datetime(2020, 4, 10)

def modi_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def check_the_diff(filename):
    if(currentTime - modi_date(filename) >= currentTime-a):
        #print("This file is older than ", currentTime - modi_date(filename))
        return True
    else:  
        #print(currentTime - modi_date(filename), datetime.timedelta(hours= 1))
        return False

def take_user_input():
    
    while(True):
        year = input("Please enter the year : YYYY  ")
        if(len(year)>5 and len(year)<3)
        
    #Needs some adjustment here to validate 
    month = input("Please enter the month : MM ")
    day = input("Please enter the day : DD ")
    return year, month, day


def file_size(size):
    _suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    order = int(log2(size) / 10) if size else 0
    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])

f = open('QBCleaner.txt', 'a') #open an exiting file 

print("Please enter your cutoff date")
take_user_input()
print("Staring the progream now....\n")
time.sleep(1)


#glob to scan through files within the GitHub folder 
#pathDir = r"\\cdhfs3\Extended Storage"
pathDir = r"C:\Users\aorihara\Documents\GitHub"
for root, dirs, files in os.walk(pathDir):
    for file in files:
        if not file.startswith(".") and file.endswith(".txt") or file.endswith(".qbw") or file.endswith(".qbb"):
            x = os.path.join(root, file)
            if check_the_diff(x): #check if file is older than x date(s)
                print(x,file_size(os.stat(x).st_size))    
                
                f.write(x)  #Write it into a file 
                f.write("  | ")
                f.write(file_size(os.stat(x).st_size))
                f.write('\n')
            else:
                #print(x)
                continue

print("\n")
print("Scan Completed! Please review the log at the file called", pathDir)
f.close()  #closing a file 