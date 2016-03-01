#import pandas
import string
from random import randint

#to plot:
import matplotlib.pyplot as plt
from collections import Counter

#for permutations:
import itertools

print "Module 1"

class MyClass:
   "Class"
   dic = {}
   trace_syscalls = []
   list_id_syscalls = []
   
   def f(self):
        print 'hello world'

   def set_dic(self, mylista):
      self.dic = mylista

   def set_mylist(self, mylista):
      self.trace_syscalls = mylista
        
   def set_list_ids(self, mylista):
      self.list_id_syscalls = mylista
   
############################     
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
   #print 'process'
   info = line[1]
   #print info[2]
   
   return info[2]

#find syscall: 
def find_syscall(line):
   "fuction to do parse syscalls lines"
   #print 'syscall'
   info = line[1]
   #print info
   print info[3]
   
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
   print 'list_syscall'
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

#this function creates a hashmap from a list
def hash_list(lista):
   #a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
   letter_counts = Counter(sys_calls_list)
   df = pandas.DataFrame.from_dict(letter_counts, orient='index')
   df.plot(kind='bar')
   plt.show()
   
#Function that  
def no_repeat_list(mylist):
   "This function do a non repetitive list"
   print 'no_repeat_list'
   newlist = []
   for i in mylist:
     if i not in newlist:
       newlist.append(i)
   #print newlist
   return newlist

#Dic function:
def make_dictionary(mylist):
   "This function creates a dictionary for each syscall"
   print 'make dictionary'
   nrl = no_repeat_list(mylist) #non repetitive syscalls
   id = 100
   dic = {} # each syscall has an id
   dic['item3'] = 3
   #print mylist
   i = 0
   while i < len(nrl):
      dic[nrl[i]] = id;
      id+=1
      i+=1

   write_file(string.translate(str(dic), None, "'"))#adding to a file
   return dic
#prediction model: based on the size of the list and the number of occurences
def do_prediction1(mylist):
   "This function will do a prediction"
   last = mylist[-1]
   x = randint(0,len(mylist)) #random number
   return mylist[x]

#this function 
def find_apperance_syscall(mylist,element):
   "This function will do a prediction"
   #last = mylist[94] #mylist[-1]
   print 'last--------------------------------'
   print element
   write_file(element)
   i = 0
   j = 0
   k = 0
   position = []
   for i in mylist:
      if i == element:
         position.append(j)
         k+=1
      j+=1
   print position
   #write_file(position)#write to file the position
   write_file(string.translate(str(position), None, "'"))
   y_association =    association(position)#write to file the association
   write_file(string.translate(str(y_association), None, "'"))
   
   return position
   
def prediction1(mylist):
   x = randint(0,len(mylist)-1) #random number
   return mylist[x]

def association(mylist):
   "This function see the association in a list"
   association_table = []
   for i in mylist:
      small_list = [i-1,i+1]
      association_table.append([i-1,i+1])
      
   print association_table
   return association_table

def test1(mylist):
   "This function do a test using the list of syscall calls"
   syscall_order = []
   for i in mylist:
      syscall_order.append(find_apperance_syscall(mylist,i))
   print "test1"
   print syscall_order
   return syscall_order


def write_file(something):
   "Thist function writes something to a file"
   f1=open('output.txt', 'a')
   f1.write(something)
   f1.write("\n")
   f1.close()

#This function translates the list from the dictionary
def translate(mylist_syscalls,dic):
      i = 0
      syscalls_ids = []
      print 'translate'
      while i < len(mylist_syscalls):
         syscalls_ids.append(dic[mylist_syscalls[i]])
         i+=1
      #show the ids [id1,id2,id3]
      print syscalls_ids
      return syscalls_ids
   
#this function divide the set in qtd [id,id,id,id,id] = [id,id] ==[id,id,id]
def combination(qtd,mylist):
   #pega de 2 em dois:
   print 'combination'
   quantity = qtd
   aux = []
   i = 0
   j = 0
   while i < len(mylist)-(len(mylist)%quantity):
      j = 0
      temp = []
      while j < quantity:
         temp.append(mylist[i+j])
         j+=1
      aux.append(temp)#([mylist[i+j])#
      i+=quantity
    
   #print aux:      
   print aux
   return aux
def count_list_frequent(mylist):
   'list frequency'
   i = 0
   list_frequency = []
   while i < len(mylist):
      list_frequency.append(frequent(mylist[i],mylist))
      i+=1
   print list_frequency
   return list_frequency

   
#this function ccounts the occasions of settings
def frequent(item, mylist):
   aux = []
   i = 0
   j = 0
   x = mylist.count(item)
   if x > 1:
      print item
   return x


#this functino uses the class:
def inv_class():
   #Class:
   dic = dicionario
   x = MyClass()
   x.f()
   x.set_dic(dic)
   x.set_mylist(x)
   x.set_list_ids(transl)

#test 2:
#This function makes combinations of subsets until 10:
def test2(transl):
   print 'test2'
   i = 1
   while i < 10:
      y_combination = combination(i,transl)
      count_list_frequent(y_combination)
      i+=1

      test3(y_combination)

#this function makes the support of an itemset
def test3(combination):
   print 'test3 with permutations'
   i  = 0
   print combination[0]
   
   x = list(itertools.permutations(combination[0]))
   print x
   
def main():
   sys_calls = read_lines()
   print len(sys_calls)
   #print sys_calls[200]
   sys_calls_div = parse_lines(sys_calls)
   #print sys_calls_div
   find_timestamp(sys_calls_div[1])
   process = find_syscall(sys_calls_div[50])
   x = list_syscall(sys_calls_div)
   dicionario = make_dictionary(x)
   #test1(x)
   #histogram_process(x)

   transl = translate(x, dicionario)
   

   test2(transl)
   return dicionario

main()
