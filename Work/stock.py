class Stock:
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def cost(self):
    return self.shares * self.price

  def sell(self, sellshares):
    self.shares -= sellshares
    return self.shares
