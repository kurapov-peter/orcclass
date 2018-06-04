from random import randint

from utils import *
from ClassInfo import ClassInfo
from VectorAttribute import VectorAttribute


class Solver:
    _matrix = []
    _info = None
    BAD_CLASS = 0
    GOOD_CLASS = 1

    def __init__(self, size=6):
        self._info = ClassInfo(size=size)
        self._matrix = [VectorAttribute(get_coordinate_for_int(i, size=size)) for i in range(3 ** size)]
        # lowest and highest are predefined
        self._matrix[0].set_class(VectorAttribute.BAD)
        self._matrix[len(self._matrix) - 1].set_class(VectorAttribute.GOOD)
        self._size = size

    def __repr__(self):
        string = str(self._info) + "\n\n"
        # for i in range(len(self._matrix)):
        #     string += str(self._matrix[i])
        return string

    def process_user_input(self, coordinates, class_value):
        target_vector = self._matrix[get_int_for_coordinates(coordinates)]
        print("user decision for " + str(target_vector) + " is " + str(class_value))

        to_add = []
        for i in range(len(self._matrix)):
            if self._matrix[i].undefined():
                if class_value == VectorAttribute.BAD:
                    if self._matrix[i] <= target_vector:
                        self._matrix[i].set_class(class_value)
                        to_add.append(self._matrix[i].get_coordinates())
                if class_value == VectorAttribute.GOOD:
                    if self._matrix[i] >= target_vector:
                        self._matrix[i].set_class(class_value)
                        to_add.append(self._matrix[i].get_coordinates())
        self._info.add_vectors(class_value, to_add)
        # print(self._info.get_centers())
        self._info.round_centers()

    def get_best_informative_vector(self):
        best_value = -1
        best_value_adjusted = -1
        best_vector_adjusted = None
        best_vector = None
        for i in range(len(self._matrix)):
            vector = self._matrix[i]
            if vector.undefined():
                closenesses = [vector.get_closeness_to(self._info, center) for center in self._info.get_centers()]
                estimations = self.get_estimations(vector)
                assert len(closenesses) == len(estimations)
                conditional = abs(closenesses[0] - closenesses[1])
                informativity = sum([a*b for a, b in zip(closenesses, estimations)])
                if informativity > best_value:
                    best_value = informativity
                    best_vector = vector
                # if conditional < estimations[0] and conditional < estimations[1] and \
                #                 informativity > best_value_adjusted:
                #     best_vector_adjusted = vector
                #     best_value_adjusted = informativity

        print("best informative vector is " + str(best_vector))
        if best_vector_adjusted is not None:
            best_vector = best_vector_adjusted
        return best_vector

    def get_estimations(self, vector):
        result = [0, 0]  # affects number of classes
        for i in range(len(self._matrix)):
            if self._matrix[i].undefined():
                if self._matrix[i] >= vector:
                    result[1] += 1
                if self._matrix[i] <= vector:
                    result[0] += 1
        return result

    def is_finished(self):
        return self._info.get_number_of_defined_vectors() == 3**self._size

    def border(self):
        upper_border = {self._matrix[0]}
        lower_border = {self._matrix[len(self._matrix)-1]}
        for vector in self._matrix:
            if vector.current_class == VectorAttribute.BAD:
                tmp = upper_border.copy()
                flag = True
                for elem in tmp:
                    if vector >= elem:
                        upper_border.remove(elem)
                    elif vector <= elem:
                        flag = False
                if flag:
                    upper_border.add(vector)
            if vector.current_class == VectorAttribute.GOOD:
                tmp = lower_border.copy()
                flag = True
                for elem in tmp:
                    if vector <= elem:
                        lower_border.remove(elem)
                    elif vector >= elem:
                        flag = False

                if flag:
                    lower_border.add(vector)
        return upper_border, lower_border

    def get_progress(self):
        return self._info.get_defined_number() / (3 ** self._size)


if __name__ == '__main__':
    # mean_iter = 0
    # for i in range(100):
    solution = Solver(size=3)
    iterations = 0
    while not solution.is_finished():
        ask = solution.get_best_informative_vector()
        print(ask)
        answer = int(input())
        # answer = randint(0, 1)
        assert answer == 0 or answer == 1
        solution.process_user_input(ask.get_coordinates(), answer)
        iterations += 1
        print(solution)

    print("Done in ", iterations, " iterations")
    print(solution.border())
    # print('==========')
    # print(solution)
    #     mean_iter += iterations
    #
    # print(mean_iter / 100.)

    for i in range(128):
        lst = get_coordinate_for_int(i, 10)
        if i != get_int_for_coordinates(lst):
            print(i, lst, get_int_for_coordinates(lst))
