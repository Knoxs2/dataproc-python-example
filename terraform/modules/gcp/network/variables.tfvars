variable "name" {
    description = "name of the VPC network"
    type = string
}

variable "subnet-name" {
    description = "name of the VPC subnetwork"
    type = string
}

variable "cidr-range" {
    description = "CIDR range of the subnetwork"
    type = string
    default = "10.10.0.0/24"
}

variable "region" {
    description = "name of the region that the sub-network will be located"
    type = "string"
}