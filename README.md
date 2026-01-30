# Seeds Soil Classification 🌾

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow 2.12](https://img.shields.io/badge/TensorFlow-2.12-orange.svg)](https://tensorflow.org/)
[![Flask 2.3](https://img.shields.io/badge/Flask-2.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Maintained? yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MahmouddSalama/seeds/graphs/commit-activity)

**Empowering agriculture with AI-driven soil identification and expert crop recommendations.**

---

## 📺 Demo & Visuals

Experience the system in action through our project walkthroughs:

| Demo 1 | Demo 2 | Demo 3 |
| :---: | :---: | :---: |
| ![Seeds Demo 1](https://raw.githubusercontent.com/MahmouddSalama/seeds/main/videos/seeds1.mp4) | ![Seeds Demo 2](https://raw.githubusercontent.com/MahmouddSalama/seeds/main/videos/seeds2.mp4) | ![Seeds Demo 3](https://raw.githubusercontent.com/MahmouddSalama/seeds/main/videos/seeds3.mp4) |

> [!NOTE]
> If the videos do not play directly in your browser, you can find them in the `videos/` directory of the repository.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Soil Classification Guide](#-soil-classification-guide)
- [Development](#-development)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Contact & Support](#-contact--support)
- [Acknowledgments](#-acknowledgments)

---

## 📖 About the Project

**Seeds Soil Classification** is an end-to-end AI solution designed to bridge the gap between complex machine learning models and practical agricultural application. By leveraging deep learning (Transfer Learning with VGG16), the system accurately classifies different soil types from images and provides tailored recommendations for crops and nutrient management.

### Why this project?
Traditional soil testing can be slow and expensive. This project provides an accessible, instant alternative that helps farmers and agricultural researchers make informed decisions about planting and soil health.

### Key Features
- 🧠 **Deep Learning Core**: Utilizes a fine-tuned VGG16 architecture for high-accuracy soil classification.
- 🚀 **RESTful API**: A lightweight Flask-based API for seamless integration with mobile or web applications.
- 📊 **Comprehensive Recommendations**: Provides detailed insights into soil formation, nutrient content, and optimal crops.
- 🖼️ **Image Processing**: Robust pipeline using OpenCV for real-time image resizing and normalization.
- 📂 **Structured Data**: Built-in support for multiple soil types including Black, Cinder, Laterite, Peat, and Yellow soil.

### Use Cases
- **Precision Agriculture**: Real-time soil assessment in the field.
- **Educational Tools**: Helping students identify soil types and their properties.
- **Agricultural Research**: Rapid data collection and categorization for soil studies.

---

## 🛠️ Tech Stack

### AI & Data Science
- **TensorFlow / Keras**: Model training and inference.
- **TensorFlow Hub**: Pre-trained model integration.
- **OpenCV**: Image preprocessing and manipulation.
- **NumPy & Matplotlib**: Data handling and visualization.
- **Joblib**: Efficient model and label serialization.

### Backend
- **Flask**: Web framework for the classification API.
- **Python**: Core programming language.

### Infrastructure
- **Git/GitHub**: Version control and documentation.

---

## 📂 Project Structure

```text
seeds/
├── AI/                     # Core AI Development
│   ├── api/                # Flask API Implementation
│   │   ├── app.py          # Main Flask Application
│   │   ├── load_model.py   # Model loading & inference logic
│   │   └── images/         # Temporary storage for uploaded images
│   ├── data/               # Dataset directory (local only)
│   ├── training_2/         # Model training artifacts
│   ├── v1.ipynb            # Initial experimentation notebook
│   └── v2.ipynb            # Refined model training notebook
├── videos/                 # Project demonstration videos
├── requirements.txt        # Python dependency manifest
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # MIT License details
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.9+**
- **pip** (Python package manager)
- **Virtual Environment** (Recommended: `venv` or `conda`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MahmouddSalama/seeds.git
   cd seeds
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Starting the API Server
Navigate to the API directory and run the Flask application:
```bash
cd AI/api
python app.py
```
The server will start at `http://127.0.0.1:5000/`.

### Classifying an Image
You can send a POST request with an image file to the `/uploader` endpoint:

**Using cURL:**
```bash
curl -X POST -F "file=@/path/to/your/soil_image.jpg" http://127.0.0.1:5000/uploader
```

**JSON Response Example:**
```json
{
  "name": "Black Soil",
  "info": {
    "Formation": "Formed from weathered basalt",
    "Nutrient Content": "Rich in calcium, potassium, and magnesium",
    "Common Crops": ["Cotton", "Wheat", "Millet"],
    "Regions Found": "Deccan Plateau, parts of India"
  }
}
```

---

## 🌱 Soil Classification Guide

Our model is trained to recognize the following soil types:

| Soil Type | Primary Characteristics | Best Crops |
| :--- | :--- | :--- |
| **Black Soil** | Rich in calcium/magnesium, dark color | Cotton, Wheat, Millet |
| **Laterite Soil** | Reddish, rich in iron/aluminum | Tea, Coffee, Rubber |
| **Peat Soil** | High organic matter, waterlogged | Rice, Cranberries |
| **Yellow Soil** | Yellow-brown, moderate nutrients | Cereals, Fruits |
| **Cinder Soil** | Volcanic, porous, poor nutrients | Pineapple, Grapes |

---

## 🧪 Development

### Running Notebooks
To explore the model training process:
1. Install `jupyter` or `notebook`.
2. Open `AI/v2.ipynb` to see the VGG16 implementation and evaluation.

### Code Quality
- **Linting**: We recommend using `flake8` for Python code quality.
- **Formatting**: Use `black` for consistent code formatting.

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

## 🗺️ Roadmap
- [ ] Mobile application integration (Flutter/React Native).
- [ ] Support for more soil types and plant diseases.
- [ ] Real-time satellite data integration.
- [ ] Multilingual support for agricultural recommendations.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact & Support
**Mahmoud Salama**
- GitHub: [@MahmouddSalama](https://github.com/MahmouddSalama)
- Project Link: [https://github.com/MahmouddSalama/seeds](https://github.com/MahmouddSalama/seeds)

---

## ✨ Acknowledgments
- [TensorFlow VGG16 Documentation](https://www.tensorflow.org/api_docs/python/tf/keras/applications/vgg16)
- [Flask Framework](https://flask.palletsprojects.com/)
- All contributors who help improve this project!
