file = open("Strings", "r")

vowels = ["a", "e", "i", "o", "u"]
doubles = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz"]
cant_see = ["ab", "cd", "pq", "xy"]
total = 0
for line in file:
    vowel_count = 0
    is_nice = False
    line = line.strip()
    for vowel in vowels:
        for char in line:
            if char == vowel:
                vowel_count += 1
    for double in doubles:
        if double in line:
            is_nice = True
    for cant in cant_see:
        if cant in line:
            is_nice = False
    if is_nice and vowel_count >= 3:
        total += 1
print(total)
