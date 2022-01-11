import unittest
import FindEss as fs
import sympy as sy

class TestFindEss(unittest.TestCase):

    def testTwoStrategies(self):

        A1 = [[1,4],[0,2]]
        self.assertEqual(fs.findEss(A1), [[1, 0]])

        # A2 = [[-1/2,2],[0,1]]
        # self.assertEqual(fs.findEss(A2), [[sy.Rational(2,3), sy.Rational(1,3)]])

    def testThreeStrategies(self):

        A1 = [[0,-1,1],[1,0,-1],[-1,1,0]]
        self.assertEqual(fs.findEss(A1), [])

        A2 = [[-2,1,4],[3,3,-2],[2,-1,3]]
        self.assertEqual(fs.findEss(A2), [[0, 1, 0], [sy.sympify('0.2',rational=True), 0, sy.sympify('0.8',rational=True)]])

    def testFourStrategies(self):

        A1 = [[3,-2,4,-1],[4,-2,1,4],[-1,3,3,-2],[1,2,-1,3]]
        self.assertEqual(fs.findEss(A1), [[0, sy.sympify('0.2',rational=True), 0, sy.sympify('0.8',rational=True)]]) 

        A2 = [[0.625,0.369,0.276,0.255], [0.848,0.602,0.356,0.266],
                        [0.685,0.620,0.440,0.260],[0,0,0,0]]
        self.assertEqual(fs.findEss(A2), [[0,0,1,0]])

if __name__ == '__main__':
    unittest.main()