# GKE Cluster Deployment with Microservices

This Terraform script automates the deployment of a Google Kubernetes Engine (GKE) cluster on Google Cloud Platform (GCP) and the subsequent deployment of a microservices application within the cluster.

## Prerequisites

Before running this script, ensure you have the following:

- A Google Cloud Platform (GCP) account.
- A service account JSON key file for authentication (e.g., `gke-1-432911-a6ca7309eef8.json`).
- Terraform installed on your local machine.
- `kubectl` and `gcloud` CLI tools installed for interacting with GKE.

## Resources Created

### Google Compute Network

- **VPC Network**: A Virtual Private Cloud (VPC) named `stanley-network` is created. This network does not auto-create subnetworks.
  
- **Subnetwork**: A subnetwork named `test-subnetwork` is created within the `stanley-network` VPC. The subnetwork is allocated an IP range of `10.2.0.0/16`. Additionally, two secondary IP ranges are defined:
  - `gke-pods-range`: `10.3.0.0/16`
  - `gke-services-range`: `10.4.0.0/20`

### Google Kubernetes Engine (GKE) Cluster

- **GKE Cluster**: A GKE cluster named `my-gke-cluster` is deployed in the `us-central1` region, within the `stanley-network` VPC and `test-subnetwork`. The cluster is configured with:
  - **Node Configuration**: Nodes of type `e2-medium`, which have 2 vCPUs and 4 GB of memory.
  - **OAuth Scopes**: Nodes are granted full access to all Google Cloud services (`https://www.googleapis.com/auth/cloud-platform`).
  - **IP Allocation**: The cluster is configured with IP aliasing, utilizing the `gke-pods-range` for pods and `gke-services-range` for services.

### Deployment of Microservices

- **Namespace Creation and Microservices Deployment**: After the GKE cluster is successfully created, a namespace named `microservices` is created, and the microservices defined in the `config.yaml` file are deployed within this namespace.

## Outputs

- **Cluster Name**: The name of the GKE cluster (`my-gke-cluster`).
- **Cluster Endpoint**: The endpoint to access the GKE cluster.
- **Cluster CA Certificate**: The cluster's CA certificate to authenticate access.

## Usage

### Step 1: Set Up Your Environment

1. Clone the repository containing this Terraform script.
2. Ensure your GCP service account credentials JSON file (e.g., `gke-1-432911-a6ca7309eef8.json`) is accessible from the Terraform directory.

### Step 2: Initialize Terraform

```bash
terraform init
