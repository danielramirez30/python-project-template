import shutil

import requests

# define a function in python that gets and image from a specific url and
# saves it in my file system


def get_image(url, filename):
    # document this function with a docstring
    """
    get_image(url, filename)
    url: url of the image to download
    filename: name of the file to save the image to
    returns: None
    """

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        response.raw.decode_content = True
        # context managers Corey Schafer
        with open(filename, "wb") as f:
            shutil.copyfileobj(response.raw, f)
            print("Image sucessfully Downloaded: ", filename)
        return True
    else:
        print("Image couldn't be retreived")
        return False


# get_image(
#     "https://th.bing.com/th/id/R.fcd349af80cb44e5a32bc3696019cf5f?rik=8bH1xMwmkghXvg&pid=ImgRaw&r=0",
#     "test.jpg",
# )
