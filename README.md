# 3D View and Dash Application Communication

This project demonstrates a simple integration between a 3D view from Autodesk Construction Cloud and a Python Dash application. The two applications communicate via a socket connection, allowing for interactive updates between the 3D scene and the Dash application.

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js
- npm (Node Package Manager)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```sh
   cd static
   npm install
   ```

### Running the Applications

1. Start the Dash application:
   ```sh
   python app.py
   ```

2. Start the JavaScript application:
   ```sh
   cd static
   npm start
   ```

3. Open your web browser and navigate to `http://localhost:8050` to view the Dash application and the integrated 3D view.

## Project Structure

- `app.py`: Contains the Dash application code.
- `requirements.txt`: Lists the Python dependencies for the Dash application.
- `static/index.html`: Hosts the JavaScript application with the 3D view.
- `static/main.js`: Contains the JavaScript code for initializing the 3D view and handling socket communication.

## Communication between Dash and 3D View

The Dash application and the JavaScript application communicate via a socket connection. When a user interacts with the 3D view, the JavaScript application sends data to the Dash application, which can then update its layout accordingly. Similarly, actions in the Dash application can trigger updates in the 3D view.

## Purpose

The purpose of this project is to demonstrate how to integrate a 3D view from Autodesk Construction Cloud with a Python Dash application, enabling interactive communication between the two applications.
