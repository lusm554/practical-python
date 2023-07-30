from typedproperty import String, Integer, Float

class Stock:
  __slots__ = ('_name', '_shares', '_price') # adding some optimization, when class used as data structure
  name = String('name')
  shares = Integer('shares')
  price = Float('price')

  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def __repr__(self):
    return f"{type(self).__name__}('{self.name}', {self.shares}, {self.price})"

  @property
  def cost(self):
    return self.shares * self.price

  def sell(self, sellshares):
    self.shares -= sellshares
    return self.shares
