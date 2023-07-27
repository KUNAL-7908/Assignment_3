# Question 7
from google_images_download import google_images_download

def download(keyword, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": keyword,
        "limit": limit,
        "print_urls": True
    }
    paths = response.download(arguments)
    return paths[keyword]

if __name__ == "__main__":
    keyword = "cat"
    num_images = 10 

    image_paths = download(keyword, num_images)
