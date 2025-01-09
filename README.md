# weather-dashboard

This project is part of my 30-Day DevOps Challenge #DevOpsAllStarChallenge. It focuses on building a Python application that retrieves real-time weather data from the OpenWeather API and saves it in an AWS S3 bucket. This project helped me learn how to work with APIs, manage environment variables, and use AWS for cloud storage.

**Features**

Fetch real-time weather data for various cities using the OpenWeather API.
Displays temperature (°F), humidity, and weather conditions
Store and manage weather data securely in an AWS S3 bucket.
Utilize environment variables for secure API key management and configuration.

**Prerequisites**

Before running this project, I made sure I had the following:

Python installed using VsCode
An OpenWeather API key from openweathermap.org
AWS account set up with AWS CLI configured with an IAM user that has S3 permissions

**Setup and Installation**

**1. Clone the Repository**
Clone the repository to your local machine:

git clone https://github.com/FLATOPA/weather-dashboard.git
cd weather-dashboard

**2. Set Up a Virtual Environment**
Create and activate a virtual environment:

python3 -m venv venv  
source venv/bin/activate

**3. Install Dependencies**
Install the required libraries:

pip install -r requirements.txt

**4. Add Your API Key and Configuration**
Create a .env file in the root directory with the following content:

OPENWEATHER_API_KEY=<My_generated_weatherAPI_key>
AWS_BUCKET_NAME=<my_aws_bucket_name>


**What I Learned**

I learned how to use an API to fetch real-time data from the internet.
I discovered how to securely manage important information like API keys using environment files.
I practiced storing data in the cloud using AWS S3 buckets.
I practiced using Access Keys to enhance the security during this project.
I understood the importance of organizing my project with a virtual environment to manage tools and libraries.
I improved my problem-solving skills by troubleshooting errors during the setup.

**Run the script to fetch the weather data and upload it to the S3 bucket:**

python3 src/weather_dashboard.py
