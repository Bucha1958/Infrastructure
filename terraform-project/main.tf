provider "google" {
  credentials = file("mike-428601-d729f858f0af.json")
  project     = "mike-428601"
  region      = "us-central1"
}

resource "google_compute_network" "vpc_network" {
  name                    = "mike-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "my_subnet" {
    name                = "test-subnetwork"
    network            = google_compute_network.vpc_network.id
    ip_cidr_range       = "10.2.0.0/16"
    region   = "us-central1"
}