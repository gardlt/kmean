from sklearn.datasets._samples_generator import make_blobs
import matplotlib.pyplot as plt

import math
import numpy as np

# Cluster assumptions
# the cluster assumptions is that the centroid is randomly generaged at initialization
class Cluster():
    def __init__(self, center) -> None:
        self.points = []
        self.centroid = center

    def calculate_mean_x(self):
        x_sum = 0

        for x, _ in self.points:
            x_sum += x

        return x_sum / len(self.points)

    def calculate_mean_y(self):
        y_sum = 0

        for _, y in self.points:
            y_sum += y

        return y_sum / len(self.points)

    def calculate_mean(self):
        x_mean = self.calculate_mean_x()
        y_mean = self.calculate_mean_y()
        # TODO: might need to make this configurable
        self.centroid = (round(x_mean, 1), round(y_mean, 1)) # set the decimal precision to 1

    def add_point(self, coord):
        self.points.append(coord)
        self.calculate_mean()

    def remove_point(self, index):
        self.points.pop(index)
        self.calculate_mean()

class KMean():
    def __init__(self, number_clusters, points) -> None:
        if (number_clusters > len(points)):
            raise 'Number of clusters is greater than points'

        self.null_points = points
        self.clusters = self.create_clusters(number_clusters)
        self.assign_points_to_cluster()

    def find_clusters(self, point):
        cluster_index = 0 # index of the cluster
        cluster_distance = 0

        for c_index in range(len(self.clusters)):
            distance = self.distance(point, self.clusters[c_index].centroid)

            if c_index == 0:
                cluster_distance = distance
            elif (cluster_distance > distance):
                cluster_distance = distance
                cluster_index = c_index

        self.clusters[cluster_index].add_point(point)

    def get_centroid_arr(self):
        cluster_centroid = []
        for _, cluster in enumerate(self.clusters):
            cluster_centroid.append(cluster.centroid)
        return cluster_centroid

    def assign_points_to_cluster(self):
        for point in self.null_points:
            self.find_clusters(point)

        changed = []
        for x in range(len(self.clusters)):
            changed.append(True)
        cluster = 0
        while max(changed):

            changed[cluster] = self.rebalance_clusters(cluster)
            cluster = cluster + 1
            if cluster == len(self.clusters) and not all(changed):
                change = False
            if cluster >= len(self.clusters):
                cluster = 0


    def rebalance_clusters(self, cluster) -> bool:
        cluster_centroids = self.get_centroid_arr()
        changed = False
        for i, point in enumerate(self.clusters[cluster].points):
            lst_distance = self.distance(point_a=point, point_b=cluster_centroids[cluster])
            for j, cc in enumerate(cluster_centroids):
                distance_check = self.distance(point_a=point, point_b=cc)
                if distance_check < lst_distance:
                    self.clusters[cluster].remove_point(i)
                    self.clusters[j].add_point(point)
                    changed = True
                    cluster_centroids = self.get_centroid_arr()
        return changed



    def create_clusters(self, number_clusters):
        rng = np.random.RandomState(2)
        i = rng.permutation(len(self.null_points))[:number_clusters]
        centers = self.null_points[i]
        clusters = []
        for x in range(number_clusters):
            clusters.append(Cluster(centers[x]))
        return clusters

    def distance(self, point_a, point_b) -> float:
        x1_point, y1_point = point_a
        x2_point, y2_point = point_b
        return math.sqrt((y2_point - y1_point)**2 + (x2_point - x1_point)**2)

    def graph(self, centers):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        for c_index in range(len(self.clusters)):
            ax.scatter(np.array(self.clusters[c_index].points)[:, 0], np.array(self.clusters[c_index].points)[:, 1], alpha=0.8, edgecolors="none", s=30)
            ax.scatter(self.clusters[c_index].centroid[0], self.clusters[c_index].centroid[1], alpha=0.9, c='black')

        plt.savefig(f'clusters-{len(self.clusters)}-sample-{len(self.null_points)}.png')

    def get_number_of_clusters(self):
        return len(self.clusters)

    def data_dump(self):
        data = {}
        centroids = []
        for c_index in range(len(self.clusters)):
            data[c_index] = {}
            print(f'Cluster {c_index}')
            print(f'Centroid: {self.clusters[c_index].centroid}')
            data[c_index]['points'] = self.clusters[c_index].points
            data[c_index]['centroid'] = self.clusters[c_index].centroid
            centroids.append(self.clusters[c_index].centroid)
        self.graph(centroids)
        return centroids

if __name__ == '__main__':
    clusters = 4
    for sample_size in [10, 20, 100]:
        data, _ = make_blobs(n_samples=sample_size, centers=clusters)
        k_mean = KMean(clusters, data)
        k_mean.data_dump()
