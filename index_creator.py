import pypdf
import re
from dataclasses import dataclass

# OFFSET for non-numerated pages
OFFSET = 0

# input files: pure text and pdf file
# PURE_TEXT_FILE = "README.md"
PDF_FILE = "README.pdf"

# ALL_WORDS_FILE gets created by this script it can be filtered by hand to create the DESIRED_INDEX_FILE
# ALL_WORDS_FILE = "all_words.txt"

# The DESIRED_INDEX_FILE is a hand filtered file that contains only the words that we want to index
DESIRED_INDEX_FILE = "desired_index.txt"

# The INDEX_FILE is the actual result
INDEX_FILE = "index.txt"

# def remove_special_characters(s):
#     s = re.sub(r'[^\w]', '', s)
#     s = re.sub(r'[0-9]', '', s)
#     return s


# def save_all_words(words):
#     with open(ALL_WORDS_FILE, "w") as all_words:
#         for word in words:
#             all_words.write(word + "\n")

# def deal_with_commas(word):
#     words = word.split(",")
    # return words[1].strip() + " " + words[0]

# def get_words_from_PURE_TEXT_FILE(PURE_TEXT_FILE):
#     no_duplicates = []

#     with open(PURE_TEXT_FILE) as readme:
#         content = readme.read()
#         words = [word.lower() for word in content.split()]

#         no_special_character_words = [remove_special_characters(word) for word in words]
#         no_duplicates = list(set(no_special_character_words))

#         no_duplicates.sort()
    
#     return no_duplicates


@dataclass
class NumberRange:
    min: int
    max: int

def create_number_range(page_numbers):
    number_range = []
    for page_number in page_numbers:
        min = page_number
        max = min
        number_range.append(NumberRange(min, max))
    return number_range

def convert_number_range_to_string(number_range):
    result = ""
    for i in range(0, len(number_range)):
        if number_range[i].min == number_range[i].max:
            result += str(number_range[i].min)
        else:
            result += str(number_range[i].min) + "-" + str(number_range[i].max)
        if i != len(number_range) - 1:
            result += ", "
        if i == len(number_range) - 1:
            result += "\n"
    return result

def process_page_numbers(number_range):
    still_processing = False
    for i in range(1, len(number_range)):
        if number_range[i].min - number_range[i-1].max < 4:
            number_range[i-1].max = number_range[i].max
            del number_range[i]
            still_processing = True
            break
    if still_processing:
        return process_page_numbers(number_range)
    return convert_number_range_to_string(number_range)


def search_page_numbers(words, complete_text):
    page_numbers = []
    split_words = words.split(";")
    for i in range(OFFSET, len(complete_text.pages)):    
        for word in split_words:
            page_obj = complete_text.pages[i]
            text = page_obj.extract_text()
            if re.search(word, text, re.IGNORECASE):
                page_numbers.append(i+1+OFFSET)
    return page_numbers

def save_desired_words():
    desired_words = []
    with open(DESIRED_INDEX_FILE, "r") as desired:
        desired_words = desired.read().splitlines()

    complete_text = pypdf.PdfReader(PDF_FILE)

    with open(INDEX_FILE, "w") as index:
        for words in desired_words:
            # if word.count(",") > 0:
            #     word = deal_with_commas(word)
            word = words.split(";")[0]
            index.write(word + ": ")
            # this search takes a long time!!
            page_numbers = search_page_numbers(words, complete_text)
            number_range = create_number_range(page_numbers)
            index.write(process_page_numbers(number_range))

if __name__ == "__main__":
    # not sure if this is really useful
    # all_words = get_words_from_PURE_TEXT_FILE(PURE_TEXT_FILE)
    # save_all_words(all_words)

    save_desired_words()
