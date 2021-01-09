import xlrd

workbook = xlrd.open_workbook('FR_Region_Mobility_Report.xlsx')
SheetNameList = workbook.sheet_names()
mySheet = workbook.sheets()[0]

""" 
in each list : retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,
parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,
workplaces_percent_change_from_baseline,residential_percent_change_from_baseline 
"""


def get_value(line):
    comma_counter = 0
    chr_num = 0
    while comma_counter != 8:
        if line[chr_num] == ",":
            comma_counter += 1
        chr_num += 1

    num_1 = ""
    while comma_counter != 9:
        if line[chr_num] == ",":
            comma_counter += 1
        else:
            num_1 += line[chr_num]
        chr_num += 1

    num_2 = ""
    while comma_counter != 10:
        if line[chr_num] == ",":
            comma_counter += 1
        else:
            num_2 += line[chr_num]
        chr_num += 1

    num_3 = ""
    while comma_counter != 11:
        if line[chr_num] == ",":
            comma_counter += 1
        else:
            num_3 += line[chr_num]
        chr_num += 1

    num_4 = ""
    while comma_counter != 12:
        if line[chr_num] == ",":
            comma_counter += 1
        else:
            num_4 += line[chr_num]
        chr_num += 1

    num_5 = ""
    while comma_counter != 13:
        if line[chr_num] == ",":
            comma_counter += 1
        else:
            num_5 += line[chr_num]
        chr_num += 1

    num_6 = ""
    while chr_num < len(line) - 1:
        num_6 += line[chr_num]
        chr_num += 1

    if num_1 != "":
        num_1 = int(num_1)
    else:
        num_1 = None

    if num_2 != "":
        num_2 = int(num_2)
    else:
        num_2 = None

    if num_3 != "":
        num_3 = int(num_3)
    else:
        num_3 = None

    if num_4 != "":
        num_4 = int(num_4)
    else:
        num_4 = None

    if num_5 != "":
        num_5 = int(num_5)
    else:
        num_5 = None

    if num_6 != "":
        num_6 = int(num_6)
    else:
        num_6 = None

    return [num_1, num_2, num_3, num_4, num_5, num_6]


def get_gmr_matrix(beginning):
    res_list = []
    for l in range(beginning, beginning + 284):
        res_list += [get_value(str(mySheet.row(l)[0]))]
    return res_list


# start value must be chosen depending on the department from which you want to extract the data #
start = 30946  # here we extract data concerning the Vaucluse

print(get_gmr_matrix(30946))
