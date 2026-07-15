terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 7.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "required_apis" {
  for_each = toset([
    "artifactregistry.googleapis.com",
    "run.googleapis.com",
    "sqladmin.googleapis.com",
    "secretmanager.googleapis.com",
  ])

  project = var.project_id
  service = each.value

  disable_on_destroy = false
}

resource "google_artifact_registry_repository" "student_services" {
  location      = var.region
  repository_id = "student-services"
  description   = "Container images for the Student Services Assistant"
  format        = "DOCKER"

  depends_on = [
    google_project_service.required_apis,
  ]
}

resource "google_service_account" "backend" {
  account_id   = "student-services-backend"
  display_name = "Student Services Backend"
}

resource "google_secret_manager_secret" "database_url" {
  secret_id = "DATABASE_URL"

  replication {
    auto {}
  }

  depends_on = [
    google_project_service.required_apis,
  ]
}

resource "google_secret_manager_secret" "openai_api_key" {
  secret_id = "OPENAI_API_KEY"

  replication {
    auto {}
  }

  depends_on = [
    google_project_service.required_apis,
  ]
}

resource "google_project_iam_member" "backend_cloud_sql_client" {
  project = var.project_id
  role    = "roles/cloudsql.client"
  member  = google_service_account.backend.member
}

resource "google_project_iam_member" "backend_secret_accessor" {
  project = var.project_id
  role    = "roles/secretmanager.secretAccessor"
  member  = google_service_account.backend.member
}