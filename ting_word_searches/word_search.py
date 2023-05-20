from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    response = []
    crr_value = instance.head_value
    while (crr_value):
        ocurrences = []
        print(crr_value.value["linhas_do_arquivo"])

        for i in range(len(crr_value.value["linhas_do_arquivo"])):
            line = crr_value.value["linhas_do_arquivo"][i]
            if (word.lower() in line.lower()):
                ocurrences.append({"linha": i + 1})

        if (len(ocurrences)):
            response.append({
                "palavra": word,
                "arquivo": crr_value.value["nome_do_arquivo"],
                "ocorrencias": ocurrences
            })
        crr_value = crr_value.next
    return response


def search_by_word(word: str, instance: Queue):
    response = []
    crr_value = instance.head_value
    while (crr_value):
        ocurrences = []
        print(crr_value.value["linhas_do_arquivo"])

        for i in range(len(crr_value.value["linhas_do_arquivo"])):
            line = crr_value.value["linhas_do_arquivo"][i]
            if (word.lower() in line.lower()):
                ocurrences.append({
                    "linha": i + 1,
                    "conteudo": line
                    })

        if (len(ocurrences)):
            response.append({
                "palavra": word,
                "arquivo": crr_value.value["nome_do_arquivo"],
                "ocorrencias": ocurrences
            })
        crr_value = crr_value.next
    return response
