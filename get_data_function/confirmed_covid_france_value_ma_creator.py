import xlrd
import numpy as np

D = dict()
D["01"] = 26
D["02"] = 28
D["03"] = 29
D["04"] = 46
D["05"] = 35
D["06"] = 38
D["07"] = 30
D["08"] = 31
D["09"] = 29
D["10"] = 27
D["11"] = 27
D["12"] = 30
D["13"] = 39
D["14"] = 31
D["15"] = 29
D["16"] = 31
D["17"] = 40
D["18"] = 27
D["19"] = 30
D["21"] = 33
D["22"] = 37
D["23"] = 29
D["24"] = 31
D["25"] = 28
D["26"] = 28
D["27"] = 27
D["28"] = 35
D["29"] = 32
D["2A"] = 35
D["2B"] = 34
D["30"] = 27
D["31"] = 36
D["32"] = 27
D["33"] = 30
D["34"] = 30
D["35"] = 38
D["36"] = 28
D["37"] = 37
D["38"] = 28
D["39"] = 27
D["40"] = 29
D["41"] = 35
D["42"] = 28
D["43"] = 34
D["44"] = 39
D["45"] = 29
D["46"] = 26
D["47"] = 37
D["48"] = 29
D["49"] = 37
D["50"] = 29
D["51"] = 28
D["52"] = 34
D["53"] = 30
D["54"] = 41
D["55"] = 28
D["56"] = 31
D["57"] = 30
D["58"] = 29
D["59"] = 27
D["60"] = 27
D["61"] = 27
D["62"] = 36
D["63"] = 34
D["64"] = 43
D["65"] = 38
D["66"] = 42
D["67"] = 31
D["68"] = 32
D["69"] = 28
D["70"] = 34
D["71"] = 37
D["72"] = 29
D["73"] = 29
D["74"] = 35
D["75"] = 28
D["76"] = 37
D["77"] = 37
D["78"] = 31
D["79"] = 34
D["80"] = 28
D["81"] = 27
D["82"] = 38
D["83"] = 26
D["84"] = 31
D["85"] = 29
D["86"] = 29
D["87"] = 35
D["88"] = 29
D["89"] = 28
D["90"] = 44
D["91"] = 30
D["92"] = 37
D["93"] = 40
D["94"] = 35
D["95"] = 34
D["971"] = 34
D["972"] = 34
D["973"] = 30
D["974"] = 31
D["975"] = 57
D["976"] = 31
D["977"] = 40
D["978"] = 36

workbook = xlrd.open_workbook('confirmed_case_france.xlsx')

SheetNameList = workbook.sheet_names()

mySheet = workbook.sheets()[0]


def get_number(line):
    index_1 = 6
    num = ""
    while line[index_1] != "t":
        num += line[index_1]
        index_1 += 1
    index_2 = D[num]
    while line[index_2] != "t":
        index_2 += 1
    if line[index_2 + 1] == " ":
        return None
    else:
        res = line[index_2 + 1:-1]
        final_res = ""
        for fig_num in range(len(res)):
            if res[fig_num] == ",":
                final_res += "."
            else:
                final_res += res[fig_num]
        return float(final_res)


def generate_list(index):
    res_list = []
    for i in range(index, index + 104):
        res_list += [get_number(str(mySheet.row(i)[0]))]
    return res_list


def generate_final_list():
    final_list = []
    for i in range(157):
        final_list += [generate_list(104 * i + 1)]
    return final_list



# print(mySheet)
# print(type(mySheet))
# print(str(mySheet.row(1)[0]))
# for i in str(mySheet.row(1)[0]):
#     print(i)
# print(str(mySheet.row(1)[0])[6:8])
# print(str(mySheet.row(1)[0])[D[str(mySheet.row(1)[0])[6:8]]])
# print(get_number(str(mySheet.row(325)[0])))
# G = generate_list(1)
# print(generate_list(1))
# for i in range(len(G)):
#     print(i, G[i])
# print("###############")
# print(str(mySheet.row(12840)[0]))
# print(get_number(str(mySheet.row(12840)[0])))
# print(type(get_number(str(mySheet.row(12840)[0]))))
# print(float(get_number(str(mySheet.row(12840)[0]))))
print(generate_final_list())