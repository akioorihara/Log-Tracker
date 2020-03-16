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


def convert(file_size):
    size = file_size/1024/1024
    print(size)    

f = open('log.txt', 'a') #open an exiting file 

#Write a current time 
#f.write("Current time is : " + str(now) + "\n") 

#Write a mod time of the log file
FileCreated = os.stat('log.txt')
FileName = 'log.txt'
#DisplayFileName(FileName)
#LogToFile
ModTime = time.ctime(FileCreated[stat.ST_MTIME])

#f.write("Last Modified Time: " + (ModTime) + '\n' + "Path: " + os.path.realpath(__file__))
#print("Current File Path: ", os.path.realpath(__file__))
basepath = "."
for entry in os.scandir(basepath):
    if not entry.name.startswith('.') and entry.is_file(): 
        #Check if oder than 7 years  
        print(entry.name)
        convert(os.path.getsize(entry.name))
        #print(os.path.getsize(entry.name))
        #I need to print a file size  

    

#print(f.read())
#f.write('\n')
#f.close()
#logging.error('%s raised an error', output)
