from utils import normalize_rounding


class ClassInfo:
    _centers = []  # BAD(x, y, ...), ..., GOOD(x, y, ...)
    _cardinality = []
    _names = []

    def __init__(self, number_of_classes=2, size=9, names=None):
        if names is None:
            names = ["bad", "good"]
        self._centers = self._setup_centers(size)
        self._cardinality = self._setup_cardinality(number_of_classes)
        self._names = names

    def __repr__(self):
        string = "ClassInfo[\n\tcenters:\n\t{\n"
        for i in range(len(self._names)):
            string += "\t\t" + str(self._names[i]) + "=" + str(self._centers[i]) + "\n"
        string += "\t}\n\tcardinality:\n\t{\n"
        for i in range(len(self._names)):
            string += "\t\t" + str(self._names[i]) + "=" + str(self._cardinality[i]) + "\n"
        string += "\t}\n];"
        return string

    @staticmethod
    def _setup_centers(size):
        centers = [[0] * size, [2] * size]
        return centers

    @staticmethod
    def _setup_cardinality(number_of_classes):
        return [1] * number_of_classes

    def add_vector(self, destination_class, vector):
        if not destination_class < len(self._centers):
            raise ValueError("No such class: " + destination_class)

        for i in range(len(self._centers[destination_class])):
            card = self._cardinality[destination_class]
            self._centers[destination_class][i] = (self._centers[destination_class][i] * card + vector[i]) / (card + 1)

        self._cardinality[destination_class] += 1

    def get_center(self, class_):
        return [normalize_rounding(x) for x in self._centers[class_]]

    def get_centers(self):
        return self._centers

    def round_centers(self):
        for i in range(len(self._centers)):
            self._centers[i] = self.get_center(i)

    def get_number_of_defined_vectors(self):
        return sum(self._cardinality)

    def add_vectors(self, class_value, vectors):
        composed = [sum(x) for x in zip(*vectors)]
        size = len(vectors)
        print("adding ", size, " vectors")
        print(vectors)
        card = self._cardinality[class_value]
        for i in range(len(self._centers[class_value])):
            self._centers[class_value][i] = (self._centers[class_value][i] * card + composed[i]) / (card + size)
        self._cardinality[class_value] += size

    def get_defined_number(self):
        return sum(self._cardinality)
