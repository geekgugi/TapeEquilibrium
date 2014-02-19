#This method reverses list with O(n) complexity
def reverseList(list):
    # get the last index
    lastIndex = len(list) - 1
    # iterate through the index 
    for item in list:
        # assign last item value to temp
        temp = list[lastIndex]
        # exchange elements
        list[lastIndex] = list[list.index(item)]
        # restore the value
        list[list.index(item)] = temp
        # decrement index
        lastIndex -= 1
        if (lastIndex >= list.index(item)):
            break

    # print the reversed list
    for item in list:
        print item

# Test list 1
list1 = [1, 2, 3, 4, 5]
reverseList(list1)

# Test list 2
list2 = [72, 272, 920, 111]
reverseList(list2)

