Face Match
---

Match two images containing face and check if two face are of same people or different.

Tested with python 3.6.

Installation
---

Clone this repo using following command.

    $ git clone https://github.com/shashwatacharya30/Face-Match.git

Install required dependencies from requirements.txt.

    $ pip install -r requirements.txt
    
Run face_match.py by passing two images. Replace FirstImage and SecondImage with your image below and compare between those two images.

    $ python face_match.py --img1 FirstImage.jpg --img2 SecondImage.jpg

To create .tflite file. Run tfliteconverter.py

    $ python tfliteconverter.py
    
