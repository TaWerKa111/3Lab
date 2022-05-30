TASK = """
        Смоделировать работу кэш-памяти. 

        На вход подается адрес памяти. 
        На выходе должна быть представлена строка кэш-памяти. 

"""
from typing import List
from prettytable import PrettyTable


# Constants
MAX_VALUE = '163398'
MIN_VALUE = '000000'

BASE = 16

def print_result(bin_adr: List, bin_tag: List, hex_tag: List, adr: str):
    address_tab = PrettyTable()

    address_tab.add_column("Адрес ОП", list(adr))
    address_tab.add_column("Адрес в двоичной форме", bin_adr)

    
    print(address_tab)

    tag_tab = PrettyTable()
    
    tag_tab.add_column("Тег", bin_tag)
    tag_tab.add_column("16 запись", hex_tag)


    print(tag_tab)



def get_cache_str(adr: str):
    """
    

    """
    bin_tag = []
    hex_tag = []
    bin_adr = []
    new_bin_tag = []

    for char in adr:
        bin_str = f"{bin(int(char, BASE))[2:]:0>4}"
        bin_adr.append(bin_str)
        for chars in zip(bin_str[0::2], bin_str[1::2]):
            bin_tag.append(f"{chars[0]}{chars[-1]}")

    hex_tag.append(hex(int(bin_tag[0], 2))[2:])
    new_bin_tag.append(bin_tag[0])

    for ind in range(1, len(bin_tag)-2, 2):
        bin_numb = bin_tag[ind] + bin_tag[ind+1]
        new_bin_tag.append(bin_numb)
        hex_tag.append(hex(int(bin_numb, 2))[2:])

    # print_result(
    #     bin_adr, 
    #     bin_tag=new_bin_tag,
    #     hex_tag=hex_tag,
    #     adr=adr
    # )

    print(f"{'Двоичная запись строки кеша:'.rjust(40)}{''.join(bin_tag):>40}")
    print(f"{'Строка кеша:'.rjust(40)}{''.join(hex_tag).upper():>40}")

def convert_adr(adr: str) -> str:
    """
    Конвертация адреса ОП в строке кэш памяти.

    @param adr: str, адрес ОП в шестнадцатиричной формате
    """
    try:
        hex_str = int(adr, BASE)
        # print(hex_str)

        if hex_str < int(MIN_VALUE, BASE) or hex_str > int(MAX_VALUE, BASE):
            raise Exception(f"Число не входит в адресный диапозон: {MIN_VALUE} и {MAX_VALUE}")

        get_cache_str(adr)


    except TypeError:
        raise Exception("Должно быть число")
    


def main():
    """
    Основная функция, в которой происходит получение числа и 
    его отпарвка дальше, а также обработка исключений.
    """
    print(
        f"""
        
        Задание: {TASK} 
        Адресный диапазон {MIN_VALUE} - {MAX_VALUE} 
        """
    )
    while True:
        addres = input("Введите адрес ОП: ")
        
        if addres == 'exit':
            print('Goobbye!')
            break

        try:
            convert_adr(addres)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    main()
