from formula import *


def Atoms(formula: Formula):
    if isinstance(formula, Atom):
        return {formula}

    if isinstance(formula, Not):
        return {formula}.union(Atoms(formula.inner))

    if isinstance(formula, (And, Implies, Or)):
        return {formula}.union(Atoms(formula.right)).union(Atoms(formula.left))
