#6.3
#glossary list
definitions = []
definitions.append('lists')
definitions.append('method')
definitions.append('code')
definitions.append('variable')
definitions.append('ide')
#creating the glossary
glossary = {}
glossary[definitions[0]] = 'a series of items of the same type'
glossary[definitions[1]] = 'type of usage of the code'
glossary[definitions[2]] = 'the structure of the program'
glossary[definitions[3]] = 'specified meaning of the option'
glossary[definitions[4]] = 'visual editor for code'
#printing
for definition in definitions:
    print(f"{definition.title()}: {glossary[definition]}.")

