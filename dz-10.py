# f = open("read_file.txt", "r", encoding='utf-8')
# r = open("keywords.txt", "a", encoding='utf-8')
# lines = f.readlines()
#
# has_keywords = []
#
# for line in lines:
#     if 'Lorem' in line:
#         r.write(line)
#         has_keywords.append(line)
#
# print(has_keywords)
# r.write('\n')
# f.close()
# r.close()

keyword = 'Lorem'
file = open("sitemap.csv", "r", encoding='utf-8') # r - read, w - write
write_file = open("write_file.txt", "a", encoding='utf-8')
# print(write_file)
lines = file.readlines()
# print(lines)

for item in lines:
    string = item.replace('\n', '').split(';')
    url = string[0]
    try:
        word = string[1]
    except:
        word = f"ERROR "
        print(word + url)
    try:
        symbol = string[2]
    except:
        symbol = f"ERROR "
        print(symbol + url)
    result = f"Url - {url}, keyword - {word}, symbol - {symbol}\n"
    write_file.write(result)
    write_file.flush()

# is_lorem = [line.replace('\n', '') for line in lines if keyword in line]
# print(is_lorem)
#
# for line in is_lorem:
#     write_file.write(line + '\n')
#     write_file.flush()


file.close()
