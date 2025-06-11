from Setup import *


def normalize(num):
    # if the decimal part is 0 then remove it and return it. if it is not, then just return it.
    if isinstance(num, float | int):
        if int(num) == num:
            return int(num)
        return num 

    if isinstance(num, str) and "." in num and ".0" not in num:
        return float(num)
    # if the string does not have a '.' or if it has a '.0' then it should be converted to int.
    else:
        # We need to convert to float first because python can't do int('1.0').
        return int(float(num))


def eq_solver(inp: str) -> None:
    def parse_expr_transformed(expr):
        return parse_expr(expr, transformations=transformations)


    equation = ""
    value = ""
    inp_without_sv = inp[3:]

    for char in inp_without_sv:
        if char == "=":
            break

        equation += char

    equation = equation.strip()
    equals_sign_idx = inp_without_sv.index("=")

    for char in inp_without_sv[equals_sign_idx + 1:]:
        value += char

    value = value.strip()
    eq = Eq(parse_expr_transformed(equation), parse_expr_transformed(value))
    solutions = solve(eq)

    print("Solutions:", end=" ")
    print(*solutions, sep=", ")


def set_var(inp: str) -> None:
    inp_without_vr = inp[3:]
    identifier: list[str] = []
    value: list[str] = []
    equals_sign_reached = False

    for char in inp_without_vr:
        if char == '=':
            equals_sign_reached = True
            continue
        
        if not equals_sign_reached:
            identifier.append(char)

        if equals_sign_reached:
            value.append(char)

    ide = "".join(identifier).strip()
    val = "".join(value).strip()
    is_not_valid_identifier = any(char not in allowed_ids for char in ide) or \
    ide[0] not in allowed_id_first_chars or (ide in ("e", "z"))

    if is_not_valid_identifier:
        print("Invalid identifier.")
        return
    
    if ide in variables.keys():
        print(f"Variable '{ide}' already exists.")
        return

    try:
        val = normalize(val)
    except ValueError:
        print("Invalid value.")
    else:
        variables[ide] = val
        print(f"{ide} = {val}")


def get_var(inp: str) -> None:
    identifier = inp[3:].strip()

    value = variables.get(identifier)

    if value is not None:
        print(value)
    else:
        print("Variable does not exist.")


def delete_var(inp: str) -> None:
    var = inp[3:].strip()
    try:
        del variables[var]
    except KeyError:
        print(f"Variable '{var}' does not exist.")
    else:
        print(f"Deleted variable '{var}'")


def evaluate_adv(inp: str) -> None:
    inp_without_ev = inp[3:].strip()

    expression = []

    if "to" not in inp_without_ev:
        expression = inp_without_ev
        digits = 8
    else:
        for idx, char in enumerate(inp_without_ev):
            if idx == inp_without_ev.index("to"):
                break
            expression.append(char)

        expression = "".join(expression).strip()
        digits = inp_without_ev[inp_without_ev.index("to") + 3:]

    try:
        digits = int(digits)
    except ValueError:
        print("Invalid amount of digits.")
    else:
        expr: Expr = parse_expr(expression, transformations=transformations, local_dict={**local_dict, **variables})
        result = float(expr.evalf(n=10000))  # type: ignore
        print(normalize(round(result, digits)))


def change_var(inp: str):
    inp_without_cg = inp[3:].strip()

    var = []

    for idx, char in enumerate(inp_without_cg):
        if idx == inp_without_cg.index("to"):
            break
        var.append(char)

    var = "".join(var).strip()

    if var not in variables.keys():
        print(f"Variable '{var}' does not exist.")
        return

    value = inp_without_cg[inp_without_cg.index("to") + 3:].strip()

    try:
        value = normalize(value)
    except ValueError:
        print("Invalid value.")
    else:
        variables[var] = value
        print(f"Variable '{var}' changed to {value}")


def derivative(inp: str) -> None:
    def split_tuple(input_tuple, chunk_size=5):
        return tuple(input_tuple[i:i+chunk_size] for i in range(0, len(input_tuple), chunk_size))


    inp_without_dv = inp[3:].strip()

    if "wr" not in inp:
        print(diff(parse_expr(inp_without_dv)))
    else:
        sym = symbols(inp_without_dv[inp_without_dv.index("wr") + 3:])

        if isinstance(sym, tuple):
            sym = split_tuple(sym)

            for tu in sym:
                expr = parse_expr(inp_without_dv[:inp_without_dv.index("wr")])
                res = tuple(f"d{symbol}: {diff(expr, symbol)}" for symbol in tu)
                print(", ".join(res))
        else:
            print(diff(parse_expr(inp_without_dv[:inp_without_dv.index("wr")]), sym))