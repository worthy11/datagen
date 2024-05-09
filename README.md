# PJM Dataset Generator
Hi :) Thanks for taking interest in improving my model. To read about the project in more detail, visit [this repo](https://github.com/worthy11/PJMRecognizer).

## Installation
You'll be tasked with supplying training data for my gesture recognition model. You need to have Python installed on your machine in order to be able to run the code. All required modules are listed in `requirements.txt`; you can install them using `pip install -r requirements.txt`. <br />

## Before you start
**IMPORTANT**: The images may look confusing if you haven't been exposed to sign language before. Some contain instructions about hand movement, for example:

<p align="center">
  <img src="https://github.com/worthy11/datagen/blob/main/img/K.png" alt="The letter K in PJM"/>
</p>

Currently, the model does not recognize any movement and only relies on still frames - please ignore the movement instructions and show a stationary gesture instead. If you're not sure whether you're showing the correct gesture or not, **DON'T WORRY**! That's the point. Just show whatever you think is the closest to what's being displayed in the image. <br />

## Usage
Running the `main.py` file will (**likely after a delay**) turn on your camera, display the feed in a **Webcam** window and show an image in an **Instruction** window, instructing you on the gesture you're supposed to make with your hand. When you think you're showing the appropriate gesture, press `ENTER` to save - in the terminal, you'll be given feedback on whether the sample has been saved successfully or an exception has occurred. Possible exceptions include failure to recognize the presence of a hand in the frame or detection of too many hands at one time. If saving succeeds, the image shown in **Instruction** will switch to the next letter. <br />

You may quit the application at any time by pressing `ESC`. <br />

## How to contribute?
This application does not save any pictures of you - it only extracts the positions of 21 landmarks detected on your hand, nothing more. When you decide you've provided enough samples, you can view the saved data in `dataset.csv` and upload said file [here](https://drive.google.com/drive/folders/1xTshgbtzfqEG89rFHfK972tlelepRrYR?usp=sharing). You may rename the file to whatever you like, but if you choose to come back and generate more samples, please remember to change the name back to `dataset.csv`.<br /><br />

<h2 align="center">Thank you :D</h2>