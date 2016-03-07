from random import randint
import numpy as np
from scipy.io.wavfile import write

max = 1000

#This function generate randomnumbers
def generate_numbers():
    return randint(0, max)

#This function creates the syscall list
def lista(index):
    a = ['system_call1', 'system_call2', 'system_call3', 'system_call4']
    return a[(index) % len(a)]

#This function generates the syscall:
def do_list_syscalls():
    temp = []
    i = 0
    while i < max:
        x = generate_numbers()
        s = lista(x)
        temp.append(s)
        i+=1
        
    #print temp
    return temp

#Reads the system calls to a list
def read_list(mylist):
    i = 0
    j = 0
    new_list = []
    while i < len(mylist):
        if mylist[i] == 'system_call1':
            new_list.append(1)
        if mylist[i] == 'system_call2':
            new_list.append(2)
        if mylist[i] == 'system_call3':
            new_list.append(3)
        if mylist[i] == 'system_call4':
            new_list.append(4)
        i+=1
        j+=1
    return new_list
#Reads the system calls to a list
def change_list(mylist):
    i = 0
    n_list = []
    while i < len(mylist):
        n_list.append((mylist[i]*32767)/4)
        i+=1
    return n_list

#recording in a wave:
def do_wave(data_1):

    data = np.array(data_1) #data = np.array(data_1, dtype=np.int16)#np.random.uniform(-10,10,44100) # 44100 random samples between -1 and 1
    
    scaled = np.int16(data/np.max(data) * 32767)
    #scaled = data
    print scaled

    write('data.wav', max, scaled)

    print 'fim'

#Main:
def main():
    lista = do_list_syscalls()
    data =  read_list(lista)
    n_data = change_list(data)
    do_wave(n_data)
    
main()
