import re

def remove_depercated_enumerations(line):
    words = line.split(" ")
    if words[0] == "#" and len(words) > 1:
        pattern = '[1-9].'
        if re.match(pattern, words[1]):
            line = " ".join(words[2:])
            line = " ".join([words[0], line])
    return line

def add_chapter_counter(file_name):
    with open(file_name, encoding="utf8") as my_file:
        text = my_file.read()
        lines = text.split("\n")
        print(len(lines))
        chapter_counter = 1
        new_lines = ""
        is_code_block = False
        for line in lines:
            if line.startswith('```') and not is_code_block:
                is_code_block = True
            elif line.startswith('```') and is_code_block:
                is_code_block = False
            if not is_code_block:
                line = remove_depercated_enumerations(line)
            words = line.split(" ")
            if words[0] == "#" and not is_code_block:
                line = " ".join(words[1:])
                line = " ".join([words[0], str(chapter_counter) + ".", line])
                chapter_counter += 1
            new_lines += line + "\n"
    return new_lines
        
def write_new_file(new_lines, file_name):
    with open(file_name, 'w', encoding="utf-8") as my_file:
        my_file.write(new_lines)


if __name__ == "__main__":
    file_name = "README.md"
    new_lines = add_chapter_counter(file_name)
    write_new_file(new_lines, file_name)
