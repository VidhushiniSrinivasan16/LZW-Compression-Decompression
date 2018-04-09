## NAME       : VIDHUSHINI SRINIVASAN
## STUDENT ID : 801029539
''' 
************************************************************************************************************************************************************************
@File          Decoder.py
 
@Title         Implementation of LZW Decoding/Decompressing Technique

@Author        VIDHUSHINI SRINIVASAN

@Created       03/01/2018

************************************************************************************************************************************************************************
'''
import sys
import numpy as np
import abc
from abc import ABC, abstractmethod

## Decoder is the abstract class with the abstract method - decompress

class Decoder(ABC):
    """ Super class Decoder"""
    
    @abstractmethod
    def decompress():
        pass

## LZW_Decoder is the derived class of Decoder and overrides decompress method that uses LZW
## decompression technique to decode strings
    
class LZW_Decoder(Decoder):
    """ 
        LZW_Decoder class 
        
        attributes
        ===========
        max_tbl_size   maximum table size according to bit length
        file_txt       contains binary contents that is read
                       using UTF-16BE encoding format
        dictionary     contains code to string mappings
                       and is populated with basic ascii codes
                       for each character before the decoding begins
        result         a list to  hold the decoded strings
    """
    # all the attributes to the decoder are initialized in this _init_ method
    def __init__(self,file_txt,bit_length):
        self.max_tbl_size=2 ** bit_length
        self.file_txt= file_txt
        self.dictionary=dict()
        self.dict_size=256
        self.result=[]
        
    # decompress method uses LZW decompression technique to decode strings
    def decompress(self):
        # table that contains basic ascii codes(0-255) and grows
        # according to strings in the file to be decoded
        self.dictionary= {i: chr(i) for i in range(self.dict_size)}
        # get the code from the first encoded sequence 
        code = ord(self.file_txt[0])
        # get the character corresponding to the code from the dictionary
        append_symbol=self.dictionary[code]
        self.result.append(append_symbol)
        for j in range(1,len(txt_from_file)):
            code = ord(self.file_txt[j])
            if code not in self.dictionary:
                new_string= append_symbol+append_symbol[0]
            else:
                new_string = self.dictionary[code]
            self.result.append(new_string)
            # Update dictionary.
            if len(self.dictionary) < self.max_tbl_size:
                    self.dictionary[self.dict_size] = append_symbol+new_string[0]
                    self.dict_size += 1
            append_symbol = new_string
        return self.result  # contains the list of decoded strings
                 

if __name__ == "__main__":
    print('@@@@@ LZW Decoding/Decompression @@@@@')
    input_file_name = sys.argv[1]   # get the input file name from command prompt
    bit_length = sys.argv[2]        # get the input bit length from the command prompt

    # get the correct bit length if not in specified range
    while ((int(bit_length) < 9) or (int(bit_length) > 16)):
             print ("The bit length should be in range 9 to 16")
             bit_length = input("Please enter the bit length again...")

    bit_len = int (bit_length)  	
    file_fp = open(input_file_name, 'r',encoding = 'UTF-16BE')           # open the file with UTF-16BE encoding to read the 16 bit binary input from the file
    txt_from_file = file_fp.read()

    # check if the input file is empty and if yes, prompt the user for non-empty file
    while not txt_from_file:
        print("File is Empty!!!")
        input_file_name = input("Please enter the non-empty input file name...")
        file_fp = open(input_file_name, 'r',encoding = 'UTF-16BE')  
        txt_from_file = file_fp.read()
        
    lzw_decoder= LZW_Decoder(txt_from_file,bit_len)                      # initialise LZW_Decoder by passing appropriate arguments
    result=lzw_decoder.decompress()                                      # get the decompressed result
    print("Decompressed Output :\n"+''.join(result))
    output_file_name = input_file_name.split(".")[0]+"_decoded"+".txt"   # create an output file with the same name as input file"_decoded" with extension .txt
    lzw_output = open(output_file_name,'w')                       	 # open file to write the decoded string
    lzw_output.write(''.join(result))                                    # write the decoded string to the file
    lzw_output.close()                            				
    file_fp.close()    
    print("The output is written to file: "+output_file_name)
'''
Note:
In Python 3, there's no difference between unicode and normal strings anymore. Only between unicode strings and binary data. So the developers finally removed
the unichr function in favor of a common chr which now does what the old unichr did. See the documentation - https://docs.python.org/3.1/library/functions.html#chr
'''
