# -*- coding: utf-8 -*-

class Updater(object):

    # Quality can't go below 0 or above 50
    quality_min = 0
    quality_max = 50

    def normal_item(self, item):
        # Regular items lose 1 quality each day and 2 after the sell date
        if item.sell_in > 0:
            change = -1
        else:
            change = -2
        
        item.quality = max((item.quality + change), self.quality_min)
        item.sell_in -= 1

    def aged_brie(self, item):
         # Aged Brie actually improves over time
        if item.sell_in > 0:
            change = 1
        else:
            change = 2
        item.quality = min((item.quality + change), self.quality_max)
        item.sell_in -= 1


    def backstage_passes(self, item):
        # Backstage passes, +1 when more than 10 days left,
        # +2 when 6–10 days, +3 when 1–5 days and then drop to 0 after the concert
        def quality(item, change):
            item.quality = min(item.quality + change, self.quality_max)

        if item.sell_in > 10:
            change = 1
            quality(item, change)
        elif item.sell_in > 5:
            change = 2
            quality(item, change)
        elif item.sell_in > 0:
            change = 3
            quality(item, change)
        else:
            item.quality = 0

        item.sell_in -= 1

    def sulfuras(self, item):
        # Legendary item, no changes
        pass


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        updater = Updater()

        for item in self.items:
            if item.name == 'Aged Brie':
                updater.aged_brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                updater.backstage_passes(item)
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                updater.sulfuras(item)
            else:
                updater.normal_item(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
