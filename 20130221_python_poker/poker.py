from collections import Counter

 
class Card(object):

    CARD_VALUE = {
        'T': 10,
        'A': 14,
        'J': 11,
        'Q': 12,
        'K': 13,
    }

    def __init__(self, value, suit):
        self.value = self.CARD_VALUE.get(value) or int(value)
        self.suit = suit        


def is_pair(cardlist):
    return len(set(c.value for c in cardlist)) == 4


def is_two_pairs(cardlist):
    two_count = 0
    values = (c.value for c in cardlist)
    for count in Counter(values).itervalues():
        if count == 2:
            two_count += 1
    return two_count == 2


def is_three_of_a_kind(cardlist):
    values = (c.value for c in cardlist)
    counts = set(Counter(values).itervalues())
    return True if 3 in counts else False


def is_four_of_a_kind(cardlist):
    return len(set(c.value for c in cardlist)) == 2


def is_straight(cardlist):
    cardvalues = sorted(c.value for c in cardlist)
    if 14 in cardvalues:
        return cardvalues == [2, 3, 4, 5, 14] or cardvalues == range(10, 14 + 1)
    else:
        expected = range(cardvalues[0], cardvalues[-1] +1)
        return cardvalues == expected


def is_flush(cardlist):
    return len(set(c.suit for c in cardlist)) == 1
    
    
def is_straight_flush(cardlist):
    return is_straight(cardlist) and is_flush(cardlist)
    
    
def is_royal(cardlist):
    return is_straight_flush(cardlist) and cardlist[0].value == 10

def is_full_house(cardlist):
    values = (c.value for c in cardlist)
    counts = set(Counter(values).itervalues())
    return True if 3 in counts and 2 in counts else False

