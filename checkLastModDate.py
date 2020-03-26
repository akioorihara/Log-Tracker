import datetime, os, time, stat, glob


#Write a mod time of the log file
fileCreated = os.stat('log.txt')
#ModTime = time.ctime(FileCreated[stat.ST_MTIME])

#current time 
currentTime = time.ctime()
today = datetime.datetime.today()
file_mod_time = os.stat('log.txt').st_mtime
print(time.ctime(os.path.getmtime('log.txt')))

d = datetime.datetime.today() - datetime.timedelta(hours=8760)
#diff = today - file_mod_time

print(today)
print(d)


#glob to scan through files within the GitHub folder 
pathDir = r"C:\Users\aorihara\Documents\GitHub"

for root, dirs, files in os.walk(pathDir):
    for file in files:
            if not file.startswith(".") and file.endswith(".txt"):
                #check if file is older than x date(s)
                #lastModTime = time.ctime(file)
                
                print(os.path.join(root, file))

