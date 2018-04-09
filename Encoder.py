
''' 
***********************************************************************************************************************************************************************
@File          Encoder.py
 
@Title         Implementation of LZW Encoding/Compressing Technique

@Author        VIDHUSHINI SRINIVASAN

@Created       03/01/2018

***********************************************************************************************************************************************************************
'''
import sys
import numpy as np
import abc
from abc import ABC, abstractmethod


## Encoder is the abstract class with the abstract method - compress


class Encoder(ABC):
    """ Super class Encoder"""
    ## abstract method that should be overrided by the derived class
    @abstractmethod
    def compress():
        pass

## LZW_Encoder is the derived class of Encoder and overrides compress method that uses LZW
## compression technique to compress strings

class LZW_Encoder(Encoder):
    '''
    LZW_Encoder class 
            
    attributes
    ===========
    max_tbl_size   maximum table size according to bit length
    file_txt       contains text that is read from the file
                   which is the input for the encoder
    dictionary     contains string to code mappings
                   and is populated with basic ascii codes
                   for each character before the encoding begins
    result         a list to  hold the codes of the encoded
                   string pattern
    '''    
    
     
    # all the attributes to the encoder are initialized in this _init_ method
    def __init__(self,file_txt,bit_length):
        self.max_tbl_size=2 ** bit_length
        self.file_txt= file_txt
        self.dictionary=dict()
        self.dict_size=256
        self.result=[]

    # compress method uses LZW compression technique to encode strings
    def compress(self):
        
        # Encoding table that contains basic ascii codes(0-255) and grows
        # according to strings in file with manipulated codes
        self.dictionary= {chr(i): i for i in range(self.dict_size)}
        append_symbol=""
        for SYMBOL in self.file_txt:
            new_string = append_symbol + SYMBOL
            if new_string in self.dictionary:
                append_symbol = new_string
            else:
                self.result.append(self.dictionary[append_symbol])
                # Add new_string to the dictionary.
                if len(self.dictionary) < self.max_tbl_size:
                    self.dictionary[new_string] = self.dict_size
                    self.dict_size += 1
                append_symbol = SYMBOL
        if append_symbol:
            self.result.append(self.dictionary[append_symbol])
        return self.result    # return the list of codes for encoded string
                 

if __name__ == "__main__":
    print('@@@@@ LZW Encoding/Compression @@@@@')
    input_file_name = sys.argv[1]  # get the input file name from command prompt
    bit_length = sys.argv[2]       # get the input bit length from the command prompt

    # get the correct bit length if not in specified range
    while ((int(bit_length) < 9) or (int(bit_length) > 16)):
             print ("The bit length should be in range 9 to 16")
             bit_length = input("Please enter the bit length again...")

    bit_len = int (bit_length) 	
    file_fp = open(input_file_name, 'r')
    txt_from_file = file_fp.read()
    
    # check if the input file is empty and if yes, prompt the user for non-empty file
    while not txt_from_file:
        print("File is Empty!!!")
        input_file_name = input("Please enter the non-empty input file name...")
        file_fp = open(input_file_name, 'r')
        txt_from_file = file_fp.read()
        
    #print('\nInput is:\n'+ txt_from_file)
    lzw= LZW_Encoder(txt_from_file,bit_len)   # initialise LZW_Encoder by passing appropriate arguments
    result=lzw.compress()                     # get the compressed result
    #print(lzw.dictionary["ab"])
    print("Codes :\t"+str(result))
    
    output_binary=""
    
    for SYMBOL in result:
        output_binary+=chr(SYMBOL)          # In python 2, chr function should be replaced by unichr function, to be converted to unicode
                                            # before encoding using UTF-16BE. Here, python 3 is used, where chr function treats normal
                                            # and unicode strings in a similar way as opposed to python 2. Please read the note below.
                                            
    output_file_name = input_file_name.split(".")[0]+".lzw"           # create an output file with the same name as input file with the extension .lzw
    lzw_output = open(output_file_name,'wb')                          # open file in binary mode to write in binary format
    lzw_output.write(output_binary.encode("UTF-16BE"))                # UTF-16BE is used to encode in 16 bit format to the output file
    lzw_output.close()                                                
    file_fp.close()
    print("The output is written in binary format to file: "+output_file_name)

'''
Note:
In Python 3, there's no difference between unicode and normal strings anymore. Only between unicode strings and binary data. So the developers finally removed
the unichr function in favor of a common chr which now does what the old unichr did. See the documentation - https://docs.python.org/3.1/library/functions.html#chr
'''
