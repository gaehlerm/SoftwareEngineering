import PyPDF2
import re

# offset for non-numerated pages
offset = 0

# input files: pure text and pdf file
pure_text_file = "README.md"
pdf_file = "README.pdf"

# all_words_file gets created by this script it can be filtered by hand to create the desired_index_file
all_words_file = "all_words.txt"

# The desired_index_file is a hand filtered file that contains only the words that we want to index
desired_index_file = "desired_index.txt"

# The index_file is the actual result
index_file = "index.txt"

def remove_special_characters(s):
    s = re.sub(r'[^\w]', '', s)
    s = re.sub(r'[0-9]', '', s)
    return s

def search_page_numbers(word, complete_text):
    page_numbers = []
    for i in range(0, len(complete_text.pages)):
        PageObj = complete_text.pages[i]
        Text = PageObj.extract_text()
        if re.search(word ,Text, re.IGNORECASE):
            page_numbers.append(i+1+offset)
    return page_numbers

def save_all_words(words):
    with open(all_words_file, "w") as all_words:
        for word in words:
            all_words.write(word + "\n")

def save_only_desired_words():
    desired_words = []
    with open(desired_index_file, "r") as desired:
        desired_words = desired.read().splitlines()

    complete_text = PyPDF2.PdfReader(pdf_file)

    with open(index_file, "w") as index:
        for word in desired_words:
            index.write(word + " ")
            # this search takes a long time for many words!!
            index.write(str(search_page_numbers(word, complete_text)))

no_duplicates = []

with open(pure_text_file) as readme:
    content = readme.read()
    words = [word.lower() for word in content.split()]

    no_special_character_words = [remove_special_characters(word) for word in words]
    no_duplicates = list(set(no_special_character_words))

    no_duplicates.sort()

    complete_text = PyPDF2.PdfReader(pdf_file)

save_all_words(no_duplicates)
save_only_desired_words()
