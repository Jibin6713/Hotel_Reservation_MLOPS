# Hotel Reservation Cancellation Prediction (MLOps Project)

This project is an end-to-end machine learning pipeline for predicting hotel reservation cancellations. It covers data ingestion, preprocessing, model training, evaluation, deployment with Flask, containerization with Docker, and CI/CD automation using Jenkins and Google Cloud.

---

## 🚀 Features

- **Data Ingestion**: Downloads data from Google Cloud Storage.
- **Data Processing**: Cleans, transforms, and splits data.
- **Model Training**: Trains a LightGBM model and evaluates performance.
- **Experiment Tracking**: Uses MLflow for logging metrics and artifacts.
- **Web App**: Flask-based UI for making predictions.
- **Containerization**: Docker support for easy deployment.
- **CI/CD**: Jenkins pipeline for automated build, test, and deploy.
- **Cloud Deployment**: Ready for Google Cloud Run.

---

## 🗂️ Project Structure

```
Hotel_Reservation/
│
├── config/                # Configuration files (YAML)
├── custom_jenkins/        # Jenkins Docker setup
├── mlruns/                # MLflow runs (ignored in .gitignore)
├── pipeline/              # Training pipeline scripts
├── src/                   # Source code (data ingestion, training, etc.)
├── static/                # Static files for Flask app (CSS)
├── templates/             # HTML templates for Flask app
├── logs/                  # Log files (ignored in .gitignore)
├── application.py         # Flask web application
├── Dockerfile             # Dockerfile for app containerization
├── requirements.txt       # Python dependencies
├── setup.py               # Package setup
└── README.md              # Project documentation
```

---

### MLOps Workflow
-**Database Setup**: Upload dataset to Google Cloud Storage bucket.
-**Project Setup**: Virtual environment, logging, exception handling, folder structure.
-**Data Ingestion**: Download dataset, train-test split.
-**Notebook Prototyping**: Exploratory data analysis, feature selection, modeling.
-**Reusable Code**: Modular scripts for preprocessing, ingestion, training.
-**Experiment Tracking**: MLflow for model metrics, artifacts.
-**Training Pipeline**: End-to-end automation script.
-**App Building**: Flask UI for user-friendly interaction.
-**CI/CD Pipeline**: Jenkins + Docker + GCR + Cloud Run for automated deployment

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Hotel_Reservation_MLOPS.git
cd Hotel_Reservation_MLOPS
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Start the Flask Web App

```bash
python application.py
```
- The app will be available at [http://localhost:8080](http://localhost:8080)

---

## 🐳 Docker Usage

### Build and Run the Docker Container

```bash
docker build -t hotel-reservation-app .
docker run -p 8080:8080 hotel-reservation-app
```

---

## 🧪 Example Usage

- Open the web app in your browser.
- Enter reservation details in the form.
- Submit to see if the reservation is likely to be canceled.

---

## 🛠️ CI/CD & Cloud Deployment

- Jenkins pipeline and Dockerfile for automated build and deployment.
- Ready for deployment to Google Cloud Run (see `custom_jenkins/` and pipeline scripts).

---

## 📊 Technologies Used

- Python, Flask, LightGBM, Pandas, Scikit-learn
- MLflow
- Docker
- Jenkins
- Google Cloud Platform (Cloud Storage, Cloud Run)

---



## 🙋‍♂️ Contact

Github: [Github](https://github.com/Jibin6713)
