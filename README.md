# AI Inference Platform

This repository contains the source code and configuration for the AI Inference Platform.

## Structure

- `docs/`: Architecture and design documentation.
- `inference-service/`: Source code for the inference service (FastAPI).
- `k8s/`: Kubernetes manifests for deployment.

## Getting Started

1.  **Build Docker Image**:
    ```bash
    cd inference-service
    docker build -t inference-service:latest .
    ```

2.  **Deploy to Kubernetes**:
    ```bash
    kubectl apply -f k8s/
    ```

## Documentation

See the `docs/` directory for more details on architecture and scaling strategies.
