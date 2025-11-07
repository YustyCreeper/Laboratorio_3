# FastAPI CI/CD Example

This project showcases a complete CI/CD pipeline for a FastAPI application, integrating the following features:

- ✅ Pre-commit hooks
- ✅ Unit testing with pytest
- ✅ Docker build
- ✅ Docker push to Docker Hub

---

## 🚀 Steps to Run

### 1. Clone the repo

```bash
git clone https://github.com/CloudComputingUAO/fastapi-ci-cd-example.git
cd fastapi-ci-cd-example
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Pre-commit

```bash
pip install pre-commit
pre-commit install
```

### 4. Run the app locally

```bash
uvicorn app.main:app --reload
```

### 5. Run tests

```bash
pytest
```

---

## 🐳 Docker

### Build Docker image

```bash
docker build -t yourusername/ci-cd-demo .
```

### Run the container

```bash
docker run -p 8000:8000 yourusername/ci-cd-demo
```

---

## 🤖 GitHub Actions CI/CD

### Create these secrets in GitHub:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
