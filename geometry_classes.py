class geofigur:
    def __init__(self, base, height):
        self.height = height
        self.base = base

class trapeze(geofigur):
  def second_base(self, base2):
    self.base2 = base2
  

class triangle(geofigur):
  def paint(self):
    for i in range(self.height): 
      b = 1 + (i/self.height)*self.base 
      str = '' 
      for i in range(int(b)): 
        str = str + '*' 
      print(str)
    
class rectangle(geofigur):  
  def paint(self):
    for i in range(self.height):
      str = ''
      for i in range(self.base):
        str = str + ' ' + "*"
      print(str)


fff = triangle(4, 5)
fff.paint()

ddd = rectangle(5, 4)
ddd.paint()
