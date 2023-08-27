import pandas as pd
import joblib
import os

class Logic():

    def __init__(self):
        self.__model = None
        self.__load_model()

    def __load_model(self):
        """Load the model to self.__model once it's been trainned"""
        self.__model = joblib.load(os.path.dirname(__file__) + '\\training\\logic_gates_model.pkl') 

    def logic_gate(self, a, b, operator):
        input_df = pd.DataFrame({
            "a":[a],
            "b":[b],
            "gate_and":[int(operator == "and")],
            "gate_nand":[int(operator == "nand")],
            "gate_nor":[int(operator == "nor")],
            "gate_or":[int(operator == "or")],
            "gate_xor":[int(operator == "xor")]
        })

        return int(self.__model.predict_proba(input_df)[0,1])
