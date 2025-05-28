def line_generator(filename, max_len):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')  # убираем перенос строки
            # разбиваем строку на куски по max_len
            for i in range(0, len(line), max_len):
                chunk = line[i:i+max_len]
                # переворачиваем слова в куске
                words = chunk.split()
                reversed_words = list(map(lambda w: w[::-1], words))  # переворачиваем каждое слово
                yield ' '.join(reversed_words)


for part in line_generator('file.txt', 10):
    print(part)
