# Flask Temperature Converter App

This repository contains a simple Flask application that converts temperatures from Celsius to Fahrenheit. It provides a REST API for POST requests with JSON payloads and serves an HTML page for GET requests.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Python](https://www.python.org/) 3.10 or later 

- [Git](https://git-scm.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## Local Setup

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   - **Windows:**
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux:**
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required Python packages:
   ```
   pip install Flask gunicorn
   ```

4. Run the application locally:
   ```
   python app.py
   ```
   Visit `http://127.0.0.1:5000/` in your browser to view the app.

## Deploying to Heroku

1. Log in to Heroku:
   ```
   heroku login
   ```

2. Initialize a Git repository (if you haven't already):
   ```
   git init
   heroku git:remote -a <your-heroku-app-name>
   ```

3. Create a `Procfile` in the root directory of your application with the following content:
   ```
   web: gunicorn -b 0.0.0.0:$PORT app:app   
   ```

4. Create a `requirements.txt` file (if you haven't already) with all the necessary Python packages:
   ```
   Flask
   gunicorn
   ```

5. Add and commit your changes to Git:
   ```
   git add .
   git commit -am "commit"
   ```

6. Deploy your application to Heroku:
   ```
   heroku push heroku master
   ```

7. Ensure that at least one instance of the app is running:
   ```
   heroku ps:scale web=1
   ```

8. Open your application in the browser:
   ```
   heroku open
   ```


## Checking the Log

If you face any error or want to check the logs:
   ```
heroku logs --tail  
 ```

## Running Unit Tests

To ensure the Flask Temperature Converter app functions correctly, it's important to run unit tests. Follow these steps to execute the tests using the `test_app.py` script:

1. **Ensure prerequisites are installed**: Make sure Python 3.10 or later is installed on your system, and all dependencies for the Flask app are satisfied.

2. **Navigate to your project directory**: Open a terminal and change to the directory containing your Flask application and the `test_app.py` file.

3. **Execute the test script**: Run the following command in the terminal:
```
python test_app.py
 ```
This command will run all unit tests defined in the `test_app.py` file.

4. **Review the test results**: After the tests have finished, the terminal will display the results, showing which tests passed and which failed, if any.
