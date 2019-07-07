# -*- coding: utf-8 -*-
"""
Generate Key

Created on Sat Jun 29 15:51:41 2019

@author: Rishabh Chandra
"""
import time

#Take 50 digit prime always.
P = 22953686867719691230002707821868552601124472329079
Q = 58645563317564309847334478714939069495243200674793

def gcd(a,b):
    while(b!=0):
        a,b = b,a%b
    return a
        
def inverseModulo(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x 

def ETF(p,q):
    return (p-1)*(q-1)

def generatePair(p=P,q=Q):
    start = int(time.time())
    phi = ETF(p,q)
    if(start >= phi):
        print("Invalid seed.")
        return -1

    while(gcd(start,phi)!=1):
        start +=1
    return ((start),(inverseModulo(start,phi)),(p*q))
