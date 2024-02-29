import validators # library that holds validators for various inputs

# function that validates a URL
def valid_url(url):
    if validators.url(url):
        return True
    else:
        return False

# function to validate the given depth (must be greater than 0)
def validate_depth(depth) :
    if depth <= 0:
        return -1
    

###Main function to run test before passing to main.py
def main():
    with open('URL_List.txt','r') as file:
        pass
    pass

if __name__ == "main":
    main()