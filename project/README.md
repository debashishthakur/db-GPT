# Project Directory README

Welcome to the project directory for db-GPT! This directory contains the code and resources for the project. Below, you'll find an overview of the contents and instructions on how to get started.

## Contents

- **gf2_model.ipynb**: This Jupyter Notebook contains the implementation of the Hugging Face model. It's where the model is loaded and generates SQL queries.

- **app.py**: This is the main Flask application for the project. It serves as the entry point for our web application.

- **database.py**: This file contains the code for the database connection from Flask to MySQL. It's responsible for managing data storage and retrieval.

- **model_params.py**: This file contains the calculation of the model parameters that I attempted to use earlier in the project. It's a crucial part of the model implementation.

- **Seq2seq.ipynb**: This Jupyter Notebook is where I've built a custom encoder-decoder model from scratch. This model is capable of predicting SQL queries. It's a valuable resource for understanding the model's architecture and training process.

- **card.json**: This dataset is used throughout the project to train and evaluate the models. It contains the necessary data for our machine learning tasks.

- **requirements.txt**: This file lists all the required dependencies for the project. Before running the application, make sure to install these dependencies.


## Getting Started

To run the application, follow these steps:

1. **Install Dependencies**: Open a terminal and navigate to the project directory. Run the following command to install the required Python packages: pip install -r requirements.txt


2. **Start the Flask Server**: After all the dependencies are installed, you can start the Flask server by running: flask --app app --debug run


This will start the web application, and you can access it in your web browser.

That's it! You're now ready to use the project. If you have any questions or encounter any issues, please refer to reach out to me.

Thank you for exploring the project, and I hope you find it valuable!
