import zipfile

def main(suffix):

    # assigning filename to a variable
    file_name = 'testdir.zip'

    # opening Zip using 'with' keyword in read mode
    with zipfile.ZipFile(file_name, 'r') as file:
        file_list = zipfile.ZipFile(file_name).namelist()
        # suffix = ['.c']
        for x in file_list:
            if x.endswith(tuple(suffix)):
                print(x)

if __name__ == '__main__':

    print("\nTest case 1")
    suffix = ['.c']
    main(suffix)

    print("\nTest case 2")
    suffix = ['.h']
    main(suffix)


