contact = ["1", "2", "3"]


def find_key_word(contact: list, key_word: str) -> bool:
    if key_word in contact:
        return True
    else:
        return False


print(find_key_word(contact, "hv"))
