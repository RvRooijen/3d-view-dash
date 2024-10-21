# Dash Application Communication

This project demonstrates a simple integration between a JavaScript application and a Python Dash application. The two applications communicate via a socket connection, allowing for interactive updates between the JavaScript application and the Dash application.

## Setup Instructions

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```sh
   ```

2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Applications

1. Start the Dash application:
   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to view the Dash application.

3. node start

## Project Structure

- `app.py`: Contains the Dash application code.
- `requirements.txt`: Lists the Python dependencies for the Dash application.
- `static/index.html`: Hosts the JavaScript application.
- `static/main.js`: Contains the JavaScript code for handling socket communication.

## Communication between Dash and JavaScript Application

The Dash application and the JavaScript application communicate via a socket connection. When a user interacts with the JavaScript application, it sends data to the Dash application, which can then update its layout accordingly. Similarly, actions in the Dash application can trigger updates in the JavaScript application.

## Purpose

The purpose of this project is to demonstrate how to integrate a JavaScript application with a Python Dash application, enabling interactive communication between the two applications.
