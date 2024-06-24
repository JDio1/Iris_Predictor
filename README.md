# Iris Predictor Cloud Function & Machine Learning
Welcome to the Iris Predictor Cloud Function project! This repository hosts a serverless machine learning service for predicting the species of an iris flower based on its dimensions.


## Purpose
The Iris Predictor Cloud Function project aims to provide a simple, serverless machine learning service for predicting the species of an iris flower based on its sepal and petal dimensions. This project leverages Google Cloud Functions, a serverless execution environment, to host a lightweight Flask web server that serves predictions using a pre-trained machine learning model.

## Technologies Used
- Python
- Google Colab
- Google Cloud Functions
- Scikit-learn (for machine learning model)
- MLflow

## Problem Solved
The project addresses the need for a scalable and cost-effective solution to deploy machine learning models for prediction tasks. By using Google Cloud Functions, it eliminates the need to manage infrastructure, making it easier to deploy and scale predictive services based on machine learning models.


## Outcome
The Cloud Function returns predictions for the species of iris flower based on the input dimensions, demonstrating the integration of machine learning into serverless environments.

## Interesting Aspects of the Project
1. **Serverless Architecture**: It utilizes Google Cloud Functions, which automatically scales based on traffic and usage, ensuring efficient resource utilization and cost-effectiveness.
2.	**Machine Learning Integration**: The project integrates a trained machine learning model (in this case, a model for iris flower classification) into a serverless environment, demonstrating practical deployment scenarios for ML applications.
3.	**RESTful API**: The Cloud Function exposes a REST API endpoint (/iris_predictor) that accepts POST requests with JSON payloads containing input data for prediction, showcasing integration with web-based and cloud-native applications.
4.	**Scalability** and Performance: Leveraging Google Cloud Functions ensures high availability and scalability without the need for manual intervention, suitable for handling varying levels of prediction requests.

## Steps
1. **Data Collection and Preparation:**
   - Loaded and preprocessed the Iris dataset.
   - Split the data into training and test sets.

2. **Model Training and Evaluation:**
   - Trained a Logistic Regression model.
   - Evaluated the model using accuracy and classification report.

3. **Experiment Tracking:**
   - Used MLflow to track experiments and log parameters, metrics, and models.

4. **Model Deployment:**
   - Saved the trained model.
   - Created a Google Cloud Function to serve the model.
   - Deployed the model and tested it using HTTP requests.

## How to Run the Project
1. Set up a Google Cloud account and enable Cloud Functions.
2. Create a Google Colab notebook and follow the provided code snippets in `Iris ML.ipynb` to load, preprocess, and train the model.
3. Use MLflow to track experiments.
4. Save the trained model and deploy it using Google Cloud Functions.
5. Test the deployed model using HTTP requests.
    - Test the Cloud Function:
    - Send a POST request to `https://REGION-YOUR_PROJECT_ID.cloudfunctions.net/iris_predictor` with JSON payload `{"input": [5.1, 3.5, 1.4, 0.2]}`.

    ## Usage Examples

    You can interact with the Iris Predictor Cloud Function using tools like `curl` or `httpie`. Here's an example using `curl`:
        ```sh
        curl -X POST \
        -H "Content-Type: application/json" \
        -d '{"input": [5.1, 3.5, 1.4, 0.2]}' \
        https://REGION-YOUR_PROJECT_ID.cloudfunctions.net/iris_predictor



