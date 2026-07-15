# Terraform Infrastructure

This directory contains the Terraform configuration used for the basic Google Cloud infrastructure of the Multi-Agent Student Services Assistant.

## Managed Resources

Terraform currently manages the following resources:

- Required Google Cloud APIs:
  - Artifact Registry API
  - Cloud Run API
  - Cloud SQL Admin API
  - Secret Manager API
- Artifact Registry Docker repository named `student-services`
- Backend service account named `student-services-backend`
- Cloud SQL Client IAM role for the backend service account
- Secret Manager Secret Accessor IAM role for the backend service account
- Secret Manager secret container for `DATABASE_URL`
- Secret Manager secret container for `OPENAI_API_KEY`

Terraform manages the Secret Manager secret containers only. Secret values are not stored in the Terraform configuration or committed to the repository.

## Cloud SQL

The `student-services-db` Cloud SQL PostgreSQL instance was created manually before the Terraform configuration was expanded.

The existing Cloud SQL instance is not currently managed by Terraform. During development, the instance was inspected before attempting infrastructure management because its live database version and machine configuration differed from the initial Terraform assumptions.

To avoid an unsafe modification of the working database, the Cloud SQL instance was intentionally left outside the current Terraform state.

The backend service account is granted the `roles/cloudsql.client` role through Terraform so the Cloud Run backend can connect to the existing Cloud SQL instance.

## Cloud Run Deployment

Cloud Run services are deployed separately using `gcloud` commands.

The backend uses the Terraform-created `student-services-backend` service account as its Cloud Run service identity.

Cloud Run deployment is intentionally kept outside the current Terraform configuration. This follows the project allowance to use `gcloud run deploy` when managing Cloud Run through Terraform would add unnecessary complexity.

## Files

- `main.tf` — Google provider and managed GCP infrastructure resources
- `variables.tf` — project ID and region variables
- `outputs.tf` — useful Terraform output values
- `.terraform.lock.hcl` — locked provider dependency versions

## Terraform Workflow

Initialize Terraform:

```powershell
terraform init