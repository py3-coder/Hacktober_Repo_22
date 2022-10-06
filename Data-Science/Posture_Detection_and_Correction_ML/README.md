# Posture Detection and Correction
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)

Website which is used to correct the posture of the user sitting in front of their screen even when the process is running in the background with voice alerts

* The deployed website can be seen [here](https://posturecorrection.herokuapp.com/)

## Table Of Contents:

[Installation](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/README.md#installation)

[Usage](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/README.md#usage)

[Working](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/README.md#working)

[ToDo](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/README.md#todo)

[Contributing](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/README.md#contributing)

## Installation

1. Download and install Python3 from [here](https://www.python.org/downloads/)
2. I recommend using [virtualenv](https://virtualenv.pypa.io/en/latest/). Download virtualenv by opening a terminal and typing:
    ```bash
    pip install virtualenv
    ```
3. Create a virtual environment with the name venv.

   * Windows
   ```bash
   virtualenv venv
   cd venv/Scripts
   activate
   ```
   * Linux:
   ```bash
   source venv/bin/activate
    ```
4. Clone this repository, extract it if you downloaded a .zip or .tar file and cd into the cloned repository.

    * For Example:
    ```bash
    cd A:\Posture_Detection_AND_Correction-main
    ```
5. Install the required packages by typing:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
* You can change the background sound of the application by just storing the sound file in the mentioned directory
```bash
se_hackethon_project/static/src/js/audofile.type
```
* Type the below command to run the Application. It will start the server on **localhost:5000**
    ```bash
    python app.py
    ```
* The Homepage of our Application.

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/1.png)

* Providing the user with google authentication which directly creates the profile of the user in the backend. Also we have provided the user with traditional system of logging in registering :)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/2.png)

* After logging in the user gets to see the different options available as mentioned in the above screen shot. Lokking at some of the features.

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/3.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/4.png)

* We don't want our users to just use our Website just as a tool, but we also want them to motivate others so that they could also make it a part of their life. So we have also created the feature of blogs in our website with basic functionality of updating deleting and so on.

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/5.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/6.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/7.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/8.png)

* Finally when we click on **Try our Website** we will come to the main feature of our website :).

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/9.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/10.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/11.png)

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/12.png)

* Now when we click upon **Analyze Session** we have provided user with an interactive dashboard whenthey can see which are the most common errors they are commiting and can also print a report.

    ![](https://github.com/BassCoder2808/Posture_Detection_AND_Correction/blob/main/Screenshots/13.png)


## Working

### Image Preprocessing

* So first of all we have stored all the templates in a folder
```bash
cd se_hackethon_project/templates
```

* After that we have created the routes of the templates in the file routes.py

* For the databse we have used sqlite and our models are stored in models.py file

* All our forms are stored the forms.py file as per the convention of flask

* All the static content need to be stored in the static folder as per the convention followed

### Recognition

#### jeelizAr

Read about jeelizAR [here](https://github.com/jeeliz/jeelizAR)
* It is basically used to recognize the face of the user
* It is used to draw the blue box around the user as seen in the above screen shots
* Also used for understanding the key points used to detect the posture

#### Three.js

Read about Three.js [here](https://threejs.org/)
* As we all know that our camera does not have a depth sensing to draw a 3-D model.
* So for actually creating a 3-D model from our live-stream of web cam we use Three.js

## ToDo

* Fixing the front-end of the application
* Resolve Bugs/Issues if any found.
* Optimize Code to make it faster.

## Contributing

Contributions are welcome :smile:

### Pull requests

Just a few guidelines:
* Write clean code with appropriate comments and add suitable error handling.
* Test the application and make sure no bugs/ issues come up.
* Open a pull request and I will be happy to acknowledge your contribution after some checking from my side.

### Issues

If you find any bugs/issues, raise an issue.
