# Output of network resources

output "subnetwork-id" {
    description = "ID"
    value       = google_compute_network.main.id
}

output "subnetwork-cidr" {
    description = "subnetwork cidr range"
    value       = google_compute_network.main.ip_cidr_range
}