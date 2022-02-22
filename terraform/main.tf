provider "google" {
  credentials = file("creds.json")

  project = "pds-cloud-resume"
  region  = "us-west1"
  zone    = "us-west1-c"
}

resource "google_firestore_document" "counter" {
  project     = "pds-cloud-resume"
  collection  = "counter"
  document_id = "counter"
  fields      = "{\"count\":{\"integerValue\":0}}"
}

resource "google_storage_bucket" "bucket" {
  name     = "counter-function"
  location = "US"
}

resource "google_storage_bucket_object" "archive" {
  name   = "counter.zip"
  bucket = google_storage_bucket.bucket.name
  source = "../backend/counter/counter.zip"
}

resource "google_cloudfunctions_function" "function" {
  name        = "counter"
  description = "counter"
  runtime     = "python39"

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  entry_point           = "visitcount"
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}

output "api_url" {
  value = google_cloudfunctions_function.function.https_trigger_url
}
