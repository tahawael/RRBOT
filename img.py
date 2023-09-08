import random
import discord
import time
from discord.ext import commands
from PIL import Image, ImageDraw, ImageSequence
import io
import requests


def generate(url):
    im = Image.open('DiscordBot/ruruN.gif')
    # Load the PNG image you want to overlay on each frame
    img_data = url
    with open('playerA.jpg', 'wb') as handler:
        handler.write(img_data)

    png_image = Image.open('playerA.jpg')
    png_image.thumbnail((50,50), Image.LANCZOS)
    # Define the desired size for the PNG image
    # w, h = png_image.size
    # new_width = w /2
    # new_height = h /2

    # Resize the PNG image to the desired size
    # png_image = png_image.resize((png_image.size[0] // 4, png_image.size[1] // 4), Image.LANCZOS)

    # print(png_image.size)
    # A list of the frames to be outputted
    frames = []

    # Loop over each frame in the animated image
    for frame in ImageSequence.Iterator(im):
        # Create a copy of the frame to work on
        frame_copy = frame.copy()

        # Calculate the position to center the resized PNG image on the frame
        frame_width, frame_height = frame.size
        png_width, png_height = png_image.size
        png_x = (frame_width - png_width) // 2
        png_y = (frame_height - png_height) // 12

        # Paste the resized PNG image onto the frame
        frame_copy.paste(png_image, (png_x, png_y), png_image)

        # Saving the modified frame without 'save_all'
        b = io.BytesIO()
        frame_copy.save(b, format="GIF")
        frame_copy = Image.open(b)

        # Then append the modified frame to a list of frames
        frames.append(frame_copy)

    # Save the frames as a new animated GIF
    frames[1].save('out1.gif', save_all=True, append_images=frames[1:])

# import multiprocessing

# def generate(url):
#     im = Image.open('C:/Users/Mohamed Wael/Desktop/ruruN.gif')

#     # Load the PNG image you want to overlay on each frame
#     img_data = url
#     with open('playerA.jpg', 'wb') as handler:
#         handler.write(img_data)

#     png_image = Image.open('playerA.jpg')

#     # Define the desired size for the PNG image
#     new_width = 50
#     new_height = 50

#     # Resize the PNG image to the desired size
#     png_image = png_image.resize((new_width, new_height), Image.LANCZOS)

#     # A list of the frames to be outputted
#     frames = []

#     # Create a pool of workers
#     pool = multiprocessing.Pool()

#     # Iterate over each frame in the animated image
#     for frame in ImageSequence.Iterator(im):
#         # Create a copy of the frame to work on
#         frame_copy = frame.copy()

#         # Calculate the position to center the resized PNG image on the frame
#         frame_width, frame_height = frame.size
#         png_width, png_height = png_image.size
#         png_x = (frame_width - png_width) // 2
#         png_y = (frame_height - png_height) // 12

#         # Paste the resized PNG image onto the frame
#         frame_copy = pool.apply_async(png_image.paste, args=(png_x, png_y, png_image))
#         frames.append(frame_copy)

#     # Close the pool
#     pool.close()
#     pool.join()

#     # Save the frames as a new animated GIF
#     frames[1].save('out1.gif', save_all=True, append_images=frames[1:])
