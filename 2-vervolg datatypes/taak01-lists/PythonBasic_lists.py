maanden= ['januari', 'februari', 'maart', 'april', 'mei', 'juni','july','augustus','september','oktober','november','december', 'weekdagen']
weekdagen= ['Maandag', 'dinsdag','woensdag','donderdag', 'vrijdag', 'zaterdag', 'zondag']
maanden[12] = weekdagen
print (maanden)
print (maanden[6])

maanden[6] = "juli"
print (maanden[6])

for i in maanden:
    print (i)

len(maanden[1])
