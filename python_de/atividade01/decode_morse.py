import os
import sys
import datetime
import pandas as pd
from config import file_path, dict_morse
from console_art import art

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços e palavras separadas por dois espaços
    output : mensagem decodificada
    '''
    words = msg.split("  ")
    decoded_words = []
    for word in words:
        letters = word.split(" ")
        decoded_word = "".join([dict_morse[letter] for letter in letters])
        decoded_words.append(decoded_word)
        result = " ".join(decoded_words)
    print(f"MENSAGEM DECODIFICADA ----> {result}")
    return result

def save_clear_msg_csv_hdr(msg):
    '''
    input : resultado da decodificação
    output : palavra escrita em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode="a", index=False, header=hdr)

if __name__ == "__main__":
    print('=========================================================')
    print(art)
    print('=========================================================')
    print('INSIRA O CÓDIGO RECEBIDO:')
    decode_msg = decode_morse(input())
    save_clear_msg_csv_hdr(decode_msg)