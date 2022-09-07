score = {'pos': 90, 'neg': 80, 'neu': 70}

labels = [key for key in score]
print(labels)
values = [score[key] for key in score]
print(values)

if labels:
    labels.pop()

print(labels)