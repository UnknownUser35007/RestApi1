from google.cloud import storage
import json

def download_blob_into_memory(bucket_name, blob_name):
    
    storage_client = storage.Client.from_service_account_json('/home/apnx-desk-05/Downloads/ax-interns-22-335d28f36a55.json')

    bucket = storage_client.bucket(bucket_name)
    #bucket_dest=storage_client.bucket('interns-bucket')
    blob = bucket.blob(blob_name)
 
    contents = blob.download_as_text()
    print(contents)
    json_data = json.loads(contents)
    
    with open("db01.json", "w") as outfile:
    	json.dump(json_data, outfile)
    #b=bucket_dest.blob('db11.json')
    #b.upload_from_string(json.dumps(json_data))	
download_blob_into_memory('apnx_bucket_02', 'drift.json')
