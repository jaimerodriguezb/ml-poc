
class Logic():

    def __init__(self):
        self.__model = None
        self.__load_model()

    def __load_model(self):
        """Load the model to self.__model once it's been trainned"""
        pass

    def logic_gate(self, a, b, operator):
        return self.__model.predict_proba(a, b, operator)

