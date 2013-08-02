import unittest
from game import  *


class TestCard(unittest.TestCase):
	def test_play(self):
		hand1 = ['AD','6H','9C','QC','8H']
		hand2 = ['9H','10C','8D','6C','10S']

		#1st round
		p11 = play(hand1)
		p12 = play(hand2, p11[0])

		self.assertEqual(p11, ('AD', 4))
		self.assertEqual(p12, ('8D', 4))

		#2nd round
		p21 = play(hand1)
		p22 = play(hand2, p21[0])

		self.assertEqual(p21, ('6H', 3))
		self.assertEqual(p22, ('9H', 3))


		#3rd round
		p32 = play(hand2)
		p31 = play(hand1, p32[0])

		self.assertEqual(p32, ('10C', 2))
		self.assertEqual(p31, ('9C', 2))

		#4th round
		p42 = play(hand2)
		p41 = play(hand1, p42[0])

		self.assertEqual(p42, ('6C', 1))
		self.assertEqual(p41, ('QC', 1))

		#5th round
		p51 = play(hand1)
		p52 =play(hand2, p51[0])

		self.assertEqual(p51, ('8H', 0))
		self.assertEqual(p52, ('10S', 0))

		self.assertEqual(lead_card(p51[0],p52[0]),p51[0])



if __name__ == '__main__':
    unittest.main()
