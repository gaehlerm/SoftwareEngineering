
def create_table_of_contents(file_name):
    with open(file_name, encoding="utf8") as my_file:
        text = my_file.read()
        lines = text.split("\n")
        table_of_contents = []
        is_code_block = False
        for line in lines:
            if line.startswith('```') and not is_code_block:
                is_code_block = True
            elif line.startswith('```') and is_code_block:
                is_code_block = False
            words = line.split(" ")
            if not is_code_block and words[0] == '#':
                table_of_contents.append([words[1], " ".join(words[2:]), "-".join(words[1:])])
    formated_table_of_contents = []
    for line in table_of_contents:
        formated_table_of_contents.append(line[0] + " [" + line[1] + "](#" + line[2] + ")")
    print(formated_table_of_contents, "\n")
    return formated_table_of_contents

def write_table_of_contents(formated_table_of_contents, file_name):
    with open(file_name, 'r', encoding="utf-8") as my_file:
        text = my_file.read()
    with open(file_name, 'w', encoding="utf-8") as my_file:
        my_file.write("\n".join(formated_table_of_contents))
        my_file.write("\n\n")
        my_file.write(text)

if __name__ == "__main__":
    file_name = "README.md"
    formated_table_of_contents = create_table_of_contents(file_name)
    write_table_of_contents(formated_table_of_contents, file_name)