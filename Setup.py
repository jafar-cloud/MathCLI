from sympy import (
    sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc, sinh, cosh, tanh, coth, sech, csch,
    asinh, acosh, atanh, acoth, asech, acsch, atan2, log, exp, sqrt, pi, E, oo, factorial, gamma, real_root, S,
    # Do not remove these, they are used/imported in Functions.py
    solve, Eq, parse_expr, Expr, diff, symbols, integrate
)
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application


# Add the transformation to support things like '2x'
transformations = standard_transformations + (implicit_multiplication_application,)

allowed = {"__builtins__": {}}
variables: dict[str, int | float] = {"inf": oo, "e": E, "pi": pi}
allowed_ids = "abcdefghijklmnopqrstuvwxyz1234567890_"
allowed_id_first_chars = "abcdefghijklmnopqrstuvwxyz_"

local_dict = {
    # Constants
    "pi": pi,
    "e": E,
    "inf": oo,

    # This is a weirdo AND a hidden feature...
    "z": S.Zero,
    

    # Arithmetic functions
    "sqrt": sqrt,
    "log": log,     # natural log by default
    "ln": log,
    "exp": exp,
    "factorial": factorial,
    "gamma": gamma,
    "atan2": atan2,
    "root": real_root,

    # Trigonometric functions and inverses
    "sin": sin, "cos": cos, "tan": tan, "asin": asin, "acos": acos, "atan": atan,
    "cot": cot, "sec": sec, "csc": csc, "acot": acot, "asec": asec, "acsc": acsc,

    # Hyperbolic functions and inverses
    "sinh": sinh, "cosh": cosh, "tanh": tanh, "asinh": asinh, "acosh": acosh, "atanh": atanh,
    "coth": coth, "sech": sech, "csch": csch, "acoth": acoth, "asech": asech, "acsch": acsch
}
