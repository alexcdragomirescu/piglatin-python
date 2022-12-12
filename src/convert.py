import argparse

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def pigify(text):
    words = text.split(' ')
    piglatinWords = []

    for word in words:
        if (word[0] in vowels):
            pigWord = word + 'ay'
        else:
            pigWord = word[1:] + word[0] + 'ay'
        piglatinWords.extend([pigWord])
    return ' '.join(piglatinWords)


parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
args = parser.parse_args()

print(pigify(args.input))
