# 🛡️ Network Security System

### Phishing & Malicious URL Detection using Machine Learning

An end-to-end **Machine Learning-based Network Security System** that detects potentially malicious or phishing-related network/URL activity using security-related URL features — built as a production-style, modular ML pipeline rather than a single notebook.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Prediction%20API-009688?logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Data%20Source-47A248?logo=mongodb&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2?logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECR%20%2B%20CI%2FCD-FF9900?logo=amazonaws&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [ML Pipeline](#️-ml-pipeline)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Dataset Features](#-dataset-features)
- [FastAPI Application](#-fastapi-application)
- [Docker](#-docker)
- [Installation](#️-installation)
- [Environment Variables](#-environment-variables)
- [Running the Pipeline & API](#️-run-the-training-pipeline)
- [CI/CD](#️-cicd)
- [Project Structure](#-project-structure)
- [Technologies Used](#️-technologies-used)
- [Key Learning Outcomes](#-key-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📌 Project Overview

Cybersecurity systems need to identify suspicious network activity and potentially malicious URLs efficiently. This project uses Machine Learning classification algorithms to analyze URL and network-security-related features and predict whether a given activity is legitimate or potentially malicious.

The system follows a **modular ML pipeline** — separated into ingestion, validation, transformation, training, tracking, and serving stages — making it easier to maintain, test, deploy, and extend compared to a single Jupyter Notebook.

---

## 🎯 Objectives

- Build an end-to-end Machine Learning pipeline for network security
- Ingest training data from MongoDB
- Validate incoming datasets and detect dataset drift
- Handle missing values using KNN Imputation
- Train and compare multiple classification algorithms
- Select the best-performing model automatically
- Track experiments using MLflow and DagsHub
- Expose the trained model through a FastAPI application
- Containerize the application using Docker
- Automate build and deployment using GitHub Actions and AWS services

---

## 🏗️ ML Pipeline

```text
                    ┌─────────────────┐
                    │    MongoDB      │
                    │   Data Source   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data Ingestion  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data Validation │
                    │ + Drift Check   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data            │
                    │ Transformation  │
                    │ KNN Imputation  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Model Training  │
                    └────────┬────────┘
                             │
             ┌───────────────┼────────────────┐
             ▼               ▼                ▼
       Random Forest    Decision Tree    Gradient Boosting
       Logistic Reg.    AdaBoost
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Best Model      │
                    │ Selection       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ MLflow /        │
                    │ DagsHub         │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ FastAPI         │
                    │ Prediction API  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Prediction      │
                    │ Output          │
                    └─────────────────┘
```

---

## 🔄 Machine Learning Workflow

### 1. Data Ingestion
Training data is retrieved from **MongoDB** and converted into a Pandas DataFrame. The ingestion component:
- Reads the MongoDB collection
- Removes MongoDB `_id` values
- Handles `"na"` values
- Stores the dataset in the feature store
- Splits the dataset into training and testing sets

### 2. Data Validation
The validation stage checks whether the incoming dataset follows the expected schema. It performs:
- Column-count validation
- Dataset consistency checks
- Dataset drift detection using the **Kolmogorov-Smirnov two-sample test (`ks_2samp`)**

A drift report is generated during validation.

### 3. Data Transformation
Missing values are handled using **KNN Imputation** through a Scikit-learn Pipeline. The preprocessing object is fitted on the training data and applied to both training and testing data, then saved for future inference.

### 4. Model Training
The system trains and evaluates multiple classification algorithms:

| Model | Purpose |
|---|---|
| Random Forest | Ensemble-based classification |
| Decision Tree | Tree-based classification |
| Gradient Boosting | Boosting-based classification |
| Logistic Regression | Linear classification baseline |
| AdaBoost | Adaptive boosting classification |

The system compares the trained models and automatically selects the model with the highest evaluation score.

### 5. Experiment Tracking
The project integrates **MLflow** and **DagsHub** for experiment tracking. Metrics tracked include:
- F1 Score
- Precision
- Recall

The trained model is also logged through MLflow.

---

## 📊 Dataset Features

The dataset contains security-related URL/network features such as:

`having_IP_Address`, `URL_Length`, `Shortining_Service`, `having_At_Symbol`, `double_slash_redirecting`, `Prefix_Suffix`, `having_Sub_Domain`, `SSLfinal_State`, `Domain_registeration_length`, `Favicon`, `port`, `HTTPS_token`, `Request_URL`, `URL_of_Anchor`, `Links_in_tags`, `SFH`, `Submitting_to_email`, `Abnormal_URL`, `Redirect`, `on_mouseover`, `RightClick`, `popUpWidnow`, `Iframe`, `age_of_domain`, `DNSRecord`, `web_traffic`, `Page_Rank`, `Google_Index`, `Links_pointing_to_page`, `Statistical_report`

**Target column:** `Result`

The project schema defines these fields as numerical features for the ML pipeline.

---

## 🚀 FastAPI Application

The trained model is exposed through a **FastAPI application**.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Redirects to the FastAPI documentation |
| `GET` | `/train` | Starts the training pipeline |
| `POST` | `/predict` | Accepts a CSV file and generates predictions using the trained model |

The prediction result is added to the dataset and displayed through the application.

---

## 🐳 Docker

The application is containerized using **Docker** (Python 3.10 base image), with dependencies installed from `requirements.txt`.

```bash
# Build the image
docker build -t network-security-system .

# Run the container
docker run -p 8000:8000 network-security-system
```

Then open: `http://localhost:8000/docs`

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/Aswinsurya-sivakumar/network_security_system.git

# 2. Move into the project
cd network_security_system

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the environment
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
MONGO_DB_URL=your_mongodb_connection_string
MONGODB_URL_KEY=your_mongodb_connection_string
```

If you're using AWS or DagsHub integrations, configure the required credentials through environment variables or GitHub Secrets.

> ⚠️ **Never commit passwords, API keys, MongoDB credentials, AWS credentials, or other secrets to GitHub.**

---

## ▶️ Run the Training Pipeline

```bash
python main.py
```

The pipeline performs:

```text
Data Ingestion → Data Validation → Data Transformation → Model Training
```

Generated artifacts — transformed datasets, preprocessing objects, trained models, logs, and prediction outputs — are stored automatically.

---

## 🌐 Run the API

```bash
python app.py
```

- Application: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`

---

## ☁️ CI/CD

A GitHub Actions workflow automates the deployment process:

```text
Git Push → GitHub Actions → Continuous Integration → Docker Image Build → Amazon ECR → Deployment Environment → Running Container
```

AWS credentials and deployment configuration are handled through **GitHub Secrets**. The workflow builds and pushes the Docker image to **Amazon Elastic Container Registry (ECR)** and then runs the container in the deployment environment.

---

## 📁 Project Structure

```text
network_security_system/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── Artifacts/
├── Network_Data/
│
├── data_schema/
│   └── schema.yaml
│
├── final_model/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── logs/
├── mlruns/
│
├── networksecurity/
│   ├── cloud/
│   ├── components/
│   ├── constant/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
│
├── prediction_output/
├── templates/
├── valid_data/
│
├── .gitignore
├── Dockerfile
├── app.py
├── main.py
├── push_data.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| **Programming** | Python |
| **Data Science & ML** | Pandas, NumPy, Scikit-learn |
| **Database** | MongoDB, PyMongo |
| **API** | FastAPI, Uvicorn |
| **MLOps** | MLflow, DagsHub |
| **DevOps & Deployment** | Docker, GitHub Actions, AWS ECR, AWS |
| **Development Tools** | Git, GitHub, VS Code |

**Main dependencies:** `pandas`, `numpy`, `pymongo`, `certifi`, `scikit-learn`, `mlflow`, `dagshub`, `fastapi`, `uvicorn`, `python-multipart`, `python-dotenv`

---

## 💡 Key Learning Outcomes

Through this project, I gained hands-on experience with:

- End-to-end ML pipeline development and modular project architecture
- MongoDB data integration, validation, and dataset drift detection
- Missing-value handling and model comparison
- Classification metrics and MLflow / DagsHub experiment tracking
- FastAPI model serving and Docker containerization
- GitHub Actions CI/CD and AWS-based deployment
- Production-oriented ML project structure

---

## 🔮 Future Improvements

- Real-time URL analysis
- Advanced feature engineering
- Explainable AI using SHAP
- Model monitoring and automated retraining
- Real-time threat monitoring dashboard
- Improved API security and authentication
- Cloud-native deployment
- More advanced anomaly-detection techniques

---

## 👨‍💻 Author

**Aswin Surya**
Machine Learning & Data Science Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-Aswinsurya--sivakumar-181717?logo=github)](https://github.com/Aswinsurya-sivakumar)

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

**Repository:** https://github.com/Aswinsurya-sivakumar/network_security_system

---

## 📄 License

This project is intended for educational and development purposes.
