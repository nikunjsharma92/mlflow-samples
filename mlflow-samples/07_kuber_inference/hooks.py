from kuberinference import pre_processing, post_processing

def input_fn(X):
    return pre_processing.pre_process(X)

def output_fn(Y):
    return post_processing.post_process(Y)
