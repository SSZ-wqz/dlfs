class Man:
  def __init__(self, name):
    self.name = name
    print("initiated")
  
  def say_hello(self):
    print("Hello, " + self.name + "!")

  def say_byebye(self):
    print("Bye, " + self.name + "!")

man = Man("Shenwei")
man.say_hello()
man.say_byebye()