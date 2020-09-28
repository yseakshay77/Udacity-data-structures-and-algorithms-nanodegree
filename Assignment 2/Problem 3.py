import sys


# encoding string process
def huffman_encoding(data):
    temp_dict = {}  # temporary dictionary
    _tree = {}  # tree dictionary
    temp_str = '1'  # temporary string
    encoded_str = ""  # encoded string

    # getting each character from data string and updating temporary dict with each character and how many times this
    # character has been added in dictionary
    for char in data:
        temp_dict[char] = temp_dict.get(char, 0) + 1

    # sorting dict by value and creating temporary string
    for num in sorted(temp_dict.items(), key=lambda x: x[1]):
        _tree[num[0]] = temp_str
        temp_str = '0' + temp_str

    # creating encoded string from temporary tree by going through each character from data string
    for d in data:
        encoded_str += _tree[d]

    # returning encoded string and temporary tree
    return encoded_str, _tree


# decoding string process
def huffman_decoding(data, tree):
    temp_dict = {}  # temporary dictionary
    temp_str, decoded_str = "", ""  # temporary empty string and decoded empty string!

    # getting characters from tree and updating temporary tree
    for c in tree:
        temp_dict[tree[c]] = c

    # based on temporary string, getting character from dictionary and decoding string
    for d in data:
        if d == '1':
            decoded_str += temp_dict[temp_str + d]
            temp_str = ''
        else:
            temp_str += d

    # returning decoded string
    return decoded_str


# tests
if __name__ == "__main__":
    codes = {}

    #Test Case
    # a_great_sentence = "The bird is the word"
    """
    The size of the data is: 69
    The content of the data is: The bird is the word    
    The size of the encoded data is: 48    
    The content of the encoded data is: 100000010000000100000000000101000000001000000000100000000001000000000001000000001001000000000001000100000010000000100000000000100001000001000000000100000000001    
    The size of the decoded data is: 69    
    The content of the encoded data is: The bird is the word
    """
    # Test Case for Empty String
    # a_great_sentence = ""
    """
    String is empty
    """
    # Test case for Repeating Character ('aaaaa')
    a_great_sentence = "aaaaa"
    """
    The size of the data is: 54    
    The content of the data is: aaaaa    
    The size of the encoded data is: 28        
    The content of the encoded data is: 11111    
    The size of the decoded data is: 54    
    The content of the encoded data is: aaaaa
    """

    if not a_great_sentence:
        print("String is empty")
        exit()
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
