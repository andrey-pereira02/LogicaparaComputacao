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
