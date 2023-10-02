import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

github_user = input('Input Github User: ')


url = 'https://github.com/' + github_user
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    soup = bs(r.content, 'html.parser')
    
    profile_image = soup.find('img', {'class': 'avatar'})['src']
    response = requests.get(profile_image)

    # Check if the image request was successful
    if response.status_code == 200:
        image_online = Image.open(BytesIO(response.content))
        plt.imshow(image_online)
        plt.axis('off')  # Turn off axes
        plt.show()
        
        # You can now work with the 'image_online' object as needed
    else:
        print("Failed to download the profile image.")
else:
    print(f"Failed to retrieve the GitHub profile for user: {github_user}")