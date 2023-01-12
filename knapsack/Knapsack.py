def input_numeric( meesage):
    while True:
        try:
            n = int(input(meesage))
            return n 
        except: 
            print('Enter Numeric Number\n')
           
def back():
    print("""
    1- enter items properties manually(item name, item weight, item value)

    2- use default items (hard coded) (default_items = [('i1', 5, 50), ('i2', 10, 60) ,('i3', 20, 140)])
    """)
    choose = input_numeric('enter Your choose\n')
    if choose == 1:
            items_numbers = input_numeric('Enter num of items\n')
            
            for  i in range(items_numbers):
                name   =  input_numeric('Enter name of item\n')
                weight =  input_numeric('Enter weight of item\n')
                value  =  input_numeric('Enter value of item\n')
    
                items.append((name, weight, value))
           
    elif choose == 2:
            items = [('i1', 5, 50), ('i2', 10, 60) ,('i3', 20, 140)]
          
    else:
            print('enter avalid choose\n')
    return items

def minimum_weight(items):
    items = sorted(items, key=lambda x: x[1])
    return items

def maximum_weight(items):
    items = sorted(items, key=lambda x: x[1], reverse= True)
    return items
def maximum_value(items):
    items = sorted(items, key=lambda x: x[2], reverse= True)
    return items
def maximum_ratiovalue(items):
    items = sorted(items, key=lambda x: x[2]/x[1], reverse= True)
    return items

def Knapasck(items, max_weirght):
    remain = max_weirght
    result =0
    result_items =[]
    for i  in range (len(items)):
            if remain >  0:
                if remain-items[i][1] >=0:
                    remain-=items[i][1]
                    result+= items[i][2]
                    result_items.append(items[i])
                else:
                    result+= (items[i][2]/(items[i][1]))*remain
                    edit_val = (items[i][0],remain, (items[i][2]/(items[i][1]))*remain)
                    result_items.append(edit_val)
                    remain = 0
                    break
            else:
                break
    return result, result_items
            

items = back()

while True:
    result = 0
    result_items =[]
    max_weirght =0
   
    print("""
        1-minimum weight
        2-maximum weight
        3-maximum value
        4-maximum value/weight
        5-back """)
    choose = input_numeric('enter Your choose\n')
    if (choose ==1):
        items= minimum_weight(items)
        result, result_items =Knapasck(items, max_weirght)
        print(result, result_items)
    elif (choose ==2):
        items= maximum_weight(items)
        
    elif (choose == 3):
        items = maximum_value(items)

    elif (choose == 4):
        items= maximum_ratiovalue(items)
    elif (choose == 5):
        items = back()

    else:
        print('Enter avalid\n')
    max_weirght = input_numeric('enter max weight\n')
    result, result_items =Knapasck(items, max_weirght)
    print(f'Knapsack Weight is {max_weirght}, and Knapsack Value is {result}')
    print('\nKnapsack Items are', result_items)