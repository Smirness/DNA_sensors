import re
import sys

def tc2n(text):
    """transformation text concentration to number. Transform to molarity"""
    dict = {
     'M': 1,
     'mM': 1e-3,
     'uM': 1e-6,
     'nM': 1e-9,
    }

    ## Using regular expression
    # pat_num = '\d+[\.\,]*\d*'
    # pat_unit = '[a-zA-Z]+'
    #
    # num = re.findall(pat_num, text)
    # num = int(num[0])
    # unit = re.findall(pat_unit, text)
    # unit = unit[0]

    # fast way
    num, unit = text.split(' ')
    num = float(num)

    unit = dict[unit]
    num = num * unit

    return num


def tt2n(text):
    """transformation text time to number. Transform to hours"""
    dict = {
     'h': 1,
     'm': 60,
     's': 3600,
    }

    ## Using regular expression
    # pat_num = '\d+[\.\,]*\d*'
    # pat_unit = '[a-zA-Z]+'
    #
    # num = re.findall(pat_num, text)
    # num = int(num[0])
    # unit = re.findall(pat_unit, text)
    # unit = unit[0]

    # fast way
    num, unit = text.split(' ')
    num = float(num)

    unit = dict[unit]
    num = num / unit

    return num

# print(tc2n('10 nM'))
# print(tt2n('50 m'))
