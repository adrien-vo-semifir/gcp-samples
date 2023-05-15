from google.cloud import storage
from google.oauth2 import service_account


def upload_blob(bucket_name: str, source_file_name:str, destination_blob_name: str):
    """Permet d'uploader un fichier dans une bucket GCP

    Args:
        bucket_name (str): Nom de la bucket GCP où stocker le fichier
        source_file_name (str): Fichier à uploader
        destination_blob_name (str): Nom du fichier dans la bucket
    """

    # Initialiser le client
    storage_client = storage.Client.from_service_account_json('credentials/credentials.json')


    # récupérer la bucket
    bucket = storage_client.bucket(bucket_name)

    # Créer un blob dans la bucket
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Usage
upload_blob('avm-exemple', 'fichiers/sample.txt', 'test/sample.txt')
