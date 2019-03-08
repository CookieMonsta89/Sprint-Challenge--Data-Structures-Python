class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #run callback on self
    cb(self.value)

    #if there is left value on self
    if self.left:
      #recurse function on left and pass in the callback
      self.left.depth_first_for_each(cb)
    #if there is a right value on self
    if self.right:
      #recurse function on right and pass in the callback
      self.right.depth_first_for_each(cb) 

  def breadth_first_for_each(self, cb):
    #this creates a queue that starts at itself.
    queue = [self]
    #this will run as long as length of queue exists
    while len(queue):
      #removes the first element and saves to a variable
      current = queue.pop(0)
      #if current has left child, append left child
      if current.left:
        queue.append(current.left)
      #if current has right child, append right child
      if current.right:
        queue.append(current.right)
      cb(current.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
