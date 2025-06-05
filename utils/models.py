import pickle as pk
import torch
import torch.nn as nn
from torchvision import models
from .config import MODEL_PATHS

def load_regression_model():
    """Load the regression model"""
    return pk.load(open(MODEL_PATHS['regression'], 'rb'))

def load_damage_model():
    """Load the damage classification model"""
    damage_model = models.resnet18(weights=None)
    damage_model.fc = nn.Linear(damage_model.fc.in_features, 2)
    damage_model.load_state_dict(torch.load(
        MODEL_PATHS['damage'], 
        map_location=torch.device('cpu')
    ))  # Fixed: Added missing parenthesis
    damage_model.eval()
    return damage_model