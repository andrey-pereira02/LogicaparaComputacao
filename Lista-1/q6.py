from formula import *


def substitution(formula: Formula, old_subformula: Formula, new_subformula: Formula):
    if formula == old_subformula:
        return new_subformula

    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, Not):
        return Not(substitution(formula.inner, old_subformula, new_subformula))

    if isinstance(formula, And):
        return And(
            substitution(formula.left, old_subformula, new_subformula),
            substitution(formula.right, old_subformula, new_subformula)
        )

    if isinstance(formula, Or):
        return Or(
            substitution(formula.left, old_subformula, new_subformula),
            substitution(formula.right, old_subformula, new_subformula)
        )

    if isinstance(formula, Implies):
        return Implies(
            substitution(formula.left, old_subformula, new_subformula),
            substitution(formula.right, old_subformula, new_subformula)
        )
