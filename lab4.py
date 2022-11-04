import os
import queue


# 1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
# dat ca parametru.

def f1(dir_path):
    result = set()

    with os.scandir(dir_path) as entries:
        for entry in entries:
            if entry.is_file():
                result.add(os.path.splitext(entry.name)[-1][1:])

    print(result)


# f1("E:")


# 2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută
# a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

def f2(dir_path, file_path):
    with open(file_path, 'w') as f:
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_file():
                    f.write(entry.name + '\n')


# f2("E:", "D:\lab4.txt")


# 3)	Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier,
# iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv)
# din directorul dat ca parametru.

def f3(path):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            f.seek(0, os.SEEK_END)
            f.seek(f.tell() - 20, 0)
            print(f.read(20))
    else:
        result_dict = dict()
        result = list()
        my_queue = list()

        my_queue.append(path)

        while len(my_queue) > 0:
            working_path = my_queue.pop()
            with os.scandir(working_path) as entries:
                for entry in entries:
                    if entry.is_dir():
                        my_queue.append(os.path.join(working_path, entry.name))
                    else:
                        extension = os.path.splitext(entry.name)[-1][1:]
                        if extension in result_dict:
                            result_dict[extension] = result_dict[extension] + 1
                        else:
                            result_dict[extension] = 1

        for (key, value) in result_dict.items():
            result.append((value, key))

        result.sort(key=lambda a: a[0], reverse=True)

        print(result)


# f3("D:\lab4.txt")
# f3("D:/lab4")


# 4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument
# la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.


def f4():
    path = str(input("Please enter a valid dir_path\n"))

    if not os.path.isdir(path):
        print("This is not a valid dir_path\n")
        return
    else:
        unique_set = set()
        multiple_set = set()
        with os.scandir(path) as entries:
            for entry in entries:
                if os.path.isfile(os.path.join(path, entry.name)):
                    extension = os.path.splitext(entry.name)[-1][1:]
                    if extension not in unique_set and extension not in multiple_set:
                        unique_set.add(extension)
                    elif extension in unique_set:
                        unique_set.remove(extension)
                        multiple_set.add(extension)

        result = [a for a in unique_set]
        result.sort()

        print(result)


# f4()
# D:/lab4/a/1

# 7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer
# si returnează un dicționar cu următoarele cămpuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.

def f7(path):
    result = dict()

    result["full_path"] = path
    result["file_size"] = os.stat(path).st_size
    result["file_extension"] = os.path.splitext(path)[-1][1:]
    result["can_read"] = os.access(path, os.R_OK)
    result["can_write"] = os.access(path, os.W_OK)

    print(result)


# f7("D:\\lab4\\b\\file.txt")


# 8)	Să se scrie o funcție ce primește un parametru cu numele dir_path.
# Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

def f8(path):
    result = list()

    with os.scandir(path) as entries:
        for entry in entries:
            if os.path.isfile(os.path.join(path, entry.name)):
                result.append(os.path.join(path, entry.name))

    print(result)

# f8("D:\\lab4\\a\\1")
