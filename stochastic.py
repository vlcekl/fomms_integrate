#!//anaconda/envs/py36/bin/python
#
# File name:   stochastic.py
# Date:        2018/07/19 15:04
# Author:      Lukas Vlcek
#
# Description: 
#

import sys
import re
import numpy as np

if __name__ == "__main__":

    with open(sys.argv[1], 'r') as f:
        for line in iter(f.readline, ''):
            sarr = re.findall('\S+', line)

# end of stochastic.py 
