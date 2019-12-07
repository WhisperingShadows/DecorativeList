class DecorativeList(list):
  def __call__(self, obj):
     self.append(obj)

l = DecorativeList()

@l
def print_test():
  print("Test !")

l[0]()
