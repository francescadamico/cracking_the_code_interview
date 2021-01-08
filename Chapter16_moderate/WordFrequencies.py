'''
Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?
'''

from collections import defaultdict

def word_freq(word, text):
  text_words = text.split(' ')
  text_dict = defaultdict(int)
  for txw in text_words:
    text_dict[txw] += 1
  return text_dict[word]


text = ''' An integer (from the Latin integer meaning "whole")[a] is colloquially defined as a number that can be written without a fractional component. For example, 21, 4, 0, and −2048 are integers, while 9.75, 5+
1
/
2
, and √2 are not.

The set of integers consists of zero (0), the positive natural numbers (1, 2, 3, ...), also called whole numbers or counting numbers,[2][3] and their additive inverses (the negative integers, i.e., −1, −2, −3, ...). The set of integers is often denoted by a boldface letter 'Z' ("Z") or blackboard bold {\displaystyle \mathbb {Z} }\mathbb {Z}  (Unicode U+2124 ℤ) standing for the German word Zahlen ([ˈtsaːlən], "numbers").[4][5][6][7]

ℤ is a subset of the set of all rational numbers ℚ, which in turn is a subset of the real numbers ℝ. Like the natural numbers, ℤ is countably infinite.

The integers form the smallest group and the smallest ring containing the natural numbers. In algebraic number theory, the integers are sometimes qualified as rational integers to distinguish them from the more general algebraic integers. In fact, (rational) integers are algebraic integers that are also rational numbers.'''

print(word_freq('algebraic', text))
