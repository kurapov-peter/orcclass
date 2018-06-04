from utils import *


class VectorAttribute:
    GOOD = 1
    BAD = 0
    UNDEFINED = -1

    def __init__(self, coordinates):
        self.current_class = VectorAttribute.UNDEFINED
        self.coordinates = coordinates

    def __repr__(self):
        return "Vector[class:" + str(self.current_class) + ";coord:" + str(self.coordinates) + "]"

    def __lt__(self, other):
        other_coords = other.get_coordinates()
        for i in range(len(self.coordinates)):
            if self.coordinates[i] >= other_coords[i]:
                return False
        return True

    def __le__(self, other):
        other_coords = other.get_coordinates()
        for i in range(len(self.coordinates)):
            if self.coordinates[i] > other_coords[i]:
                return False
        return True

    def __gt__(self, other):
        other_coords = other.get_coordinates()
        for i in range(len(self.coordinates)):
            if self.coordinates[i] <= other_coords[i]:
                return False
        return True

    def __ge__(self, other):
        other_coords = other.get_coordinates()
        for i in range(len(self.coordinates)):
            if self.coordinates[i] < other_coords[i]:
                return False
        return True

    def set_class(self, new_class):
        if self.current_class != VectorAttribute.UNDEFINED:
            raise ValueError("Vector already set: " + str(self))
        if new_class not in [VectorAttribute.GOOD, VectorAttribute.BAD]:
            raise ValueError("Unable to set vector class to " + new_class)
        self.current_class = new_class

    def get_coordinates(self):
        return self.coordinates

    def undefined(self):
        return self.current_class == VectorAttribute.UNDEFINED

    def get_closeness_to(self, class_info, class_center):
        max_dist = get_euclid_distance([2] * len(self.coordinates), [0] * len(self.coordinates))
        dist_of_interest = get_euclid_distance(self.coordinates, class_center)
        cardinality = 2  # todo
        distances = [get_euclid_distance(self.coordinates, x) for x in class_info.get_centers()]
        alternative_dist = sum(distances)
        return (max_dist - dist_of_interest) / (cardinality * max_dist - alternative_dist)
