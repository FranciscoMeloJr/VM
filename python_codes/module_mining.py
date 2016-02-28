import pandas
import matplotlib.pyplot as plt
from collections import Counter

print "Module 1"

f=open('../traces/output3349.txt','r')
print f
content = f.read()
#print content

#parse the lines in [n,[info]]
def parse_lines(sys_calls):
   i = 0
   sys_calls_divided = []
   while i < 99:#len(sys_calls):
      sys_calls_divided.append(parse_line(i,sys_calls[i]))
      i+=1
   return sys_calls_divided
      
#dictionary of syscalls: 
def parse_line(i,line):
   "fuction to do parse syscalls lines"
   info = []
   
   info = line.split()
   #print info
   content = []
   content.append(i)
   content.append(info)
   #print content
   
   return content

#find timestamp: 
def find_time(line):
   "fuction to do parse syscalls lines"
   print 'time'
   info = []
   info = line[1]
   #print info[0]
   
   return info[0]

#find timestamp: 
def find_timestamp(line):
   "fuction to do parse syscalls lines"
   print 'timestamp'
   info = []
   info = line[1]
   #print info[1]
   
   return info[1]

#find process: 
def find_process(line):
   "fuction to do parse syscalls lines"
   print 'process'
   info = line[1]
   #print info[2]
   
   return info[2]

#find syscall: 
def find_syscall(line):
   "fuction to do parse syscalls lines"
   print 'process'
   info = line[1]
   #print info
   #print info[3]
   
   return info[3]


#read the lines in the trace:
def read_lines():
   ## Open the file with read only permit
   f = open('../traces/output3349.txt')
   ## Read the first line 
   line = f.readline()

   ## If the file is not empty keep reading line one at a time
   ## till the file is empty
   dict_calls = []
   j = 0
   while line:
       line = f.readline()
       #print line
       dict_calls.insert(j,line)
       j+=1
       #print j
   f.close()
   return dict_calls

#find all the syscalls
def list_syscall(sys_calls_div):
   content = []
   i = 0
   while i < len(sys_calls_div):
      x = find_syscall(sys_calls_div[i])
      #print x
      content.append(x)
      i+=1
   return content

#find all the timestamps of certain process:
def list_syscall(sys_calls_div):
   content = []
   i = 0
   while i < len(sys_calls_div):
      x = find_syscall(sys_calls_div[i])
      #print x
      content.append(x)
      i+=1
   return content

#this function do a histogram
def histogram_process(sys_calls_list):
   #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
   letter_counts = Counter(sys_calls_list)
   df = pandas.DataFrame.from_dict(letter_counts, orient='index')
   df.plot(kind='bar')
   plt.show()

def main():
   sys_calls = read_lines()
   print len(sys_calls)
   #print sys_calls[200]
   sys_calls_div = parse_lines(sys_calls)
   #print sys_calls_div
   find_timestamp(sys_calls_div[1])
   process = find_syscall(sys_calls_div[50])
   x = list_syscall(sys_calls_div)
   histogram_process(x)
   
main()

