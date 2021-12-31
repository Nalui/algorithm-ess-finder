import unittest
import EssByNash as en
import numpy as np

class TestessByNash(unittest.TestCase):

    def testTwoStrategies(self):

        A1 = np.array([[4,2],[1,3]])
        self.assertTrue(np.allclose(en.essByNash(A1), [[1, 0],[0, 1]]))

        A2 = np.array([[2,4],[3,1]])
        self.assertTrue(np.allclose(en.essByNash(A2), [[3/4, 1/4]]))

        A3 = np.array([[1,1],[1,1]]) #colocar uma matriz melhor
        self.assertTrue(np.allclose(en.essByNash(A3), []))

    def testThreeStrategies(self):

        A1 = np.array([[-2,1,4],[3,3,-2],[2,-1,3]])
        self.assertTrue(np.allclose(en.essByNash(A1), [[0, 1, 0], [0.2, 0, 0.8]]))

        A2 = np.array([[0,-1,1],[1,0,-1],[-1,1,0]])
        self.assertTrue(np.allclose(en.essByNash(A2), []))

    def testFourStrategies(self):

        A1 = np.array([[3,-2,4,-1],[4,-2,1,4],[-1,3,3,-2],[1,2,-1,3]])
        self.assertTrue(np.allclose(en.essByNash(A1), [[0, 0.2, 0, 0.8]]))

        A2 = np.array([[0.625,0.369,0.276,0.255], [0.848,0.602,0.356,0.266],
                        [0.685,0.620,0.440,0.260],[0,0,0,0]])
        self.assertTrue(np.allclose(en.essByNash(A2), [[0,0,1,0]]))

if __name__ == '__main__':
    unittest.main()