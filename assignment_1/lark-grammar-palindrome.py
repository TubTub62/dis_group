#Lark palindrome grammar

from lark import Lark

grammar = """
start: palindrome
palindrome: empty | single_dit | recursive_palindrome

single_dit: "0" | "1"
recursive_palindrome: "0" palindrome "0" | "1" palindrome "1" | "00" | "11"
empty: "empty"

%import common.WS
%ignore WS

"""
parser = Lark(grammar)
try:
    # these will work
    print(parser.parse("0"))
    print(parser.parse("1"))
    print(parser.parse("empty"))
    print(parser.parse("00"))
    print(parser.parse("11"))
    print(parser.parse("000"))
    print(parser.parse("111"))
    print(parser.parse("0110"))
    print(parser.parse("1001"))
    print(parser.parse("000000"))
    print(parser.parse("101101"))

    # this will make an error
    #print(parser.parse("01"))

except Exception as e:
    print(f"Error:", e)

# The above grammar is a simple Lark grammar for palindromes.
#it will accept grammar like:
# "" (empty)
# 0, 1 (single digit 0's and 1's) 
# 00, 11 (2 digit palindromes 0's and 1's)
# 010, 101, 000, 111 (any uneven length where the first and last didgit
# match and the middle is a palindrome)
# 0000, 1111 (any even length where the first and last didgit match 
# and the middle is a palindrome)