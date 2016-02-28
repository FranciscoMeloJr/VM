
print "Module 1"

f=open('../traces/output3349.txt','r')
print f
content = f.read()
#print content

#dictionary of syscalls: 
def parse_lines(sys_calls):
   "fuction to do parse syscalls lines"
   i = 0
   info = []
   content = []
   while i < 1:#len(sys_calls):
      line = sys_calls[200]
      info = line.split()
      #print info
      content.append(info[0])
      content.append(info[1])
      content.append(info[2])
      content.append(info[3])
      content.append(info[5]+info[6]+info[7])
      content.append(info[10]+info[11]+info[12])
      content.append(info[13]+info[14]+info[15])
      print content
      i+=1

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

sys_calls = read_lines()
print len(sys_calls)
print sys_calls[200]
parse_lines(sys_calls)
