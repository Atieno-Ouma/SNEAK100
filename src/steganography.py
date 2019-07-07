# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:02:12 2019

@author: Rishabh Chandra
"""
from PIL import Image
import rsa_encrypt as crypto

def encodePic(msg, pk, imgurl):
    N = len(str(pk[1]))
    packets = crypto.encrypt_packets(msg,pk)
    pic = Image.open(imgurl)
    w,h = pic.size
    if(h <= len(packets) or w <= N or 255< len(packets)):
        print("Select a bigger pic or reduce text size!")
        return
    if(pic.mode!='RGB'):
        print("Choose a color picture!")
        return
    newpic = pic.copy()
    packetlen = len(packets)
    R,G,B = newpic.getpixel((0,0))
    newpic.putpixel((0,0),(packetlen,G,B))
    for r in range(1,len(packets)+1):
        plen = len(packets[r-1])-2
        R,G,B = newpic.getpixel((r,0))
        newpic.putpixel((r,0),(plen,G,B))
        for c in range(1,plen+1):
            R,G,B = newpic.getpixel((r,c))
            R= (R&(240))+(int(packets[r-1][c+1],16))
            newpic.putpixel((r,c),(R,G,B))
    #newpic.show()
    #save as png always because others are lossy compression format.
    newpic.save("../secret.png")
    return newpic

def decodePic(pk,imgurl):
    pic = Image.open(imgurl)
    packets = []
    plen = pic.getpixel((0,0))[0]
    for r in range(1,plen+1):
        strlen = pic.getpixel((r,0))[0]
        temp = "0x"
        for c in range(1,strlen+1):
            R = pic.getpixel((r,c))[0]
            temp += str(hex(R&(15)))[2:]
        packets.append(temp)
        temp = ""
    return crypto.decrypt_packets(packets,pk)
