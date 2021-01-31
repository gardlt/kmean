import unittest
from sklearn.datasets._samples_generator import make_blobs

from main import Cluster, KMean, find_optimal_cluster_size

class CentroidTest(unittest.TestCase):

    def test_calculate_coords(self):
        cA = Cluster((0,0))
        cA.add_point((1.2, 2.4))
        cA.add_point((2.4, 3.5))

        assert cA.centroid == (1.8, 3.0)
        assert len(cA.points) == 2
        assert cA.centroid != (0,0)

    def test_calculate_mean(self):
        cA = Cluster((0,0))
        cA.add_point((1, 1))
        cA.add_point((2, 2))
        cA.add_point((3, 3))
        assert cA.centroid == (2.0,2.0)
        cA.remove_point(0)
        assert cA.centroid == (2.5,2.5)
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

class OptimalData(unittest.TestCase):
    def test_optimal_cluster(self):
        expected = 2
        sample_size = 100
        data, _ = make_blobs(n_samples=sample_size, cluster_std=0.60, random_state=0)
        optimal_clusters = find_optimal_cluster_size(sample_size, data=data)
        self.assertEqual(expected, optimal_clusters)


if __name__ == '__main__':
    unittest.main()