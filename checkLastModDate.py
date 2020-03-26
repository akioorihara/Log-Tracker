import datetime, os, time, stat, glob


#Write a mod time of the log file
fileCreated = os.stat('log.txt')
#ModTime = time.ctime(FileCreated[stat.ST_MTIME])

#current time 
currentTime = time.ctime()
now = datetime.datetime.now()
file_mod_time = os.stat(fileCreated).st_mtime
diff = now - file_mod_time

print(now)
print(currentTime)
print(file_mod_time)
print(diff)


#glob to scan through files within the GitHub folder 
pathDir = r"C:\Users\aorihara\Documents\GitHub"

for root, dirs, files in os.walk(pathDir):
    for file in files:
            if not file.startswith(".") and file.endswith(".txt"):
                #check if file is older than x date(s)
                #lastModTime = time.ctime(file)
                print(os.path.join(root, file))

