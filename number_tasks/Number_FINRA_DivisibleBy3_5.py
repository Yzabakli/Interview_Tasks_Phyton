def _f_i_n_r_a():
    for i in range(1, 31):

        if i % 5 == 0 and i % 3 == 0:

            print("FINRA")

        elif i % 5 == 0:

            print("RA")

        elif i % 3 == 0:

            print("FIN")

        else:
            print(i)


_f_i_n_r_a()
