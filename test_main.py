import unittest
from main import Cluster, KMean

class CentroidTest(unittest.TestCase):

    def test_calculate_coords(self):
        cA = Cluster()
        cA.add_point((1.2, 2.4))
        cA.add_point((2.4, 3.5))

        assert cA.centroid == (1.8, 3.0)
        assert len(cA.points) == 2

class KMeanTest(unittest.TestCase):

    def test_kmean_assignment(self):
        points = [(1.1, 2.5), (3.4, 1.9)]
        k_mean = KMean(2, points)
        print(k_mean.data_dump())

if __name__ == '__main__':
    unittest.main()