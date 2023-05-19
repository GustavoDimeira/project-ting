import sys


def format_lines(lines):
    list_lines = []
    for line in lines:
        list_lines.append(line.split("\n")[0])
    return list_lines


def txt_importer(path_file):
    try:
        if (not path_file.endswith("txt")):
            raise NameError
        with open(path_file, "r") as file:
            return format_lines(file.readlines())
    except FileNotFoundError:
        msg = f"Arquivo {path_file} não encontrado"
        print(msg, file=sys.stderr)
    except NameError:
        print("Formato inválido", file=sys.stderr)
