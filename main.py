
class laptop :
    def __init__ (self ,name ):
      self.name = name 
      

    def show (self):
      print(f"this is the laptop you searched {self.name} ")
    
    def unknown (self):
      print (f"this laptop is not available")

class asus (laptop) :
    
    def __init__(self,name,color):
      super().__init__(name)
      self.color = color 

    
    def show(self):
      print(f"this is the laptop you searched {self.name} and its color is {self.color}")

    def specs (self):
      print ("""
      1)it come with most powerful processor amd ryzen mobile chip 4900 h 
      2)it is more light weight and affordable 
      3)comes with good screen
      
      """)

    def buying (self):
      print("     BUYNOW                   ADD TO CART ")

class apple (laptop):
  
  def specs (self):
    print ("""
    
    1)it comes with powerful cpu m1 
    2)it come with 4k retina display
    """)

class undefinite (laptop):
  pass

a= asus("tufgaming","silver")
a.show()
a.specs()
a.buying()
