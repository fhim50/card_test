from game import highest_rank
import unittest

class TestCard(unittest.Test):
	def test_highest_rank(self):
		self.assertEqual(highest_rank(['6D','KD','10D']),'KD')
