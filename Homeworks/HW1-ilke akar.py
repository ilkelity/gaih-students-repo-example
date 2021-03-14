list1: list[int] = [2, 4, 6]
list2: list[int] = [1, 3, 5]

mergedlist = list2 + list1

newmergedlist = [i * 2 for i in mergedlist]

for x in newmergedlist:
    print(newmergedlist)
