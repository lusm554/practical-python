# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
  def test_create(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

  def test_cost_property(self):
    name, shares, price = 'GOOG', 100, 490.1
    s = stock.Stock(name, shares, price)
    self.assertEqual(s.cost, shares*price)

  def test_sell_method(self):
    name, shares, price = 'GOOG', 100, 490.1
    sell_shares = 50
    s = stock.Stock(name, shares, price)
    s.sell(sell_shares)
    self.assertEqual(s.shares, shares-sell_shares)

  def test_bad_shares(self):
    name, shares, price = 'GOOG', 100, 490.1
    s = stock.Stock(name, shares, price)
    with self.assertRaises(TypeError):
      s.shares = '11'

if __name__ == '__main__':
  unittest.main()
