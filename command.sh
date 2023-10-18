docker build --platform linux/amd64 -t asia-south2-docker.pkg.dev/founderxnotes/founderx-whatsapp/status .
# docker run -p 5000:8080 myflaskapp


docker push asia-south2-docker.pkg.dev/founderxnotes/founderx-whatsapp/status:latest

# run on cloud run using cloud run
gcloud run deploy --image asia-south2-docker.pkg.dev/founderxnotes/founderx-whatsapp/status:latest --platform managed --region asia-south2 --allow-unauthenticated




