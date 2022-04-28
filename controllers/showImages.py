from flask import flash,session
from models import getImages

def showImagesUser():
    try:
        token = session['token']
        images = getImages.getImagesUser(token)
        return images
    except:
        print("Error occured in showImagesUser")
def showImages():
    try:
        images = getImages.getImages()
        print(images)
        return images
    except:
        print("Error occured in showImages")
def showImagesEdit(id):
    try:
        images = getImages.getImagesId(id)
        print(images)
        return images
    except:
        print("Error occured in showImagesEdit")
        