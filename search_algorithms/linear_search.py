def linear_search(list,val):
    for i in range(0,len(list)):
        if list[i] == val:
            print('Your value(index) :', i)
        else:
            print('No value')
