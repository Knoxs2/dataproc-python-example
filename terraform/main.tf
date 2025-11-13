resource "google_storage_bucket" "data_bucket" {
    name = "${var.project_id}-data-bucket"
    location = var.region
}

resource "google_dataproc_cluster" "spark_cluster" {
    name = "spark-cluster"
    region = var.region

    cluster_config {
        master_config {
            num_instances = 1
            machine_type = "n1-standard-2"
        }

        worker_config {
            num_instances = 2
            machine_type = "n1-standard-2"
        }

        software_config {
            image_version = "2.0-debian10"
        }
    }
}