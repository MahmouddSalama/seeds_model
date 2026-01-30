from tensorflow.keras.models import Sequential, model_from_json
import tensorflow_hub as hub
from tensorflow.keras.optimizers import RMSprop
import cv2
import matplotlib.pylab as plt
import numpy as np
import joblib
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten
from tensorflow.keras.applications import VGG16


def load_model():
    input_shape = (224, 224, 3)  

    base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
    inputs = Input(shape=input_shape)
    x = base_model(inputs)
    x = Flatten()(x)
    x = Dense(512, activation='relu')(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(100, activation='relu')(x)
    outputs = Dense(5, activation='softmax')(x)
    model = Model(inputs=inputs, outputs=outputs)
    model.load_weights('mdoel.ckpt')
    return model

model=load_model()
le=joblib.load("labels")

def pip_line(image_path):
    image=cv2.imread(str(image_path))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageee=cv2.resize(image,(224,224))
    imageee=imageee/255.0
    plt.imshow(imageee)
    res= model.predict(np.array([imageee]))
    return le.classes_[np.argmax(res)] 




soil_comparison = {
    "Black Soil": {
        "Formation": "Formed from weathered basalt",
        "Nutrient Content": "Rich in calcium, potassium, and magnesium",
        "Water Retention": "High, retains moisture well",
        "Common Crops": ["Cotton", "Wheat", "Millet"],
        "Color": "Black or dark gray",
        "Regions Found": "Deccan Plateau, parts of India"
    },
    "Cinder Soil": {
        "Formation": "Derived from volcanic cinders",
        "Nutrient Content": "Poor in nutrients, low fertility",
        "Water Retention": "Good drainage, low water retention",
        "Common Crops": ["Pineapple", "Grapes"],
        "Color": "Dark, porous",
        "Regions Found": "Areas near volcanic regions"
    },
    "Laterite Soil": {
        "Formation": "Forms in tropical regions with heavy rainfall",
        "Nutrient Content": "Rich in iron and aluminum oxides",
        "Water Retention": "Low to moderate",
        "Common Crops": ["Tea", "Coffee", "Rubber"],
        "Color": "Red or reddish-brown",
        "Regions Found": "Tropical regions, India, Africa"
    },
    "Peat Soil": {
        "Formation": "Formed from decomposed organic matter",
        "Nutrient Content": "High in organic material, low in minerals",
        "Water Retention": "Very high, retains a lot of moisture",
        "Common Crops": ["Rice", "Cranberries", "Turf"],
        "Color": "Dark brown or black",
        "Regions Found": "Waterlogged areas, swamps, bogs"
    },
    "Yellow Soil": {
        "Formation": "Formed by weathering of rocks",
        "Nutrient Content": "Moderate, rich in iron oxides",
        "Water Retention": "Moderate",
        "Common Crops": ["Cereals", "Fruits", "Olives"],
        "Color": "Yellow or yellowish-brown",
        "Regions Found": "Mediterranean regions, China"
    }
}

# Example: Accessing information about Black Soil
print(soil_comparison["Black Soil"])

