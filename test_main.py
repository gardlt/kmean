import unittest
from sklearn.datasets._samples_generator import make_blobs

from main import Cluster, KMean

class CentroidTest(unittest.TestCase):

    def test_calculate_coords(self):
        cA = Cluster((0,0))
        cA.add_point((1.2, 2.4))
        cA.add_point((2.4, 3.5))

        assert cA.centroid == (1.8, 3.0)
        assert len(cA.points) == 2
        assert cA.centroid != (0,0)

class KMeanTest(unittest.TestCase):

    def test_kmean_assignment(self):
        data, _ = make_blobs(n_samples=10, centers=2, random_state=0)
        k_mean = KMean(2, data)
        assert len(k_mean.clusters) == 2

    def test_kmean_distance(self):
        data, _ = make_blobs(n_samples=10, centers=2, random_state=0)
        k_mean = KMean(2, data)
        point_a=(7,9)
        point_b=(2,3)
        actual = k_mean.distance(point_a, point_b)
        assert round(actual, 1) == 7.8

if __name__ == '__main__':
    unittest.main()