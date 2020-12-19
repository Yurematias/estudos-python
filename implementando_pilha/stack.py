class Stack:
    def __init__(self, maxSize):
        self.__maxSize = maxSize
        self.__elements = []

    def push(self, element):
        if self.length < self.__maxSize:
            self.__elements.append(element)

    def pop(self):
        if not self.is_empty:
            removed_element = self.top
            self.__elements.pop()
            return removed_element

    @property
    def length(self):
        return len(self.__elements)

    @property
    def top(self):
        if not self.is_empty:
            return self.__elements[len(self.__elements) - 1]

    @property
    def asArray(self):
        return [ *self.__elements ]

    @property
    def is_empty(self):
        return self.length == 0
