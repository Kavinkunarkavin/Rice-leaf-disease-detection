# Rice-leaf-disease-detection
This project provides a solution for automated detection and classification of diseases affecting rice plants using computer vision and deep learning techniques. It includes source code for the backend using FastAPI and TensorFlow, as well as a PyQT-based frontend for user interaction.


# Features
Automatic detection and classification of rice leaf diseases
Pretrained deep learning model for accurate predictions
User-friendly frontend using PyQT for capturing and uploading leaf images
Real-time disease predictions with confidence scores


# Installation
Clone the repository
git clone https://github.com/kavinkunarkavin/rice-leaf-disease-detection.git

Install the required dependencies:
pip install -r requirements.txt

Configure AWS S3 credentials:
Open config.py file and enter your AWS S3 credentials. 

Start the backend server:
python predict.py

Launch the frontend application:
Open the frontend directory.
Run the PyQT applicatation
python frontend.py


# USAGE
Open the frontend application.
Capture or upload an image of a rice leaf.
Click the "Predict" button to initiate disease detection.
View the predicted class and confidence score for the detected disease.


# Dataset Link:
https://www.kaggle.com/datasets/shayanriyaz/riceleafs


# Acknowledgments
Special thanks to the developers and contributors of FastAPI, TensorFlow, and PyQT for their invaluable libraries and tools.


# Contributions
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.


# License
This project is not liensed(open source code)


# Acknowledgments
Special thanks to the developers and contributors of FastAPI, TensorFlow, and PyQT for their invaluable libraries and tools.

# Contact
For any inquiries or questions, please contact kavin11112003@gmail.com.

Please note that this project is not actively maintained, but your feedback is still highly appreciated.
