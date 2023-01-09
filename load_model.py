
model = None

def load_model():
    global model
    # model variable refers to the global variable
    with open('stacked_model.pkl', 'rb') as f:
        model = pickle.load(f)
