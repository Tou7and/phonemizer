import os
import sys
from phonemizer import phonemize
from phonemizer.backend import EspeakBackend

backend = EspeakBackend('cmn')

def convert_textfile(text_path, output_dir):
    if os.path.isdir(output_dir) == False:
        os.makedirs(output_dir)

    with open(text_path, "r") as reader:
        text_ls = reader.readlines()

    phone_ls = []
    for text in text_ls:
        phonemized = backend.phonemize([text])
        phone_ls.append(phonemized[0]+"\n")

    print(phone_ls)
    output_path = os.path.join(output_dir, os.path.basename(text_path))
    with open(output_path, "w") as writer:
        writer.writelines(phone_ls)

if __name__ == "__main__":
    convert_textfile("data/input/xx.txt", "data/output")

