import unittest
from gilded_rose import GildedRose, Item

class GildRoseUnitTest(unittest.TestCase):


    def updater(obj = GildedRose, times = 1):
        for _ in range(times):
            obj.update_quality()

    def test_normal_item(self):

        test_item = Item("+5 Dexterity Vest", 10, 20)
        gilded_rose_shop= GildedRose([test_item])

        # Test after one day, normal items lose 1 quality each day
        gilded_rose_shop.update_quality()
        self.assertEqual(test_item.sell_in, 9)
        self.assertEqual(test_item.quality, 19)


        # After sell date
        GildRoseUnitTest.updater(gilded_rose_shop, test_item.sell_in + 1)
        self.assertEqual(test_item.sell_in, -1)
        self.assertEqual(test_item.quality, 8) # quality should drop twice as fast

        # Go 10 days forward, quality can’t go below zero
        GildRoseUnitTest.updater(gilded_rose_shop, 10)
        self.assertEqual(test_item.sell_in, -11)
        self.assertEqual(test_item.quality, 0)

    
    def test_aged_bire(self):
        test_item = Item("Aged Brie", 2, 0)
        gilded_rose_shop = GildedRose([test_item])

        # Test after one day
        gilded_rose_shop.update_quality()
        self.assertEqual(test_item.sell_in, 1)
        self.assertEqual(test_item.quality, 1)


        # After sell date, it improves twice as fast
        GildRoseUnitTest.updater(gilded_rose_shop, test_item.sell_in + 1)
        self.assertEqual(test_item.sell_in, -1)
        self.assertEqual(test_item.quality, 4)

        # Never go above 50
        GildRoseUnitTest.updater(gilded_rose_shop, 10)
        self.assertEqual(test_item.sell_in, -11)
        self.assertLessEqual(test_item.quality, 50)
    

    def test_backstage_passes(self):

        test_item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        gilded_rose_shop = GildedRose([test_item])

        # Early days, just normal +1
        gilded_rose_shop.update_quality()
        self.assertEqual(test_item.sell_in, 14)
        self.assertEqual(test_item.quality, 21)


        # Still more than 10 days out
        GildRoseUnitTest.updater(gilded_rose_shop, 4)
        self.assertEqual(test_item.sell_in, 10)
        self.assertEqual(test_item.quality, 25)

        # Within 10 days, increase quality by 2
        GildRoseUnitTest.updater(gilded_rose_shop)
        self.assertEqual(test_item.sell_in, 9)
        self.assertEqual(test_item.quality, 27)

        # Within 6–10 days
        GildRoseUnitTest.updater(gilded_rose_shop, 4)
        self.assertEqual(test_item.sell_in, 5)
        self.assertEqual(test_item.quality, 35)
        #  Within 1–5 days, increase quality by 3
        GildRoseUnitTest.updater(gilded_rose_shop)
        self.assertEqual(test_item.sell_in, 4)
        self.assertEqual(test_item.quality, 38)


        # Getting close to the show still under 50
        GildRoseUnitTest.updater(gilded_rose_shop, 3)
        self.assertEqual(test_item.sell_in, 1)
        self.assertLessEqual(test_item.quality, 50)

        # After the concert quality drops to zero
        GildRoseUnitTest.updater(gilded_rose_shop, 5)
        self.assertEqual(test_item.sell_in, -4)
        self.assertEqual(test_item.quality, 0)

    
    def test_sulfuras(self):
        test_item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        gilded_rose_shop = GildedRose([test_item])

        # Legendary item never changes
        gilded_rose_shop.update_quality()
        self.assertEqual(test_item.sell_in, 0)
        self.assertEqual(test_item.quality, 80)


        GildRoseUnitTest.updater(gilded_rose_shop, 10)
        self.assertEqual(test_item.sell_in, 0)
        self.assertEqual(test_item.quality, 80)

    
    def test_conjured(self):

        test_item = Item("Conjured Mana Cake", 3, 6)
        gilded_rose_shop = GildedRose([test_item])

        # Conjured items lose 2 quality per day
        gilded_rose_shop.update_quality()
        self.assertEqual(test_item.sell_in, 2)
        self.assertEqual(test_item.quality, 4)

        GildRoseUnitTest.updater(gilded_rose_shop, 2)
        self.assertEqual(test_item.sell_in, 0)
        self.assertEqual(test_item.quality, 0)  # drops to 0 but not negative

        # After sell date, should not go below 0
        GildRoseUnitTest.updater(gilded_rose_shop, 3)
        self.assertEqual(test_item.sell_in, -3)
        self.assertEqual(test_item.quality, 0)



if __name__ == '__main__':
    unittest.main()




