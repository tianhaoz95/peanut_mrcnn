def keras_model_fn(hyperparameters):
    compiled_model = None
    return compiled_model

def train_input_fn(training_dir, hyperparameters):
    # Logic to the following:
    # 1. Reads the **training** dataset files located in training_dir
    # 2. Preprocess the dataset
    # 3. Return 1)  a dict of feature names to Tensors with
    # the corresponding feature data, and 2) a Tensor containing labels
    return features, labels

def eval_input_fn(training_dir, hyperparameters):
    # Logic to the following:
    # 1. Reads the **evaluation** dataset files located in training_dir
    # 2. Preprocess the dataset
    # 3. Return 1)  a dict of feature names to Tensors with
    # the corresponding feature data, and 2) a Tensor containing labels
    return features, labels

def serving_input_fn(hyperparameters):
    # Logic to the following:
    # 1. Defines placeholders that TensorFlow serving will feed with inference requests
    # 2. Preprocess input data
    # 3. Returns a tf.estimator.export.ServingInputReceiver or tf.estimator.export.TensorServingInputReceiver,
    # which packages the placeholders and the resulting feature Tensors together.
