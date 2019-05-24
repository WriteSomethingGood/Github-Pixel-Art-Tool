import json

def read_json(filepath):
  with open(filepath, 'rb') as file:
    return json.load(file, encoding = 'utf-8')


def convertMessage(message="HIRE ME", charactersDictionary = "dictionary.json"):
    letters = read_json(charactersDictionary)

    last_letter = " "
    timeline = []
    weekSpace = [0, 0, 0, 0, 0, 0, 0]
    for c in message:

        if c.isalnum() and last_letter.isalnum():
            timeline.append( weekSpace )
        last_letter = c

        #this is the width size of the letter
        width = len(letters[c][0])
        for i in range( width ):
            week = []
            for line in letters[c]:
                week.append(line[i])
            timeline.append(week)

    timeline.append(weekSpace)
    return timeline


if __name__ == "__main__":
    timeline = convertMessage()
    for week in timeline:
        print(week)
