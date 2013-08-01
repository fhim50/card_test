import unittest
from game import  *

hand1 = ['AD','6H','9C','QC','8H']
hand2 = ['9H','10C','8D','6C','10S']

#1st round
p11 = play(hand1)
p12 = play(hand2,'AD')

#2nd round
p21 = play(hand1)
p22 = play(hand2,'6H')

#3rd round
p32 = play(hand2)
p31 = play(hand1,'10C')

#4th round
p42 = play(hand2)
p41 = play(hand1,'6C')

#5th round
p51 = play(hand1)
p52 =play(hand2,'8H')

class TestCard(unittest.TestCase):
	def test_1st_play(self):
		self.assertEqual(p11[1],4)
		self.assertEqual(p12[1],4)
		self.assertEqual(p12[0],'8D')
		self.assertEqual(lead_card(p11[0],p12[0]),p11[0])

	def test_2nd_play(self):
		self.assertEqual(p21[1],3)
		self.assertEqual(p22[1],3)
		self.assertEqual(p22[0],'9H')
		self.assertEqual(lead_card(p21[0],p22[0]),p22[0])

	def test_3rd_round(self):
		self.assertEqual(p31[1],2)
		self.assertEqual(p32[1],2)
		self.assertEqual(p31[0],'9C')
		self.assertEqual(lead_card(p31[0],p32[0]),p32[0])
		
	def test_4th_round(self):
		self.assertEqual(p41[1],1)
		self.assertEqual(p42[1],1)
		self.assertEqual(p41[0],'QC')
		self.assertEqual(lead_card(p41[0],p42[0]),p41[0])

	def test_5th_round(self):
		self.assertEqual(p51[1],0)
		self.assertEqual(p52[1],0)
		self.assertEqual(p52[0],'10S')

	def test_winner(self):
		self.assertEqual(lead_card(p51[0],p52[0]),p51[0])



if __name__ == '__main__':
    unittest.main()
