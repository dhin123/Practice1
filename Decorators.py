def cale(date):
    lst = date.split("-")
    year = lst[0]
    month = lst[1]
    date = lst[2]
    total = int(date)
    i = 1
    #print(year)
    if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
        cal1 = {"jan" : 31, "feb": 29, "mar": 31, "apr":30, "may":31, "jun":30, "jul":31, "aug":31, "sep":30, "octo":31, "nov": 30, "dec":31}
    else:
        cal1 = {"jan" : 31, "feb": 28, "mar": 31, "apr":30, "may":31, "jun":30, "jul":31, "aug":31, "sep":30, "octo":31, "nov": 30, "dec":31}
    dic_val = list(cal1.values())
    print(dic_val)
    while i < int(month):
        #for i in range(1,len(cal1.values())):
        total += dic_val[i-1]
        i += 1
    return total


date = "2004-03-01"
print(cale(date))