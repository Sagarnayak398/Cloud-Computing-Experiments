# process_images.py

import threading
from azure.storage.blob import BlobServiceClient
from PIL import Image
import io

# Azure connection - PASTE your connection string here between the quotes
connection_string = "CONNECTION_STRING"
container_name = "images"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

def process_image(blob_name):
    blob_client = container_client.get_blob_client(blob_name)

    # Download original image
    data = blob_client.download_blob().readall()
    stream = io.BytesIO(data)

    # Open and process image (resize + grayscale)
    img = Image.open(stream)
    img = img.resize((300, 300))
    img = img.convert("L")   # grayscale

    # Save processed image
    output = io.BytesIO()
    img.save(output, format="JPEG")
    output.seek(0)

    # Upload processed image with new name
    new_blob_name = "processed_" + blob_name
    container_client.upload_blob(name=new_blob_name, data=output, overwrite=True)
    print(f"Processed and uploaded: {new_blob_name}")

# Get list of original images (skip already-processed ones)
blob_list = [b.name for b in container_client.list_blobs() if not b.name.startswith("processed_")]

# Run processing in parallel using threads
threads = []
for blob_name in blob_list:
    t = threading.Thread(target=process_image, args=(blob_name,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All images processed successfully.")
