# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:16:41 2019

@author: Rishabh Chandra
"""
#Encoding scheme.
letter = {"A":11,"B":12,"C":13,"D":14,"E":15,"F":16,"G":17,"H":18,"I":19,"J":20,"K":21,"L":22,"M":23,"N":24,"O":25,"P":26,"Q":27,
          "R":28,"S":29,"T":30,"U":31,"V":32,"W":33,"X":34,"Y":35,"Z":36,",":37,".":38,"!":39,"?":40," ":41}
inverse_letters = {v: k for k, v in letter.items()}

#public_key = (1561969061,1346131896572399546968899739532362106256863031854576515473311686956486474621355377386123069156205647)
#private_key = (1284388089168598223238864662876880532243337461141875025004463609682040613870343996995742566094692557,1346131896572399546968899739532362106256863031854576515473311686956486474621355377386123069156205647)

#Modulo Power
def power(a, p, m) : 
    ans = 1 
    a = a % m  
    while (p > 0) : 
        if ((p & 1) == 1) : 
            ans = (ans * a) % m 
        p = p >> 1    
        a = (a * a) % m    
    return ans 

def makePackets(message,N):
    message = message.upper()
    # length of chars in each packet.
    pktChars = (N-1)//2
    # size is number of packets.
    paddingSize = pktChars - (len(message)%pktChars)
    for i in range(0,paddingSize):
        message += " "
        
    packets = []
    temp = 0
    for i in range(0,len(message)):
        if(i%pktChars==0 and i!=0):
            packets.append(temp)
            temp=0
        temp = temp*100 + int(letter[message[i]])
    if(temp!=0):
        packets.append(temp)
    return packets
    
def encrypt_packets(message,key):
    N = len(str(key[1]))
    packets = makePackets(message,N)
    ans = []
    for x in packets:
        ans.append(hex(power(x,key[0],key[1])))
    return ans


def decrypt_packets(packets, key):
    ans = []
    for x in packets:
        ans.append(power(int(x,16),key[0],key[1]))
    result = ""
    for p in ans:
        temp=""
        code = str(p)
        for s in range(0,len(code)-1,2):
            digits = int(code[s])*10 +int(code[s+1])
            temp = temp + str(inverse_letters[digits])
        result= result + temp
    return result

if __name__ == "__main__":
    N=100
    print(len(message))    
    print(len(makePackets(message,N))*N)
    print(encrypt_packets(message,public_key))    

