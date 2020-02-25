import datetime, os, time, stat 

now = datetime.datetime.now()

f = open('log.txt', 'a') #open an exiting file 
f.write("Current time is : " + str(now) + "\n")



#Write a mod time of the log file
FileCreated = os.stat('log.txt')
ModTime = time.ctime(FileCreated[stat.ST_MTIME])
f.write(FileCreated + "Last Modified Time: " + ModTime + '\n\n')

#print(f.read())


#print a file name func 



f.write('\n')
f.close()




#logging.error('%s raised an error', output)