import random
import math

# Cluster assumptions
# the cluster assumptions is that the centroid is randomly generaged at initialization
class Cluster():
    def __init__(self) -> None:
        self.points = []
        self.centroid = (random.randint(-10, 10), random.randint(-10, 10))

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

class KMean():
    def __init__(self, number_clusters, points) -> None:
        if (number_clusters > len(points)):
            raise 'Number of clusters is greater than points'

        self.clusters = self.create_clusters(number_clusters)
        self.null_points = points
        self.assign_points_to_cluster()

    def find_clusters(self, point):
        cluster_index = 0 # index of the cluster
        cluster_distance = 0

        for c_index in range(len(self.clusters)):
            distance = self.distance(point, self.clusters[c_index].centroid)
            print(distance)
            if c_index == 0:
                cluster_distance = distance
            elif (cluster_distance > distance):
                cluster_distance = distance
                cluster_index = c_index

        self.clusters[cluster_index].add_point(point)

    def assign_points_to_cluster(self):
        for point in self.null_points:
            self.find_clusters(point)

    def create_clusters(self, number_clusters):
        clusters = []
        for x in range(number_clusters):
            clusters.append(Cluster())
        return clusters

    def distance(self, point_a, point_b) -> float:
        x1_point, y1_point = point_a
        x2_point, y2_point = point_b
        return math.sqrt((y2_point - y1_point)**2 + (x2_point - x1_point)**2)

    def graph(self):
        pass

    def get_number_of_clusters(self):
        return len(self.clusters)

    def data_dump(self):
        data = {}
        for c_index in range(len(self.clusters)):
            data[c_index] = {}
            print(f'Cluster {c_index}')
            print(f'Points: {self.clusters[c_index].points}')
            print(f'Centroid: {self.clusters[c_index].centroid}')
            data[c_index]['points'] = self.clusters[c_index].points
            data[c_index]['centroid'] = self.clusters[c_index].centroid

        return data

if __name__ == '__main__':
    points = [(1.1, 2.5), (3.4, 1.9)]
    k_mean = KMean(2, points)
    print(k_mean.data_dump())