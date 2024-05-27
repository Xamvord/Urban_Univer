def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]

gen_obj = all_variants("abcdef")
for substr in gen_obj:
    print(substr)

