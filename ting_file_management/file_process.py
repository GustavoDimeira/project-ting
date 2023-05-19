import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def already_in(path_file: str, instance: Queue):
    crr_value = instance.head_value
    while (crr_value):
        if (path_file == crr_value.value["nome_do_arquivo"]):
            return True
        crr_value = crr_value.next
    return False


def process(path_file: str, instance: Queue):
    lines = txt_importer(path_file)

    if (not already_in(path_file, instance)):
        new_content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
        instance.enqueue(new_content)

        return sys.stdout.write(str(new_content))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
