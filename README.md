# Cyber Incident Monitoring System

## Project Overview

The **Cyber Incident Monitoring System** is a comprehensive tool designed to provide real-time feeds of cyber incidents occurring in the cyber space within the Indian region. This tool aggregates data from various sources, including social media (e.g., Twitter), news websites, and other relevant feeds. It leverages machine learning to classify incidents and generates reports to help stakeholders understand the nature and frequency of cyber incidents in real-time. 

This project consists of a full-stack application with a backend that handles data collection, processing, and storage, as well as a frontend that presents data in an interactive and user-friendly interface.

---

## Features

- **Real-time Incident Collection**: Scrapes data from sources such as Twitter and news websites.
- **Incident Classification**: Uses a machine learning model to classify cyber incidents.
- **Visualization Dashboard**: Provides a frontend dashboard for visualizing and interacting with the data.
- **API Access**: Offers a REST API for accessing incident data and reports.
- **Configurable and Scalable**: Supports configurations for deployment in different environments.



---

## Technologies Used

### Frontend
- **React**: For building the user interface.
- **CSS & Bootstrap**: For styling and responsive design.

### Backend
- **Flask**: API server for handling requests.
- **BeautifulSoup and Tweepy**: For web scraping and social media data collection.
- **MongoDB / PostgreSQL**: For data storage.
- **Celery and Airflow**: For scheduling and orchestrating data ingestion tasks.

### Machine Learning
- **scikit-learn**: For building and training classification models.
- **Pandas & NumPy**: For data processing.
- **Pickle**: For saving and loading models.

### Deployment
- **Docker**: Containerization for consistent deployment.
- **Kubernetes**: For managing containerized applications (if needed).
- **NGINX**: As a reverse proxy for the backend.
- **AWS/GCP**: Cloud deployment and storage.

---

## System Architecture

The project follows a microservices-based architecture, with each major component isolated for better scalability and maintainability. Here’s a quick overview:

1. **Frontend**: A React-based web application that connects to the backend API to display incidents data in real-time.
2. **Backend**: A Flask server that provides API endpoints for data ingestion, processing, and retrieval.
3. **Data Pipeline**: A data pipeline that collects data from sources such as Twitter and news websites, processes it, and stores it in the database.
4. **Machine Learning**: A trained model to classify incident types and severity based on historical data.
5. **Database**: A MongoDB/PostgreSQL database that stores raw and processed incident data.

---

## Setup Instructions

### Prerequisites

- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) (for frontend)
- [Python 3.7+](https://www.python.org/)
- [Docker](https://www.docker.com/) (for containerization)
- Cloud provider account (optional, for deployment)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/cyber_incident_monitoring.git
   cd cyber_incident_monitoring
   ```

2. **Setup Backend**:

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Setup Frontend**:

   ```bash
   cd ../frontend
   npm install
   ```

4. **Configure Environment Variables**:
   
   ```bash
   # Copy the example environment file
   cp .env.example .env
   ```
   
   Then edit `.env` and configure:
   - Database credentials (username, password, host)
   - Secret keys
   - API keys (Twitter, News API, etc.)
   
   **Important**: The `.env` file stores **sensitive credentials** and should never be committed to version control.

5. **Run Backend**:

   ```bash
   cd backend
   python app.py
   ```

6. **Run Frontend**:

   ```bash
   cd ../frontend
   npm start
   ```

7. **Database Setup**:
   - Initialize the database by running `init_db.py` script from the `database/` directory.

8. **Run Data Pipeline**:
   - Start the data ingestion and processing pipeline using Airflow or Celery, as configured in the `data_pipeline/` folder.

---

## Configuration Guide

### Understanding `.env` vs `config/*.yaml`

The project uses two types of configuration files that work together:

#### `.env` File (Sensitive Credentials)
- **Purpose**: Stores **sensitive information** like passwords, API keys, and secrets
- **Location**: Root directory (`.env`)
- **Version Control**: **Never committed** to Git (listed in `.gitignore`)
- **Usage**: Required for local development and deployment
- **Example**: `.env.example` provides a template

**Contains**:
- Database credentials (username, password)
- API keys (Twitter, News API, etc.)
- Secret keys for encryption
- Service tokens

#### `config/*.yaml` Files (Non-Sensitive Settings)
- **Purpose**: Stores **non-sensitive** application settings per environment
- **Location**: `config/development.yaml` and `config/production.yaml`
- **Version Control**: **Safe to commit** (no secrets)
- **Usage**: Optional for basic local development, useful for advanced deployment

**Contains**:
- Application settings (debug mode, host, port)
- Logging configuration
- Feature flags
- Performance tuning parameters
- References to environment variables (e.g., `${DATABASE_URI}`)

### Quick Start for Local Development

For basic local development, you only need to:

1. Copy `.env.example` to `.env`
2. Fill in your database credentials and API keys in `.env`
3. Run the application

The `config/*.yaml` files are **optional** for local development. They become important when:
- Deploying to multiple environments (dev, staging, production)
- Using Docker or Kubernetes
- Need environment-specific configurations
- Working in a team with different setups

### Environment-Specific Configuration

**Development** (`config/development.yaml`):
- Debug mode enabled
- Verbose logging
- SQLite or local PostgreSQL
- CORS enabled for local frontend

**Production** (`config/production.yaml`):
- Debug mode disabled
- Minimal logging
- Production database with connection pooling
- Security hardening
- Performance optimizations

---

## Usage

### Access the Web Application

Once the frontend and backend servers are running, open [http://localhost:3000](http://localhost:3000) in your browser to access the web application.

### Running the Data Pipeline

To collect and process real-time data:

```bash
python data_pipeline/jobs/ingest_data.py
```

### Access API Endpoints

The backend provides several API endpoints:

- **`GET /api/incidents`**: Retrieve a list of cyber incidents.
- **`POST /api/incidents`**: Add a new cyber incident (for testing).
- **`GET /api/incidents/<id>`**: Retrieve details of a specific incident.

---

## API Endpoints

Here are some core API endpoints for interacting with the backend.

1. **Get All Incidents**:
   ```http
   GET /api/incidents
   ```

2. **Get Incident by ID**:
   ```http
   GET /api/incidents/<id>
   ```

3. **Add Incident** (for testing purposes):
   ```http
   POST /api/incidents
   ```

---

## Deployment

### Docker Compose (Local)

You can deploy the whole stack using Docker Compose for local testing:

```bash
docker-compose up --build
```

### Cloud Deployment (AWS/GCP)

1. **Build Docker Image**:
   ```bash
   docker build -t your-image-name .
   ```

2. **Push to Container Registry**:
   ```bash
   docker push your-image-name
   ```

3. **Deploy to Kubernetes**:
   - Use the Kubernetes manifests in the `deployment/k8s/` folder to deploy on a Kubernetes cluster.

---

## License

Content protected. Unauthorized use prohibited without explicit permission. Reach out for permissions before sharing or adapting this work .

project owner
rajeevsharmamachphy@gmail.com
anchalverma31296@gmail.com

---
