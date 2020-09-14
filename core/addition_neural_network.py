'''
Created on 08-Apr-2020

@author: Deepak Shajan
'''

import tensorflow.keras as keras
from dataprovider import addition_data_provider as provider

__TRAINING_COUNT        = 500000
__VALIDATION_COUNT      = 500000
  
__TESTING_COUNT         = 500000
  
__EPOCHS                = 5000
__BATCH_SIZE            = 5000

 
__model = None
 
MAX_INPUT_BIT_SIZE    = 8


def get_neural_network_model():
    
    global __model
    
    if __model is not None:
        return __model
    else:
        _load_neural_network_model_from_file()
        if __model is not None:
            return __model
        else:
            _create_neural_network_model()
            _train_neural_network()
            _test_neural_network()
            _save_neural_network_model_to_file()
            
    return __model


def _create_neural_network_model():
    
    print('Creating neural network from scratch...')
    global __model
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(512, input_dim=2*MAX_INPUT_BIT_SIZE, activation='sigmoid'))
    model.add(keras.layers.Dense(512, activation='sigmoid'))
    model.add(keras.layers.Dense(512, activation='sigmoid'))
    model.add(keras.layers.Dense(MAX_INPUT_BIT_SIZE+1,  activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='RMSprop', metrics=['accuracy'])
    __model = model
    print(model.summary())
    return __model


def _save_neural_network_model_to_file():
    
    print('Saving neural network to file...')
    global __model
    __model.save("TrainedNeuralNetworkModel.h5")
    
    
def _load_neural_network_model_from_file():
    
    print('Loading neural network model from file...')
    global __model
    try:
        __model = keras.models.load_model("TrainedNeuralNetworkModel.h5")
    except:
        print('Could not load saved neural network model from file...')
    else:
        print(__model.summary())
    return __model
    
    
def _train_neural_network():
    
    global __model
    training_data = provider.get_training_data(__TRAINING_COUNT,MAX_INPUT_BIT_SIZE)
    input_training_data = training_data[0]
    output_training_data = training_data[1]
    validation_data = provider.get_validation_data(__VALIDATION_COUNT,MAX_INPUT_BIT_SIZE)
#     callback = keras.callbacks.EarlyStopping(monitor='accuracy', min_delta=0.0001, patience=500, restore_best_weights=True)
    
#     print('data -> {}'.format(training_data))
#     print('full input -> {}'.format(input_training_data))
#     print('full output -> {}'.format(output_training_data))
    print('sample input -> {}'.format(input_training_data[0]))
    print('sample output-> {}'.format(output_training_data[0]))

    get_neural_network_model()
    history = __model.fit(input_training_data, output_training_data, validation_data=validation_data, epochs=__EPOCHS, batch_size=__BATCH_SIZE)
    print('Training history -> {}'.format(history.history))
    return history 


def _test_neural_network():
    
    global __model
    testing_data = provider.get_testing_data(__TESTING_COUNT, MAX_INPUT_BIT_SIZE)
    input_testing_data = testing_data[0]
    output_testing_data = testing_data[1]
    
    history = __model.fit(input_testing_data, output_testing_data, epochs=1, batch_size=__BATCH_SIZE, verbose=0)
    print('Testing history -> {}'.format(history.history))
    return history 
        
        
        
        
        
        
        
        
        