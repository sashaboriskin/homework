#cur_list - current list to add values 
#recurseCount - recurrent decreasing counter - N
#prevValue - last i value from previous recursion 
#valToComp - value we need to get - K
def calc(cur_list, recurseCount, prevValue, valToComp): 
  for i in range (prevValue+1, valToComp): 
    new_list = cur_list[:]
    new_list.append(i) 

    if recurseCount > 1: 
      calc(new_list, recurseCount-1, i, valToComp) 
    else: 
      if sum(new_list) == valToComp: 
        print(new_list) 

prev_value = -1 
valToComp = 12 
recurseCount = 3 
cur_list = [] 
calc(cur_list, recurseCount, prev_value, valToComp)
