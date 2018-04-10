all_words = []                     
                                   
for i in range(len(str)):          
  str2 = str[i:len(str)]           
  all_words.append(str2)           
  for j in range(1,len(str2)):     
    str3 = str2[:-j]               
    all_words.append(str3)         
                                   
                                   
for c in  (set(str) ):             
  count = 0                        
  for  word  in all_words:         
    count += word.count(c)         
  print(c, count)
