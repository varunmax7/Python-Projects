#Week-6 P2 Replace first letter with capital letter
import string
def firstletteruppercase(text):
    result=string.capwords(sample_text)
    return result
sample_text="Its gone too far"
print("Original text: ", sample_text)
print("New text: ", firstletteruppercase(sample_text))
