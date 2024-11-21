import pickle

def trigger_deserialization(serialized_input):
    return pickle.loads(serialized_input)
