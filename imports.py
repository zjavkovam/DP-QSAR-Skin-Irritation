# RDKit
from rdkit import Chem
from rdkit.Chem import AllChem, Draw, Descriptors, MACCSkeys
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.ML.Descriptors import MoleculeDescriptors

# Data manipulation
import pandas as pd
import numpy as np
from collections import Counter
import json

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Statistical tests
from scipy.stats import skew, kurtosis, shapiro, uniform

# Machine learning - scikit-learn
from sklearn.pipeline import Pipeline
from sklearn.model_selection import (
    train_test_split, GridSearchCV, RandomizedSearchCV,
    StratifiedKFold, cross_val_score, learning_curve
)
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    precision_score, recall_score, f1_score,
    roc_curve, auc, log_loss, roc_auc_score
)
from sklearn.preprocessing import (
    MinMaxScaler, FunctionTransformer, LabelEncoder,
    PowerTransformer, QuantileTransformer
)
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.base import BaseEstimator, ClassifierMixin, clone
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA, KernelPCA
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# XGBoost
import xgboost as xgb
from xgboost import XGBClassifier

# SHAP
import shap

# Optuna
import optuna

# Persistence
import joblib
