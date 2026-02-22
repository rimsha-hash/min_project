def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read() 
            words = text.split()  # Split the text into words
            print(f"Total words: {len(words)}")  # Count and print the number of words
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "abc.txt"  # Replace with your file name
count_words(filename)