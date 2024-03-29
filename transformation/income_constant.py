# Features with string data types that will be converted to indices
CATEGORICAL_FEATURE_KEYS = [
    'education', 'marital_status', 'occupation', 'race', 'relationship', 'workclass', 'sex', 'native_country'
]

# Numerical features that are marked as continuous
NUMERIC_FEATURE_KEYS = ['fnlwgt', 
                        'education_num',
                        'capital_gain', 'capital_loss', 'hours_per_week'
                       ]

# Feature that can be grouped into buckets
BUCKET_FEATURE_KEYS = ['age']

# Number of buckets used by tf.transform for encoding each bucket feature.
FEATURE_BUCKET_COUNT = {'age': 4}

# Feature that the model will predict
LABEL_KEY = 'income'

# Utility function for renaming the feature
def transformed_name(key):
    return key + '_xf'
