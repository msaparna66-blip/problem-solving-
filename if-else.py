#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
  
    svg = int(input().strip())

if svg % 2 != 0:
    print("Weird")
elif 2 <= svg <= 5:
    print("Not Weird")
elif 6 <= svg <= 20:
    print("Weird")
elif svg > 20:
    print("Not Weird")
