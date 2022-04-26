import requests
import ctypes
def download_image_from_url(image_url, save_path):
    """
    connects to the API to download the image from the url
    :param image_url: URL of image
    """


    print('Downloading image from URL...', end='')

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)   
        print("Success")
    else:
        print('Failed. Response code:', response.status_code)


def set_desktop_bckgrng_img(image_path):
    """
    Sets the wallpapper
    :param image_path: path where image gets saved
    """

    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)