print("Text Analizer")


def word_list(text):
    """Esta funcion divide el texto (text) en una lista de palabras manteniendo el orden"""
    list = text.split(' ')
    filtered_list = [] 
    # for item in list:
    #     if item: 
    #         filtered_list.append(item)
    filtered_list = [item for item in list if item]

    return filtered_list


def unique_words(text):
    # David Jimenez
    """Crea un set que incluye únicamente una ocurrencia de cada palabra"""
    pass


def word_frequency(text):
    # Sergio Torres
    """Retorna un diccionario con las palabras y su frecuencia en el texto"""
    pass

def longer_word(text):
    # Noemí
    palabras = text.split()  
    longer_word = palabras[0]  
    for palabra in palabras:
        if len(palabra) > len(longer_word):
            longer_word = palabra
    return longer_word


texto = "Me llamo Noemí y vivo en Huesca"
print("La palabra más larga es:", longer_word(texto))

def shorter_word(text):
    #Noemí
    palabras = text.split()  
    shorter_word = palabras[0]  
    for palabra in palabras:
        if len(palabra) < len(shorter_word):
            shorter_word = palabra
    return shorter_word


texto = "Me llamo Noemí y vivo en Huesca"
print("La palabra más corta es:", shorter_word(texto))

def word_filter(words, filter_words):
    # Ruben
    """Return  the words list filtered by filter_words"""
    pass

def char_counter(text):
    #Jahn
    """Return the quantity of chars in the text excluding special 
    charts like ',','.','(',')' and spaces"""
    pass

def filter_by_word_length(text,l):
    #Juan Antonio
    """Return the list of words with lenght over than l"""
    pass

def count_by_lenght(text, l):
    # Dani Gonzalez
    """Return a dict with lengths and quantities of words with this lenghts"""
    pass




if __name__ == "__main__":
    print("==Test Text Analizer==")
    print(word_list("Hola  que tal"))
    # print(len(word_list("Hola que tal")))

    assert len(word_list("Hola que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert len(word_list("Hola  que tal")) == 3, "word_list failed and not returned the required quantity of words..."
    assert word_list("Hola que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."
    assert word_list("Hola  que tal") == ['Hola','que','tal'], "word_list failed and not returned the required list of words..."

    #Angel -> Escribir los asserts de validar todas las funciones anteriores
    
    print("Todo OK")