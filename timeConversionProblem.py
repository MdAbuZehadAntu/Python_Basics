# !/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):

    h=int(s[0:2]);
    str1 = list(s)
    if (str1[8] == 'A'):
        if (h == 12):
            str1[1] = '0';
            str1[0] = '0';
            str1 = str1[0:8];
            st = ''.join([str(item) for item in str1])
            return st;

        else:
            str1 = str1[0:8];
            st = ''.join([str(item) for item in str1])
            return st;

    else:


     if (h != 12):
        h = h + 12;

        str1[0] = str(int(h / 10));
        str1[1] = str(h % 10);
        str1 = str1[0:8];
        st = ''.join([str(item) for item in str1])
        return st;


     else:
      str1 = str1[0:8];
      st = ''.join([str(item) for item in str1])
      return st;

s=input();

print(timeConversion(s))
