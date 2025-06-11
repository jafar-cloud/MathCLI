# v 1.1.0
import readline
from Functions import *


while True:
    user_inp = input(">>> ")

    if user_inp.startswith("ev"):
        user_inp_without_ev = user_inp[3:].strip()

        try:
            print(normalize(eval(user_inp_without_ev, {**allowed, **variables})))
        except Exception as e:
            try:
                evaluate_adv(user_inp)
            except Exception as e:
                print(e)

    elif user_inp.startswith("sv"):
        eq_solver(user_inp)

    elif user_inp.startswith("vr"):
        set_var(user_inp)

    elif user_inp.startswith("gt"):
        get_var(user_inp)

    elif user_inp.startswith("dl"):
        delete_var(user_inp) 

    elif user_inp.startswith("cg"):
        change_var(user_inp)

    elif user_inp.startswith("dv"):
        derivative(user_inp)

    elif user_inp in ("ex", "br"):
        print("Thanks for using MathCLI!")
        break
