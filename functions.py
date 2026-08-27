from formula import *


def lenght(formula: Formula):

    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return lenght(formula.inner) + 1
    if isinstance(formula, And) or isinstance(formula, Or) or isinstance(formula, Implies):
        return lenght(formula.left) + lenght(formula.right) + 1


def subformlas(formula: Formula):

    if isinstance(formula, Atom):
        # essas chaves representam um conjunto do objeto, quase que um set pelo oq eu entendi
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformlas(formula.inner))
    if isinstance(formula, And) or isinstance(formula, Or) or isinstance(formula, Implies):
        left = subformlas(formula.left)
        right = subformlas(formula.right)

        return {formula}.union(left).union(right)


"""Codigo para ver se duas formulas são logicamente equivalentes """


def is_logical_equivalence(formula1, formula2):

    if isinstance(formula1, Atom) and isinstance(formula2, Atom):
        return True if formula1.__eq__(formula2) else False

    if isinstance(formula1, Not) and isinstance(formula2, Not):
        return is_logical_equivalence(formula1.inner, formula2.inner)

    if isinstance(formula1, (And, Implies, Or)) or isinstance(formula2, (And, Implies, Or)):

        if type(formula1) != type(formula2):
            return False

        return is_logical_equivalence(formula1.left, formula2.left) and is_logical_equivalence(formula1.right, formula2.right)

    return False


"""Tentativa de codigo para ver se é uma tautologia,provavelmente esta BEM errado"""


def is_valid(formula1: Formula):

    if isinstance(formula1, Atom):
        return True if formula1 == True else False

    if isinstance(formula1, Not):
        return is_valid(formula1.inner)

    if isinstance(formula1, (And, Or, Implies)):
        return is_valid(formula1.left) and is_valid(formula1.right)
