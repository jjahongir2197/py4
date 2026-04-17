def count_words(filename):
    try:
        file = open(filename, "r")
        text = file.read()
        file.close()

        words = text.split()

        counts = {}

        for word in words:
            word = word.lower()

            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        for w in counts:
            print(w, ":", counts[w])

    except:
        print("File not found!")


count_words("text.txt")
