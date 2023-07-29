class Stock:
  __slots__ = ('name', '_shares', 'price') # adding some optimization, when class used as data structure
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def __repr__(self):
    return f"{type(self).__name__}('{self.name}', {self.shares}, {self.price})"

  @property
  def cost(self):
    return self.shares * self.price

  @property
  def shares(self):
    return self._shares

  @shares.setter
  def shares(self, value):
    if not isinstance(value, int):
      raise TypeError('expected an integer')
    self._shares = value

  def sell(self, sellshares):
    self.shares -= sellshares
    return self.shares
