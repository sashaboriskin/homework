N = int(input())
K = int(input())
petya_desk = int(input())
petya_place = int(input())

petya_index  = (petya_desk-1)*2 + (petya_place-1)
vasya_index1 = petya_index - K
vasya_index2 = petya_index + K

if vasya_index1 < 0 and vasya_index2 >= N:
  print("-1")
  exit()

if  vasya_index1 < 0:
  best_index = vasya_index2
elif vasya_index2 > K:
  best_index = vasya_index1
else:
  vasya_desk1 = (vasya_index1 / 2) + 1
  vasya_desk2 = (vasya_index2 / 2) + 1
  vasya_distance1 = petya_desk - vasya_desk1
  vasya_distance2 = vasya_desk2 - petya_desk
  if(vasya_distance1 < vasya_distance2):
    best_index = vasya_index1
  else:
    best_index = vasya_index2

vasya_desk = int(best_index/2) + 1
if best_index % 2:
  vasya_place = 2
else:
  vasya_place = 1
print(vasya_desk, vasya_place)  

