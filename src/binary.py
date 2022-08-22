import random as r

import numpy as np


class binaryShell:
    def __init__(self, size: int = 10):
        self.size = size
        self.__bool_vector = []

        for i in range(size):
            self.__bool_vector.append(r.choice([0, 1]))

    def bit_flip(self, position: int):
        if self.__bool_vector[position]:
            self.__bool_vector[position] = 0
        else:
            self.__bool_vector[position] = 1

    def print_sequence(self):
        result = ''
        for val in self.__bool_vector:
            if val:
                result += '1'
            else:
                result += '0'
        print(result)


a = binaryShell()
a.print_sequence()
a.bit_flip(-1)
a.print_sequence()
