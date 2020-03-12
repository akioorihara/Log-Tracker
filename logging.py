import datetime, os, time, stat 

now = datetime.datetime.now()

#Class for print a file name  
class DisplayFileName: 
    def __init__(self, fname):
        self.fname = fname 
        print(os.path.basename(os.path.basename(fname)))

class LogToFile:
    def __init__(self, ModTime):
        self.ModTime = ModTime 
        ModTime = time.ctime(FileCreated[stat.ST_MTIME])
        f.write("Last Modified Time : " + ModTime + '\n\n')


f = open('log.txt', 'a') #open an exiting file 
f.write("Current time is : " + str(now) + "\n")

#Write a mod time of the log file
FileCreated = os.stat('log.txt')
FileName = 'log.txt'
#DisplayFileName(FileName)
#LogToFile
ModTime = time.ctime(FileCreated[stat.ST_MTIME])
f.write(str(FileCreated) + "Last Modified Time: " + str(ModTime) + '\n')

#print(f.read())
#f.write('\n')
f.close()
#logging.error('%s raised an error', output)