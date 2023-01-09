import pickle
pickle_out = open("stacked_model.pkl", "wb")
pickle.dump(gbc, pickle_out)
pickle_out.close()
