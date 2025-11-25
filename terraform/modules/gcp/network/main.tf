resource "google_compute_network" "main" {
  name                    = var.name
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "private" {
  name          = var.subnet-name
  ip_cidr_range = var.cidr-range
  region        = var.region
  network       = google_compute_network.main.id
}