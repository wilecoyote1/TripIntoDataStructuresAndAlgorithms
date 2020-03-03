import sys
sys.path.append('../')

from searchtext import searchtext

text = """
comme un vol de gerfauts, hors du charnier natal
"""

find ="gerfaut"
find2 = "olivier"
print(f"the word {find} is found in the text at the position : {searchtext(text,find)}")
print(f"the word {find2} is found in the text at the position : {searchtext(text,find2)}")