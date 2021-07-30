# For sample predict functions for popular libraries visit https://github.com/opendatahub-io/odh-prediction-samples

# Import libraries
# import tensorflow as tf
import logging

logging.basicConfig(level=logging.INFO)
# Load your model.
# model_dir = 'models/myfancymodel'
# saved_model = tf.saved_model.load(model_dir)
# predictor = saved_model.signatures['default']


# Write a predict function 
def predict(args_dict):
    logging.info(f'args_dict: {args_dict}')
    arg = args_dict.get('arg1')
    # predictor(arg)
    return {'arg1': arg}

#
# Test
#
# curl -X POST -H "Content-Type: application/json" --data '{"arg1": "hello world"}' http://<hostname>/predictions
#
