import os,requests,threading
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for errors

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"Download completed: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Function to download multiple files using threads
def download_multiple_files(file_urls, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    threads = []

    for i, url in enumerate(file_urls):
        filename = os.path.join(save_folder, f"file_{i+1}.jpg")  # Adjust extension if needed
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to finish

    print("All downloads completed!")

# List of file URLs to download
#url="https://www.google.com/imgres?q=picture%20&imgurl=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F036%2F324%2F708%2Fsmall%2Fai-generated-picture-of-a-tiger-walking-in-the-forest-photo.jpg&imgrefurl=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2Fpicture&docid=wska7sM6RxRdCM&tbnid=crGgp78bfBsQFM&vet=12ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECBsQAA..i&w=300&h=200&hcb=2&ved=2ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECBsQAA"
file_urls = [
    "https://www.google.com/imgres?q=picture%20&imgurl=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2024%2F05%2F26%2F10%2F15%2Fbird-8788491_1280.jpg&imgrefurl=https%3A%2F%2Fpixabay.com%2Fphotos%2Fbird-blue-clouds-weather-pen-8788491%2F&docid=UHcUa7a-6-cYRM&tbnid=90TpIHBM_bySlM&vet=12ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECHoQAA..i&w=1280&h=853&hcb=2&ved=2ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECHoQAA",
    "https://www.google.com/imgres?q=picture%20&imgurl=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F045%2F132%2F934%2Fsmall_2x%2Fa-beautiful-picture-of-the-eiffel-tower-in-paris-the-capital-of-france-with-a-wonderful-background-in-wonderful-natural-colors-photo.jpg&imgrefurl=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2Fpicture&docid=wska7sM6RxRdCM&tbnid=dFYrDP8ftTkUfM&vet=12ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECBcQAA..i&w=551&h=400&hcb=2&ved=2ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECBcQAA",
    "https://www.google.com/imgres?q=picture%20&imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F1704488%2Fpexels-photo-1704488.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fprofile%2520picture%2F&docid=FvQHUVZ-cx81xM&tbnid=IZwkkMq7AJXOIM&vet=12ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECEIQAA..i&w=500&h=661&hcb=2&ved=2ahUKEwiupdr08aWMAxW2ywIHHUpZEIEQM3oECEIQAA"
]

save_folder = "downloads"

# Start downloading files
download_multiple_files(file_urls, save_folder)
