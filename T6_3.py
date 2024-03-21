

class EnsembleAvecMin:

    def get_min(self):
        raise NotImplementedError("Cette méthode est abstraite")


class EnsembleList(EnsembleAvecMin):

    def __init__(self):
        self.__elements = []

    def add(self, element: int):
        self.__elements.append(element)

    def get_min(self):
        if not self.__elements:
            return None
        return min(self.__elements)

    def __add__(self, other):
        composite = CompositeAvecMin(self, other)
        return composite


class EnsembleDict(EnsembleAvecMin):

    def __init__(self):
        self.__elements = {}

    def add(self, key: str, value: int):
        self.__elements[key] = value

    def get_min(self):
        if not self.__elements:
            return None
        return min(self.__elements.values())


class CompositeAvecMin(EnsembleAvecMin):

    def __init__(self, *ensembles):
        self.__ensembles = ensembles

    def get_min(self):
        min_values = [ensemble.get_min() for ensemble in self.__ensembles if ensemble.get_min() is not None]
        if not min_values:
            return None
        return min(min_values)


if __name__ == '__main__':

    ed = EnsembleDict()
    ed.add("A", 10)
    ed.add("B", 12)
    ed.add("C", -5)

    el = EnsembleList()
    el.add(4)
    el.add(-8)

    ce = CompositeAvecMin(el, ed)
    ce2 = el + ce
    print(ed.get_min(), el.get_min(), ce.get_min(), ce2.get_min())

    ed.add("D", -10)
    print(ed.get_min(), el.get_min(), ce.get_min())
    other_el = EnsembleList()
