 
# File Reader Flask App
 
## Overview
This Flask application functions as a basic file reader, enabling users to access and read text files stored on the server. Users can specify the file name and, if desired, a specific range of lines to view.
 
## Features
- **Reading Files**: Access file contents by appending the file name to the root URL.
- **Selecting Line Ranges**: Define a line range for file reading through the utilization of `start_line` and `end_line` query parameters.
 
## Installation
 
To run this application, you'll need Python and Flask installed on your system.
 
1. Clone the repository:
https://github.com/Narsi12/-Vetty_client_Assessment.git
 
2. Create a virtual environment: Navigate to your project directory and run:
python3 -m venv env
 
3. Activate the virtual environment(On Windows, run):
.\venv\Scripts\activate
 
 
4. Navigate to the cloned directory:
cd [File_Read_Flask]
 
5. Install the required packages:
pip install -r requirements.txt
 
6. Start the server with the following command:
flask run --debug
 
7. based on start_line and end_line endpoint:
http://localhost:5000/file3.txt?start_line=1&end_line=30