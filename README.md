# Data Pipeline Project

This project demonstrates a complete end-to-end data pipeline process using Python, Pandas, and Apache Airflow. The pipeline performs Extract, Transform, and Load (ETL) operations on data, making it ready for analysis or further processing.

## Overview

This project extracts data from CSV files, transforms it using Python and Pandas, and loads it into a database or other formats. Apache Airflow is used to orchestrate and automate the workflow.

## Prerequisites

Before you begin, ensure that you have met the following requirements:
- Python 3.x
- Apache Airflow
- Pandas
- Git (for version control)

## Installation

### 1. Clone the repository

Clone the repository to your local machine using:

```bash
git clone https://github.com/fardeenshroff/data-pipeline-project.git

2. Navigate to the project directory

Go to the project directory:

cd data-pipeline-project

3. Set up a virtual environment (optional but recommended)

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install dependencies

Install the required Python packages:

pip install -r requirements.txt

If you don't have a requirements.txt file, you can manually install the necessary dependencies:

pip install pandas apache-airflow

Usage

1. Run the data extraction, transformation, and loading (ETL) pipeline

To run the ETL pipeline, use the following command:

python extract.py

2. Apache Airflow Setup (Optional)

If you're using Apache Airflow to schedule and monitor your workflows:

Start the Airflow scheduler:


airflow scheduler

Start the Airflow web server:


airflow webserver

Then, you can access the Airflow UI at http://localhost:8080.

Contributing

If you'd like to contribute to this project, feel free to fork it and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License - see the LICENSE.md file for details.



