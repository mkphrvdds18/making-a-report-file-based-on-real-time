
import time
import datetime

# below codes will only focus on how to create a file name with current time being a part of file name
# make sure to add codes to goto required working directory
# get the current time information from system

partial_time = str(datetime.datetime.now())
#print local time - for info only
print(partial_time)

logfile_name = 'Test_report_' + partial_time[0:10]+ '_' + partial_time[11:13] + partial_time[14:16]
log_file = logfile_name + '.' + 'txt'
print(log_file)

# this will create a file named as logfile in the current directory ; it is a text file
write_file = open(log_file, 'w')
write_file.close()

