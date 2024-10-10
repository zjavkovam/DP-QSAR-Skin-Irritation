
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Descriptors, MACCSkeys
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem import Draw

#from mordred import Calculator, descriptors

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split

import xsmiles
import json
import shap


def open_file(path):
    df = pd.read_excel(path)
    return df

def main():
    file_path = 'udataset.xlsx'

    df = open_file(file_path)
    print(df.head())