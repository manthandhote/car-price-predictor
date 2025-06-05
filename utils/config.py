from torchvision import transforms  # Add this import at the top

# Configuration constants
CLASS_NAMES = ['Damage', 'Whole']

# Image transformations
TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                        [0.229, 0.224, 0.225])
])

# Model paths
MODEL_PATHS = {
    'regression': 'models/model.pkl',
    'damage': 'models/car_damage_model.pth'
}