import os
import requests

def download_mod(url, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        file_path = os.path.join(directory, file_name)

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {file_name} to {directory}")
    else:
        print(f"Failed to download from {url}. Status code: {response.status_code}")