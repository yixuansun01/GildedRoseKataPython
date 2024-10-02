# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
    # Add three unit test
    def test_aged_brie(self):
        items = [Item("Aged Brie", 10, 25)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 26)

        items[0].sell_in = 0
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 27)

    def test_sulfuras(self):
        items = [Item("Sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)
        items[0].sell_in = -5
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -5)
        self.assertEqual(items[0].quality, 80)

    def test_conjured_item(self):
        items = [Item("Conjured Mana Bread", 3, 6)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 2)
        self.assertEqual(items[0].quality, 4)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 2)


if __name__ == '__main__':
    unittest.main()
   
