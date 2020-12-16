import numpy as np
from data import *

def cleaning_str(chain):
    new_chain = ""
    index = 0
    while index < len(chain):
        if chain[index] == "[":
            index += 3
        else:
            new_chain += chain[index]
            index += 1
    return new_chain


def str_to_list():
    chain = str(input("List : "))
    chain = cleaning_str(chain)
    res_list = []
    for chr_number in range(len(chain)):
        nbr = chain[chr_number]
        if (nbr != " "):
            if len(chain) - 1 == chr_number:
                prev = chr_number - 1
                while chain[prev] != " ":
                    nbr = chain[prev] + nbr
                    prev -= 1
                res_list += [int(nbr)]
            elif chain[chr_number + 1] == " ":
                prev = chr_number - 1
                while chain[prev] != " ":
                    nbr = chain[prev] + nbr
                    prev -= 1
                res_list += [int(nbr)]
    return res_list



# for i in range(150):
#     B = str_to_list()
# print("   Check   ")
# print(B)
# print(len(B))
# print(len(big_list))

# print(time_list)
# print(len(time_list))
# print(departments_list)
# print(big_list)
# print(len(departments_list))
# print(len(big_list[0]))