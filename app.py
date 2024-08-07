import streamlit as st
from google.cloud import storage
from google.oauth2 import service_account
import os

# Set up Google Cloud Storage credentials
def get_gcs_client():
    return storage.Client()

def upload_to_gcs(bucket_name, source_file, destination_blob_name):
    client = get_gcs_client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(source_file)
    return f"File uploaded to {destination_blob_name} in bucket {bucket_name}"

# Streamlit app
st.title("Upload Files to Google Cloud Storage")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    bucket_name = 'sales-databse'
    destination_blob_name = uploaded_file.name
    upload_message = upload_to_gcs(bucket_name, uploaded_file, destination_blob_name)
    st.success(upload_message)
    if os.path.exists(uploaded_file.name):
        os.remove(uploaded_file.name)
        st.write(f"File {uploaded_file.name} deleted successfully.")
