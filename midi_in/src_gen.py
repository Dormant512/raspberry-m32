map_dict = {
        41: "a",
        42: "q",
        43: "s",
        44: "w",
        72: " "
        }


def nk(key, dict=map_dict):
    """Takes dict key, returns NOTE ON XX... TYPE X string."""
    return f'\t\t"Note on {key}" ) xdotool type {dict[key]} ;; \n'


if __name__ == "__main__":

    with open("midi2keys.sh", "w") as f:
        L_0 = [
                '#!/bin/bash \n',
                'aseqdump -p "KOMPLETE KONTROL M32" | while IFS=" ," read src ev1 ev2 ch label1 data1 label2 data2 rest; do \n',
                '\tcase "$ev1 $ev2 $data1" in \n'
                ]

        L_1 = [
                '\tesac \n',
                'done\n'
                ]


        f.writelines(L_0)
        for key in map_dict:
            f.write(nk(key))
        f.writelines(L_1)
