# LZW-Compression-Decompression
The Lempel–Ziv–Welch (LZW) algorithm for Compression/Decompression
PROGRAM AND DATA STRUCTURE DESIGN
============================================================================================================================

The LZW Encoder/Decoder program consists of two files

     * Encoder.py   source code containing LZW encoding logic
     * Decoder.py   source code containing LZW decoding logic

@@@ Design of code - Encoding @@@


Encoder is the abstract class that contains a method compress that is overridden by the derived class LZW_Encoder.

The LZW_Encoder class has the following attributes:

    -max_tbl_size   maximum table size according to bit length
    -file_txt       contains text that is read from the file
                    which is the input for the encoder
    -dictionary     contains string to code mappings
                    and is populated with basic ascii codes
                    for each character before the encoding begins
    -result         a list to  hold the codes of the encoded
                    string pattern
Steps in Encoding

     1. Build dictionary with default ascii characters(0-255) with character as key and corresponding ascii value
     2. Set maximum size of dictionary based on the input bit length 
     3. Read the symbols from file and append them one by one to the current string
     5. check whether the resulting string has a code in the dictionary.
     6. If the resulting string does not exist in the dictionary, it means it has found a new string: it outputs the code 
        corresponding to the string without the newest symbol, adds the string concatenated with the newest symbol 
        (i.e., the new string) to the dictionary with its code(which is the previous largest code value incremented 
        by one), and resets the current string to the newest symbol.
     7. Thus the next time the LZW algorithm encounters a repeated string in the input sequence, it 
        will be encoded with a single number
     8. The algorithm continues to process symbols from the input sequence, building new strings until the 
        sequence is exhausted, and it then outputs the code for the remaining string


     
Data structure - Encoding

     *Dictionary is used for mapping strings to the code value as it can be easily accessed using keys and 
      its a dynamic data structure that grows with the size of the entries and so its space efficient.
     *List is also dynamic and is used to return code values after encoding and this can be easily iterated
      to write the resulting codes to file in binary format.
     *Strings are used for storing temporarary values and as keys to encoding table.

@@@ Design of code - Decoding @@@


Decoderis the abstract class that contains a method decompress that is overridden by the derived class LZW_Decoder.

The LZW_Decoder class has the following attributes:

        -max_tbl_size   maximum table size according to bit length
        -file_txt       contains binary contents that is read
                        using UTF-16BE encoding format
        -dictionary     contains code to string mappings
                        and is populated with basic ascii codes
                        for each character before the decoding begins
        -result         a list to  hold the decoded strings

Steps in Decoding

     1. Build dictionary with default ascii characters(0-255) with ascii code as key and the corresponding ascii character 
        as value.
     2. Set maximum size of dictionary based on the input bit length 
     3. Read an input code (integer) from the encoded sequence, look up the code in the dictionary by using 
        it as an index, and output the string associated with the code.
     5. Thereafter, the decoder reads in a new code, finds the new string indexed by this code, and outputs it.
     6. The first character of this new string is concatenated to the previously decoded string.This new concatenation 
        is added to the dictionary with an incremented code (simulating how the strings were added during compression)
     7. The decoded new string then becomes the previous string, and the process repeats.
     8. When the decoder receives a code that is not already in its dictionary, it can be shown that the new string 
        corresponding to this code consists of the previously decoded string with the first character of the previously 
        decoded string appended.
     9. Each time it reads in a code that does not exist in the dictionary, it must add the code and the corresponding 
        string to the dictionary.

Data structure - Decoding

     *Dictionary is used for mapping code to strings and its a dynamic data structure that grows with the 
      size of the entries and so its space efficient.
     *List is also dynamic and is used to return the decoded string.
     *Strings are used for storing temporarary values and are used as values for the keys(codes) in dictionary.

Files
=================================================================================================================================
* Encoder.py             source code containing LZW encoding logic
* Decoder.py             source code containing LZW decoding logic
* input1.txt             file containing sample input
* input1.lzw             file containing compressed output in binary format
* input1_decoded.txt     file containing decompressed output
* Project1.pdf           The project file with instructions for encoding/decoding tasks
* README.txt             The file that contains information about program and data structure design, encoding/decoding logic
                         and instructions on how to execute the source code.

Merits/Demerits of the program
=================================================================================================================================
* This Encoding/Decoding technique works on all ascii(extended) inputs.
* It is assumed that the input files are placed in the same folder as the source code.
* Encoding/Decoding works on input files containing single/multiple lines with multiple words.
* It has been programmed to accept fixed input bit length in the range 9 to 16. So, if the input length
  exceeds this range, the user is again prompted to enter input in the specified range.
* If empty file is given as input to encoder/decoder the user is prompted to enter non-empty file
  Example for encoder: input.txt
  Example for decoder :input.lzw
* It is assumed that the text file is given as input to encoder and binary file is given as input to decoder

Programming Language/ Pre Requisites
=================================================================================================================================
Programming Language:   Python

Pre Requisites:	        Python   - Version: 3.5.2 [This program does not work with python version 2]
			IDE used - Python's Integrated Development and Learning Environment(IDLE) - Version - 3.5.2
Usage Instructions
=================================================================================================================================
* Place the source code (.py files) and the input file in the same folder and open the command prompt(CMD)from that folder.

* Encoding/Compression: The Encoder.py file can be run from the command prompt from the folder where the files are placed using 
  the command: python <filename>.py <Input File Name>.txt <Bit Length>

  Example: python Encoder.py input.txt 12

  The Compressed Output file will be created in the same location as the input file with the name <Input File Name>.lzw in 
  16bit format(UTF-16BE encoding). 
  Example: input.lzw

* Decoding/Decompression: The Decoder.py file can be run from the command prompt from the folder where the files are placed using 
  the command: python <filename>.py <Input File Name>.lzw <Bit Length>

  Example: python Decoder.py input.lzw 12
  Here input.lzw contains encoded input in binary format, which is the input file for decoder.

  The Decoded Output file will be created in the same location as the input file with the name <Input File Name>_decoded.txt 
  Example: input_decoded.txt

***NOTE***

In Python 3, there's no difference between unicode and normal strings anymore. Only between unicode strings and binary data. So 
the developers finally removed the unichr function in favor of a common chr which now does what the old unichr did. There is no 
unichr function in python 3. See the documentation - https://docs.python.org/3.1/library/functions.html#chr
