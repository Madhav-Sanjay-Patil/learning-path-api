# Personalized Learning Path API

A modular Flask-based backend service that provides personalized topic recommendations to learners based on their progress and topic prerequisites.

---

## Features

- Modular Flask application using Blueprints
- SQLAlchemy integration with SQLite
- Learner progress tracking with statuses like "Completed", "In Progress", etc.
- Prerequisite-aware topic recommendation logic

---

## Project Structure

```

project/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── extensions.py
├── seed.py
├── requirements.txt
├── run.py
└── README.md

````

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Seed the database with initial data

```bash
python seed.py
```

### 5. Start the Flask development server

```bash
python run.py
```

---

## API Endpoint

### Get eligible topics for a learner

```
GET /eligible-topics/<learner_id>
```

**Description**: Returns a list of topics the learner is eligible to study based on their current progress and the prerequisite structure.

---

## API Documentation

Interactive Swagger docs available at: `/apidocs`

Powered by [Flasgger](https://github.com/flasgger/flasgger)


## License

This project is licensed under the MIT License.

```

