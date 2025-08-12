from mypalindrome import *
from  Q1_and_Q2.myinputreader import *

def main():
    text= input("Enter a String: ").strip()
     
    print("{} {} a palindrome!".format(text, "is" if is_palindrome(text) else "is not"))
     


main()