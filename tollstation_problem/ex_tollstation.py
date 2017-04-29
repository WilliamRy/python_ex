# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:13:52 2016

@author: renyan
"""

import random

def points_generator(number, rangee):
    lst = range(1,rangee+1)
    random.shuffle(lst)
    f =lst[0:number-1]
    f.sort()
    result = [0] + f
    return result 

lst = points_generator(7,100)

print 'the original points and its backward are:'
print lst

def reverse(lst):
    end = lst[-1]
    result = []
    for i in range(len(lst)):
        result.append(end - lst[-i-1])
    return result
    
print reverse(lst)

def distances(lst):
    result = []
    lenn = len(lst)
    for i in range(lenn-1):
        for j in range(i+1,lenn):
            result.append(lst[j] - lst[i])
    random.shuffle(result)
    return result
    
dist = distances(lst)
dist.sort(reverse = True)

print 'the distances between these points are'    
print dist


found = False

def locate(dist):
    d = dist[:]
    result = []

    
    def position(puton, ds):
        puton.sort()
        rt = [puton[0]+ds, puton[-1] - ds]
        for i in range(1,len(puton)-1):
            if puton[i] - ds > 0:
                rt.append(puton[i]-ds)
            if puton[i] + ds < puton[-1]:
                rt.append(puton[i]+ds)
        print 'try the following positions'
        print rt        
        return rt
         

    def inloc(puton, dd):
        global found

        if dd == []:
            puton.sort()
            found = True
            result.extend(puton)
            print 'the tolls are:'
            print puton
        else:
            for i in position(puton, dd[0]):
                if found == True:
                    break
                else:
                    j = 0
                    tempd = dd[:]
                    print 'try %d'%i
                    while j < len(puton) and abs(puton[j]-i) in tempd:
                        tempd.remove(abs(puton[j]-i))
                        j += 1
                    if j == len(puton):
                        tempd.sort(reverse =True)
                        print 'the new puton is:'
                        print puton + [i]
                        print 'the removed distances set is:'
                        print tempd
                        inloc(puton + [i], tempd)
                    else:
                        print '%d is not suitable'%i
            else:
                print 'there is no way. we have to go back'
                    
    inloc([0,d[0]],d[1:])
    return result
    
print locate(dist)