# GrandRP Treasure Finder
This scripts helps you to find the GrandRP treasures easily by providing just a screenshot of the treasure.

## How it works
This script uses tensorflow to convert the images of the treasures to vectors. Once the program is started, it will also convert the user.png image to vectors and compare the vectors of the provided image with the all vectors of the treasure images. It will then calculate the equality of the vectors for every treasure and provide you with the most matching treasure.

## Preview
- Treasure Finder<br>
     <img src="https://github.com/SiroxCW/grandrp-treasure-finder/blob/main/preview/preview_treasure.png" width="550" height="300">

- Discord Bot<br>
     <img src="https://github.com/SiroxCW/grandrp-treasure-finder/blob/main/preview/preview_discord_bot.png" width="550" height="300">


## Usage
- Treasure Finder
  1. Take a screenshot of the treasure inside the game.
  2. Save the image as user.png in the same folder as the script.
  3. Run the treasure script and it should open the image of the map, where the treasure is located.
- Discord Bot
  1. Put your discord bot token inside the config.json file and save it.
  2. Run the discord_bot script.
  3. Use /treasure on the discord server and provide a picture (this will be user.png). The bot should then return the map, where the treasure is located by uploading a image.

## How to add images
If you want to add images to the search like for the weapon components event you can do the following:
1. Create a new folder inside the data folder.
2. Place a picture of the map location inside the new folder called map.png.
3. Place a second picture of the secret image ingame inside the new folder called treasure.png. <br>

The missing vector.txt file will be automatically created by the script.
