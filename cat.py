import sys

def with_files(files):
    """Executes when file(s) is/are specified."""
    try:
        # Read each file's contents and store them
        file_contents = [contents for contents in [open(file).read() for file in files]]
    except OSError as err:
        # This executes when there's an error (e.g. FileNotFoundError)
        exit(print(f"cat: error reading files ({err})"))

    # Write all file contents into the standard output stream
    for contents in file_contents:
        sys.stdout.write(contents)

def no_files():
    """Executes when no file(s) is/are specified."""
    try:
        # Get input, output the input, repeat
        while True:
            print(input())
    # Graceful exit for Ctrl + C, Ctrl + D
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()

def main():
    """Entry point of the cat program."""
    # Read the arguments passed to the program
    if not sys.argv[1:]:
        no_files()
    else:
        with_files(sys.argv[1:])

if __name__ == "__main__":
    main()
