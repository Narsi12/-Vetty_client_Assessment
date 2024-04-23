from flask import Flask, request, render_template
from utils import read_file_with_encoding
import os

app = Flask(__name__)

@app.route('/', defaults={'filename': 'file1.txt'},methods=['GET'])
@app.route('/<filename>', methods=['GET'])
def display_file(filename):
    """
    Display the contents of a text file.

    Args:
        filename (str): The name of the text file to display. Defaults to 'file1.txt' if not provided.

    Returns:
        str: Rendered HTML template with the contents of the specified text file.
        If an error occurs, the error message is rendered using the 'error.html' template.
    """
    try:
        start_line = request.args.get('start_line', type=int)
        end_line = request.args.get('end_line', type=int)
        
        # Generate the file path dynamically based on filename
        file_path = os.path.join('static_files', filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{filename}' do not exist in {file_path}.")
        
        lines = read_file_with_encoding(file_path,start_line,end_line)
 
    except Exception as e:
        return render_template('error.html', error=str(e)) # templates
    
    return render_template('file_content.html', content=lines)

if __name__ == "__main__":
    app.run()