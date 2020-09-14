'''
Created on 10-Apr-2020

@author: Deepak Shajan
'''
from core import addition_neural_network as network
from util import addition_util as util

def add(first_number, second_number):
    
    model = network.get_neural_network_model()
    
    input_as_binary_array_concat = util.convert_to_binary_array_by_concat(first_number, second_number, network.MAX_INPUT_BIT_SIZE)
    
    output_as_approximate_binary_array = model.predict([input_as_binary_array_concat])
#     print('inputs -> ({},{})'.format(first_number, second_number))
#     print('approximate binary output array -> {}'.format(output_as_approximate_binary_array))
    output_as_binary_array = util.convert_to_binary_array(output_as_approximate_binary_array[0])
#     print('binary output array -> {}'.format(output_as_binary_array))

    output_as_decimal = util.convert_binary_array_to_decimal(output_as_binary_array)
    print('{} + {} = {}'.format(first_number,second_number,output_as_decimal))
    