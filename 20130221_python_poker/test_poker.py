import unittest
from poker import Card, is_pair, is_two_pairs, is_three_of_a_kind,\
    is_four_of_a_kind, is_straight, is_flush, is_straight_flush, is_royal,\
    is_full_house


class TestCard(unittest.TestCase):

    def test_A_converts_to_14(self):
        self.assertEqual(14, Card('A', 'H').value)
        
    def test_T_converts_to_10(self):
        self.assertEqual(10, Card('T', 'H').value)
        
    def test_J_converts_to_11(self):
        self.assertEqual(11, Card('J', 'H').value)
        
    def test_Q_converts_to_12(self):
        self.assertEqual(12, Card('Q', 'H').value)
        
    def test_K_converts_to_13(self):
        self.assertEqual(13, Card('K', 'H').value)


class TestHandTypes(unittest.TestCase):
    
    def test_pair_true(self):
        self.assertTrue(is_pair([
            Card('2', 'D'), Card('2', 'S'),
            Card('A', 'D'), Card('K', 'D'),
            Card('6', 'D')
        ]))

    def test_pair_false(self):
        self.assertFalse(is_pair([
            Card('2', 'D'), Card('3', 'S'),
            Card('A', 'D'), Card('K', 'D'),
            Card('6', 'D')
        ]))

    def test_two_pairs_true(self):
        self.assertTrue(is_two_pairs([
            Card('2', 'D'), Card('2', 'S'),
            Card('A', 'D'), Card('A', 'H'),
            Card('6', 'D')
        ]))

    def test_two_pairs_false(self):
        self.assertFalse(is_two_pairs([
            Card('2', 'D'), Card('2', 'S'),
            Card('A', 'D'), Card('K', 'D'),
            Card('6', 'D')
        ]))

    def test_3_of_a_kind_true(self):
        self.assertTrue(is_three_of_a_kind([
            Card('2', 'D'), Card('2', 'S'),
            Card('2', 'H'), Card('A', 'H'),
            Card('6', 'D')
        ]))

    def test_3_of_a_kind_false(self):
        self.assertFalse(is_three_of_a_kind([
            Card('2', 'D'), Card('2', 'S'),
            Card('A', 'D'), Card('A', 'S'),
            Card('6', 'D')
        ]))

    def test_4_of_a_kind_true(self):
        self.assertTrue(is_four_of_a_kind([
            Card('2', 'D'), Card('2', 'S'),
            Card('2', 'H'), Card('2', 'C'),
            Card('6', 'D')
        ]))

    def test_4_of_a_kind_false(self):
        self.assertFalse(is_four_of_a_kind([
            Card('2', 'D'), Card('2', 'S'),
            Card('A', 'D'), Card('A', 'C'),
            Card('6', 'D')
        ]))

    def test_straight_true_ace_at_start(self):
        self.assertTrue(is_straight([
            Card('A', 'D'), Card('2', 'D'), 
            Card('3', 'S'), Card('4', 'H'), 
            Card('5', 'C'),
        ]))

    def test_straight_true_ace_at_end(self):
        self.assertTrue(is_straight([
            Card('T', 'D'), Card('J', 'S'),
            Card('Q', 'D'), Card('K', 'C'),
            Card('A', 'D')
        ]))

    def test_straight_false(self):
        self.assertFalse(is_straight([
            Card('T', 'D'), Card('J', 'S'),
            Card('2', 'D'), Card('K', 'C'),
            Card('A', 'D')
        ]))

    def test_flush_true(self):
        self.assertTrue(is_flush([
            Card('T', 'D'), Card('3', 'D'),
            Card('2', 'D'), Card('6', 'D'),
            Card('A', 'D')
        ]))

    def test_flush_false(self):
        self.assertFalse(is_flush([
            Card('T', 'S'), Card('3', 'D'),
            Card('2', 'D'), Card('6', 'D'),
            Card('A', 'D')
        ]))
        
    def test_straight_flush_true(self):
        self.assertTrue(is_straight_flush([
            Card('T', 'D'), Card('J', 'D'),
            Card('Q', 'D'), Card('K', 'D'),
            Card('A', 'D')
        ]))

    def test_straight_flush_false_only_flush(self):
        self.assertFalse(is_straight_flush([
            Card('T', 'D'), Card('3', 'D'),
            Card('2', 'D'), Card('6', 'D'),
            Card('A', 'D')
        ]))
                
    def test_straight_flush_false_only_straight(self):
        self.assertFalse(is_straight_flush([
            Card('T', 'S'), Card('J', 'D'),
            Card('Q', 'D'), Card('K', 'D'),
            Card('A', 'D')
        ]))

    def test_straight_flush_false_neither(self):
        self.assertFalse(is_straight_flush([
            Card('2', 'D'), Card('3', 'S'),
            Card('A', 'D'), Card('K', 'D'),
            Card('6', 'D')
        ]))

    def test_royal_straight_flush_true(self):
        self.assertTrue(is_royal([
            Card('T', 'D'), Card('J', 'D'),
            Card('Q', 'D'), Card('K', 'D'),
            Card('A', 'D')
        ]))

    def test_royal_straight_flush_false(self):
        self.assertFalse(is_royal([
            Card('T', 'D'), Card('J', 'D'),
            Card('4', 'D'), Card('K', 'D'),
            Card('A', 'D')
        ]))
        
    def test_full_house_true(self):
        self.assertTrue(is_full_house([
            Card('T', 'D'), Card('T', 'H'),
            Card('T', 'C'), Card('A', 'S'),
            Card('A', 'D')
        ]))
    
        
    def test_full_house_false(self):
        self.assertFalse(is_full_house([
            Card('2', 'D'), Card('T', 'H'),
            Card('T', 'C'), Card('A', 'S'),
            Card('A', 'D')
        ]))


unittest.main()
