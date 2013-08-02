from game import play
import unittest

class TestCard(unittest.TestCase):
	# def test_highest_rank(self):
	# 	#self.assertEqual(highest_rank(['6D','KD','10D']),'KD')
	# 	pass

	def test_play(self):
		self.assertEqual(play(['6D','KD','10D'],'AD')[0],'6D')
		self.assertEqual(play(['8D','10D','6H'])[0],'8D')
		self.assertEqual(play(['AC','KS','10D'],'10H')[0],'AC')
if __name__ == '__main__':
	unittest.main()