import sys
from math import floor, log

def natural_to_bit_string(n):
    """ converts natural number into bit string"""

    try:
       n = int(n)
    except: 
       print "Error in natural_to_bit_string: '%s' is not a number." %(n)
       sys.exit(1) 

    if n != int(n):
       print "Error in natural_to_bit_string: '%s' is not a natural number." %(n)
       sys.exit(1) 

    if n < 0:
       print "Error in natural_to_bit_string: '%d' is negative." %(n)
       sys.exit(1) 

    bit_list = []

    k = int(n)
    while k != 0:
          bit_list.insert(0,int(k % 2))
          k = floor(k/2)

    bit_string = ""
 
    for elem in bit_list:
        bit_string += repr(elem)

    return bit_string


def real_to_bit_string(x, precision):
    """ converts real number into bit string via floating point number"""
    
    try:
       x = float(x)
    except: 
       print "Error in real_to_bit_string: '%s' is not a number." %(x)
       sys.exit(1) 

    if precision not in ["single","double"]:
       print "Error in real_to_bit_string: '%s' is not a valid precision. Only 'single' and 'double'." %(precision)
       sys.exit(1) 

    # floating point number representation of x

    # exponent
    e = int(floor(log(abs(x))/log(2.)))
    print "e = ", e
    # bias
    if precision == "single":
       B = 127
       number_of_mantisse_bits = 23
    else: # double
       B =  1023
       number_of_mantisse_bits = 52
    E = e + B
    E_binary = natural_to_bit_string(E)

    # mantisse
    a = int((abs(x)/pow(2,e)-1.)*pow(2,number_of_mantisse_bits)) 
    print "a = ", a

    # sign bit
    if x >= 0:
       sign = "0"
    else:
       sign = "1"
    bit_string = sign + " "

    a_binary = natural_to_bit_string(a)
    # fill up mantisse with zeros at the beginning!
    zeros = ""
    for i in range(number_of_mantisse_bits-len(a_binary)):
        zeros += "0"
    bit_string += E_binary + " " + zeros + a_binary

    #print "Laenge des Exponenten:", len(E_binary), "bit"
    #print "Laenge der Mantisse:", len(zeros) + len(m_binary), "bit"

    return bit_string

def compare_bit_strings(bit_string1, bit_string2):
    """ detects the differences between two bit strings """

    if len(bit_string1) != len(bit_string2):
       print "ERROR in compare_bit_strings: Length of the bit strings differ. Cannot compare!"
       print "Length of bit string 1 = ", len(bit_string1), ", Length of bit string 2 = ", len(bit_string2)
       sys.exit(1)

    number_of_different_bits = 0
    difference_positions = []
    bit_counter = -1 # spaces should not be counted!
    for i in range(len(bit_string1)):
        if bit_string1[i] != " ":
           bit_counter += 1
        if bit_string1[i] != bit_string2[i]:
           number_of_different_bits += 1
           difference_positions.append(bit_counter)

    print "Number of different bits = ", number_of_different_bits
    print "Positions of different bits: "
    for elem in difference_positions:
        print elem,

x = 26.9

precision = "single"

#args = sys.argv

#try:
#	x = args[1]
#except:
#	print "ERROR: You must indicate the number you want to convert!"
#        sys.exit(1)

#try:
#	precision = args[2]
#except:
#	print "ERROR: You must indicate your desired precision!"
#	sys.exit(1)

bit_string = real_to_bit_string(x, precision)

print x, " = ", bit_string


    


















    

    
