from formula import *


def big_and(formulas):
    result = formulas[0]

    for formula in formulas[1:]:
        result = And(result, formula)

    return result


def big_or(formulas):
    result = formulas[0]

    for formula in formulas[1:]:
        result = Or(result, formula)

    return result


def formula_a():
    formulas = []

    for i in range(1, 21):
        formulas.append(Atom(f"p{i}"))

    return big_and(formulas)


def formula_b(n):
    formulas = []

    for i in range(1, n + 1):
        formulas.append(Atom(f"p{i}"))

    return big_and(formulas)


def formula_c(n, m):
    formulas_or = []

    for i in range(1, n + 1):
        formulas_and = []

        for j in range(1, m + 1):
            atom = Atom(f"p{i},{j}")
            formulas_and.append(Not(atom))

        formulas_or.append(big_and(formulas_and))

    return big_or(formulas_or)


def formula_d(n):
    formulas = []

    for i in range(1, n + 1):
        ai = Atom(f"a{i}")
        bi = Atom(f"b{i}")
        ai1 = Atom(f"a{i + 1}")
        bi1 = Atom(f"b{i + 1}")

        or_formula = Or(ai1, bi1)

        left = Implies(ai, or_formula)
        right = Implies(bi, or_formula)

        formulas.append(And(left, right))

    return big_and(formulas)


def formula_e(n):
    formulas = []

    for i in range(1, n + 1):
        pi = Atom(f"p{i}")
        qi = Atom(f"q{i}")

        formulas.append(Or(pi, qi))

    left = big_or(formulas)
    right = Atom(f"p{n + 1}")

    return Implies(left, right)


def formula_f(n):
    formulas_and = []

    for i in range(1, n + 2):
        formulas_or = []

        for j in range(1, n + 1):
            formulas_or.append(Atom(f"p{i},{j}"))

        formulas_and.append(big_or(formulas_or))

    return big_and(formulas_and)


def formula_g(n):
    formulas_i = []

    for i in range(1, n + 1):

        formulas_k = []

        for k in range(i + 1, n + 1):

            formulas_j = []

            for j in range(1, n + 1):
                pij = Atom(f"p{i},{j}")
                pkj = Atom(f"p{k},{j}")

                formulas_j.append(And(pij, pkj))

            formulas_k.append(big_and(formulas_j))

        formulas_i.append(big_or(formulas_k))

    return big_or(formulas_i)
