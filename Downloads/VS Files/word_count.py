import re
msg = input()
msg = re.sub(r"[^\w\s]", "", msg)
words = msg.split()
word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] =1
print("Word frequency :")
for word, count in word_count.items():
    print(f"{word} : {count}")