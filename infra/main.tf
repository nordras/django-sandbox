# Exemplo de script OpenTofu/Terraform
terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = "2.11.0"
    }
  }
}
provider "kubernetes" {
  config_path = "~/.kube/config"
}
resource "kubernetes_namespace" "apps" {
  metadata {
    name = "apps_namespace"
  }
}
