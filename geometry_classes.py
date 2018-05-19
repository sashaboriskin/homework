#class geofigur:
    #def __init__(self, base, height):
        #self.height = height
        #self.base = base

class trapeze:
  def __init__(self, base, base2, height):
    self.base = base
    self.base2 = base2
    self.height = height


class triangle:
  def __init__(self, base, height):
    self.base = base
    self.height = height  

  def paint(self):
    for i in range(self.height): 
      b = 1+ (i/self.height)*self.base 
      str = '' 
      for i in range(int(b)): 
        str = str + '*' 
      print(str)
    
class rectangle:
  def __init__(self, base, height):
    self.base = base
    self.height = height
  
  def paint(self):
    for i in range(self.height):
      str = ''
      for i in range(self.base):
        str = str + ' ' + "*"
      print(str)



#fff = triangle(5, 4)
#fff.paint()

ddd = rectangle(5, 4)
ddd.paint()


'''
A = 4
B = 5

for i in range(A):
  str = ''
  for i in range(B):
    str = str + ' ' + "*"
  print(str)


A = 5 
B = 4 


for i in range(A): 
  b = 1+ (i/A)*B 
  str = '' 
  for i in range(int(b)): 
    str = str + '*' 
  print(str)  
  '''
