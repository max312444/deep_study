
# dataset
# feature, label

class MyDataset:
  def __init__(self, feature:list, label:list) -> None:
    self.feature:list = feature
    self.label:list = label
    
  def __str__(self): # 출력 용
    return f"Dataset: \nfeature: {self.feature}\
           \nlabel: {self.label}"
  
  def __getitem__(self, index:int)->tuple: # 재정의
    return self.feature[index], self.label[index]
  
  def __setitem__(self, index:int, value:tuple[list,list])->None: # 재정의
    self.feature[index] = value[0]
    self.label[index] = value[1]

  def __len__(self):
    return len(self.feature)
  
  def __iter__(self):
    for x, y in zip(self.feature, self.label):
      yield x, y
  
dataset = MyDataset([1, 2, 3], [10, 20, 30])

for x, y in dataset: # dataset.__iter()__ -> iterator.__next__()
  print("x, y: {x}, {y}")