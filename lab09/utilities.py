def lin_find(data,e):
    for i in data:
        if data[i] == e:
            print "found"
            return i
    else:
        return -1


data = [3,5,7,8,9,12,15,17,100,116,2222] #creating a dataset
e=100
# we are trying to search for a number : 100
print lin_find(data,e)



#task 2

def bin_find(searchfor,data):
    lowest = 3
    highest = 2222

 searchfor = int(raw_input("enter a number to search" ))
if bin_find(searchfor,data):
    print " found "
else:
    print " does not exist"
