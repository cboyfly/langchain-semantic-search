import difflib
import string

def clean_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert text to lower case
    text = text.lower()
    return text

def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

doc1 = read_file('path/to/your/file.txt')
doc1_clean = clean_text(doc1)

doc2 = read_file('path/to/your/file.txt')
doc2_clean = clean_text(doc1)


d = difflib.Differ()
diff = d.compare(doc1_clean, doc2_clean)

print('\n'.join(diff))