#main function
# from blinder.blinder import get_blinded_file 
# from blinder.data_loader import load_data
# from blinder.str_func import create_all_cases  
# from Data import local_data as data
from pdf_to_text import pdf_to_txt 


pdf_to_txt("./documents_sample", "./documents_sample")
# load_data("/home/peter/etna/oceanet_cv_blinder/Data/patronymes.csv",0,data.data_to_blind)
# data.data_to_blind = create_all_cases(data.data_to_blind)
# load_data("/home/peter/etna/oceanet_cv_blinder/Data/prenom.csv",0,data.data_to_blind)
# data.data_to_blind = create_all_cases(data.data_to_blind)

