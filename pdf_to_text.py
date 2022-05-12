import pdftotext
import os
from blinder.blinder import get_blinded_file
from Fonctions.hash  import encrypt_filename


def pdf_to_txt(dir_path: str, dir_path_dest: str):
    """Convert successively pdf into txt"""
    # Loop through all files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith(".pdf"):
            # Load the pdf and read it
            with open(dir_path+"/"+filename, "rb") as f:
                pdf = pdftotext.PDF(f)
            # Get the number of pages
            num_pages=len(pdf)
            # Copie le contenue du pdf dans un nouveau fichier txt
            if num_pages > 0:
                filename_txt=filename.replace(".pdf", ".txt")
                new_file=open(r"%s/%s"%(dir_path_dest, filename_txt), "a")
                new_file.writelines(pdf)
                new_file.close()
                get_blinded_file(new_file.name)
                crypted_filename = encrypt_filename(new_file.name)
                new_file_path = dir_path_dest+"/"+str(crypted_filename)
                os.rename(new_file.name, new_file_path)
                continue
        else:
            continue
