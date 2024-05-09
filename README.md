## Dataset generator
Hi :) Thanks for taking interest in improving my model. To read about the project in more detail, visit [this repo](https://github.com/worthy11/PJMRecognizer).
### Installation
You'll be tasked with supplying training data for my gesture recognition model. You need to have Python installed on your machine in order to be able to run the code. All required modules are listed in `requirements.txt`; you can install them using `pip install -r requirements.txt`. <br />

### Usage
Running the `main.py` file will (**likely after a delay**) turn on your camera, display the feed in a **Webcam** window and show an image in an **Instruction** window, instructing you on the gesture you're supposed to make with your hand. When you think you're showing the appropriate gesture, press `Enter` to save - you'll be given feedback about whether the sample has been saved successfully or an exception has occurred. Possible exceptions include the failure to recognize the presence of a hand in the frame or the detection of too many hands at one time. If saving succeeds, the image shown in **Instruction** will switch to the next letter. <br />

### How to contribute?
Once you've completed all the letters, you can choose to quit or go again. When you think you've supplied enough samples, commit your changes so that I can use the updated dataset. If you wanna take a break and come back some other time, remember to first `git pull`.

## Thank you :D