import timeit
import xlsxwriter
start = timeit.default_timer()

file = open("beit_hapolitica", mode="r", encoding="utf-8")
lines = file.readlines()
file.close()
datesCounter = dict({})
for line in lines:
    try:
        date = line.strip().split("[")[1].split(",")[0]
        if date.count("/") == 2:
            if datesCounter.get(date) is not None:
                datesCounter[date] += 1
            else:
                datesCounter[date] = 1
    except:
        pass

# count=0
# for value in datesCounter.values():
#     count+=value
# print(count)

dates = list(datesCounter.keys())
values = list(datesCounter.values())
f = open("result.txt", mode="w")
for i in range(len(dates)):
    f.write(str(dates[i])+":"+str(values[i])+"\n")
f.close()
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

# Iterate over the data and write it out row by row.
for i in range(len(dates)):
    item = dates[i]
    cost=values[i]
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1
workbook.close()
print(f"finished in {timeit.default_timer() - start} seconds")
exit()
