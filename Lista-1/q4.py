from formula import *


def is_negation_normal_form(formula: Formula):
    if isinstance(formula, Atom):
        return True

    if isinstance(formula, Not):
        return isinstance(formula.inner, Atom)

    if isinstance(formula, (And, Or)):
        return is_negation_normal_form(formula.left) + is_negation_normal_form(formula.right)

    return False
