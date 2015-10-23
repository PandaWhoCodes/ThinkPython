"""
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
print letter + suffix
The output is:
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack
Of course, that's not quite right because "Ouack"
and "Quack" are misspelled. """


prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    g = letter + suffix
    if(g=="Oack" or g=="Qack"):
        print("Quack")
    else:
        print(g)
