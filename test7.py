def repair_logs(entries: list) -> list:
    c = []

    for entry in entries:
        z = ""  

        for ch in entry:
            if ch.isalpha():
                z += ch.lower()

        if z == "":
            continue

    
        if len(z) >= 4:
            z = z[::-1]

        c.append(z)

    return c


a = ["Sp@ac3e", "Mi$$oon", "R0ck!et", "Io!"]
print(repair_logs(a))





def decode_spellbook_words(entries):
    res = ""
    for ch in entries:
        if ch.isalpha():
            if len(ch) % 2 == 1:
                res += ch[0]
            else:
                res += ch[-1]
    return res.upper()

entries = ["spark", "42", "flame", "orb", "!", "rune"]
print(decode_spellbook_words(entries))









