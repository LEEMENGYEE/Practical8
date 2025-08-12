from myinputreader import *  #* file all function put in 
from mystringprocessor import *

def main():
    text = read_string("Enter a string: ")

    print("\n No Of Word: ", count_words(text))

    print("Average word length: {:.2f}\n".format(calculate_average_word_length(text)))


    for vowel,frequeancy in count_vowel_aeiou(text).items():
        print("No of {}: {:d}".format(vowel,frequeancy))


main()