def merge_lists(list1, list2):
    list3 = list1 + list2
    n = len(list3)
    i = 0
    a = 0
    b = 0
    while i<n:
        if a >= len(list1):
            list3[i] = list2[b]
            b+=1
        elif b >= len(list2):
            list3[i] = list1[a]
            a+=1
        elif list1[a] < list2[b]:
            list3[i] = list1[a]
            a+=1
        else:
            list3[i] = list2[b]
            b+=1
        i+=1
    print list3




list1 = [3, 4, 6, 10, 11, 15]
list2 = [1, 5, 8, 12, 14, 19]
print merge_lists(list1, list2)