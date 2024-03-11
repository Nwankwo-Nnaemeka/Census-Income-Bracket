import income_constant
import tensorflow as tf
import tensorflow_transform as tft

# Unpack the contents of the constants module
_NUMERIC_FEATURE_KEYS = income_constant.NUMERIC_FEATURE_KEYS
_CATEGORICAL_FEATURE_KEYS = income_constant.CATEGORICAL_FEATURE_KEYS
_BUCKET_FEATURE_KEYS = income_constant.BUCKET_FEATURE_KEYS
_FEATURE_BUCKET_COUNT = income_constant.FEATURE_BUCKET_COUNT
_LABEL_KEY = income_constant.LABEL_KEY
_transformed_name = income_constant.transformed_name

def preprocessing_fn(inputs):
    """Preprocess input columns into transformed columns.
    Args: 
        inputs (): 

    Return:
        dictionary
        
    """
    outputs = {}
    # Scale these fatures to be [0,1]
    for key in _NUMERIC_FEATURE_KEYS:
        outputs[_transformed_name(key)] = tft.scale_to_0_1(inputs[key])

    for key in _CATEGORICAL_FEATURE_KEYS:
        outputs[_transformed_name(key)] = tft.compute_and_apply_vocabulary(inputs[key])

    for key in _BUCKET_FEATURE_KEYS:
        outputs[_transformed_name(key)] = tft.bucketize(inputs[key], _FEATURE_BUCKET_COUNT[key])


    outputs[_transformed_name(_LABEL_KEY)] = tft.compute_and_apply_vocabulary(inputs[_LABEL_KEY])
    
    
    return outputs
