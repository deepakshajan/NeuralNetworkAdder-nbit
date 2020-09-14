'''
Created on 08-Apr-2020

@author: Deepak Shajan
'''
from random import randint
from util import addition_util as util
import math

def get_training_data(count, max_bit_size):
    
    data = [[],[]]
    input_data = []
    output_data = []
    
    max_limit = math.pow(2, max_bit_size)-1
    for _ in range(count):
        first_input  = randint(0, max_limit)
        second_input = randint(0, max_limit)
        output_value = first_input + second_input
        input_binary64 = util.convert_to_binary_array_by_concat(first_input, second_input, max_bit_size)
        output_binary64 = util.convert_to_binary__array(output_value, max_bit_size)
        input_data.append(input_binary64)
        output_data.append(output_binary64)
        
#         print('x1->{}->{}'.format(first_input, input_binary64))
#         print('x1->{}->{}'.format(second_input, input_binary64))
#         print('y->{}->{}'.format(output_value, output_binary64))
    
    data[0] = input_data    
    data[1] = output_data
    
    return data

def get_validation_data(count, max_bit_size):
    return get_training_data(count, max_bit_size)

def get_testing_data(count, max_bit_size):
    return get_training_data(count, max_bit_size)


    