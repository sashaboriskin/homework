dfd = ''                                       
#process input arguments                       
N, M =  (int(val) for val in input().split())  
all_index = []                                 
all_words = []                                 
for j in range(M):                             
    string = input().split()                   
    all_index.append(int(string[0]) - 1)       
    all_words.append(string[1])                
                                               
#Search guessed words. Start from end          
guess_words = []                               
points = [0] * N                               
for i in reversed(range(M)):                   
    if all_words[i] in guess_words:            
        continue                               
    points[all_index[i]] += 1                  
    guess_words.append(all_words[i])           
                                               
#Print results                                 
#for i in range( M ):                          
 # print (points[i]) ,                         
                                               
for i in range(len(points)):                   
  dfd = dfd + str(points[i]) + ' '             
print(dfd)
