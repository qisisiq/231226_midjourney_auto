import os

# Path to the directory containing the images
folder_path = 'mj-fave-seed-images'

# URL format
url_format = 'https://github.com/qisisiq/231226_midjourney_auto/blob/main/mj-fave-seed-images/{filename}?raw=true'

# List of URLs
urls = []

# Iterate over the files in the directory
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.png')):  # Check for .jpg and .png files
        # Replace spaces in filenames with %20 for URL encoding
        encoded_filename = filename.replace(' ', '%20')
        # Create the full URL and add it to the list
        full_url = url_format.format(filename=encoded_filename)
        urls.append(full_url)

# Now 'urls' contains all the formatted URLs
for url in urls:
    print(url)
