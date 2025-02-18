from itertools import product

class Formula:
    def __init__(self):
        pass
            
    def __str__(self):
        if type(self) == Atom:
            return self.letter
        elif type(self) == Negation:
            return '~' + str(self.subf)
        elif type(self) == Binary:
            return '(' + str(self.left) + self.connective + str(self.right) + ')'
    
    def letters(self):
        if type(self) == Atom:
            return set(self.letter)
        if type(self) == Negation:
            return self.subf.letters()
        if type(self) == Binary:
            return self.left.letters().union(self.right.letters())
    
    def value(self, I):
        if type(self) == Atom:
            return I[self.letter]
        if type(self) == Negation:
            return not self.subf.value(I)
        if type(self) == Binary:
            if self.connective == 'Y':
                return self.left.value(I) and self.right.value(I)
            if self.connective == 'O':
                return self.left.value(I) or self.right.value(I)
            if self.connective == '>':
                return not self.left.value(I) or self.right.value(I)
            if self.connective == '=':
                return self.left.value(I) == self.right.value(I)
    
    def find_models(self):
        letters = self.letters()
        num_letters = len(letters)
        truth_combinations = list(product([True, False], repeat=num_letters))
        interpretations = [dict(zip(letters, combination)) for combination in truth_combinations]
        models = []
        for I in interpretations:
            if self.value(I):
                models.append(I)
        return models
            
    def num_conec(self):
        if type(self) == Atom:
            return 0
        if type(self) == Negation:
            return 1 + self.subf.num_conec()
        if type(self) == Binary:
            return 1 + self.left.num_conec() + self.right.num_conec()

    def num_paren(self):
        if type(self) == Atom:
            return 0
        if type(self) == Negation:
            return self.subf.num_paren()
        if type(self) == Binary:
            return 2 + self.left.num_paren() + self.right.num_paren()

    def num_bin(self):
        if type(self) == Atom:
            return 0
        if type(self) == Negation:
            return self.subf.num_bin()
        if type(self) == Binary:
            return 2 + self.left.num_bin() + self.right.num_bin()
    
    def sub_forms(self):
        if type(self) == Atom:
            return {self.__str__()}
        if type(self) == Negation:
            return {self.__str__()}.union(self.subf.sub_forms())
        if type(self) == Binary:
            return {self.__str__()}.union(self.left.sub_forms()).union(self.right.sub_forms())
    

            
class Atom(Formula):
    def __init__(self, letter: str):
        self.letter = letter

class Negation(Formula):
    def __init__(self, subformula: Formula):
        self.subf = subformula

class Binary(Formula):
    def __init__(self, connective: str, left: Formula, right: Formula):
        assert(connective in ['Y', 'O', '>', '='])
        self.connective = connective
        self.left = left
        self.right = right



