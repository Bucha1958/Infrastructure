# Kubernetes Project

This repository contains a Kubernetes project that demonstrates the deployment of MongoDB and Mongo Express using Kubernetes. 

## Project Structure

- `mongodb-deployment.yaml`: Kubernetes Deployment and Service definitions for MongoDB.
- `mongo-express-deployment.yaml`: Kubernetes Deployment and Service definitions for Mongo Express.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Setup

### 1. Start Minikube

Start your Minikube cluster with the recommended resources:

```sh
minikube start --memory=2048mb --cpus=2

