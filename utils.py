def read_file_with_encoding(file_path, start_line=None, end_line=None):
    """
    Read the file with different encodings and return content.
    """
    encodings = ['utf-8', 'utf-16']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                lines = file.readlines()
                
                if start_line is not None and end_line is not None: # If any value is negative raise error
                    if start_line <= 0 or end_line <= 0 or start_line > end_line:
                        raise ValueError("Invalid start_line or end_line values.")
                    lines = lines[start_line - 1:end_line]
                elif start_line is None and end_line is not None:
                    if end_line <= 0:
                        raise ValueError("Invalid end_line value.")
                    lines = lines[:end_line]
                elif start_line is not None and end_line is None:
                    if start_line <= 0:
                        raise ValueError("Invalid start_line value.")
                    if start_line > len(lines):  # Check if start_line is out of range
                        raise IndexError("start_line is out of range.")
                    lines = lines[start_line - 1:]
                
                return ''.join(lines)
        except UnicodeError:
            continue  # If encoding fails, try the next one
            
    raise UnicodeError("Unable to read file with specified encodings.")
