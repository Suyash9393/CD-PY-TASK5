# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:22:55 2024

@author: suyash morye
"""

import string
import random

if __name__ == "__main__":
    s1 =string.ascii_lowercase
    
    s2 =string.ascii_uppercase
    
    s3 =string.digits
    
    s4 =string.punctuation
    
    plen = int(input("Enter A Password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    #random.shuffle(s)
    
    print("your passwor is :")
    #print("".join(s[0:plen]))
    print("".join(random.sample(s,plen)))
    
    