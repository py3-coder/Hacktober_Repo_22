# spam-detection
#### Spam detection model which predicts whether mail is spam or not.

![stephen-phillips-hostreviews-co-uk-3Mhgvrk4tjM-unsplash](https://user-images.githubusercontent.com/88129183/170872627-d3b8e473-d3a4-4ce8-ae29-7bcb79d7a153.jpg)

## About Dataset
This dataset contains around 5k sample mail with label 'Spam' and 'Ham'.

## About Project
This project predicts whether entered mail is spam or not. I made it using Flask and Flasgger, built a model using Sklearn library. 

## How to run
* First install libraries from `requirement.txt file`.
* Then run `flasgger_app.py`. It'll give you localhost, go to browser and search `localhost/apidocs` which leads to this page.

![image](https://user-images.githubusercontent.com/88129183/170879031-6f0ada32-21c4-4859-b0a4-f965defa994b.png)

* Then click on 'Try it out' and enter your mail in a given text box, then hit 'Execute' button.
* Prediction will appear in below as shown in screen. For spam it'll give `This Mail is Spam.` otherwise give `This Mail is not Spam.`
*  For current input it gave `This Mail is Spam.`

![image](https://user-images.githubusercontent.com/88129183/170879222-57712ed9-1bda-4c93-a043-65e0b6aafb4b.png)
