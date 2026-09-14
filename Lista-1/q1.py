from formula import *


def number_of_connectives(A: Formula):
    if isinstance(A, Atom):
        return 0

    if isinstance(A, Not):
        return 1 + number_of_connectives(A.inner)

    if isinstance(A, Or) or isinstance(A, And) or isinstance(Formula, Implies):
        return 1 + number_of_connectives(A.left) + number_of_connectives(A.right)
