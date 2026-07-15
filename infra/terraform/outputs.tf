output "artifact_registry_repository_name" {
  description = "Name of the Artifact Registry repository"
  value       = google_artifact_registry_repository.student_services.repository_id
}

output "backend_service_account_email" {
  description = "Email of the backend Cloud Run service account"
  value       = google_service_account.backend.email
}