
def thesaurus(*args):
    persons = {}
    for arg in args:
        if persons.get(arg[0]) == None:
            persons.update({arg[0]: [arg]})
        else:
            persons[arg[0]].append(arg)
    return persons


print(thesaurus("Алина", "Ксения", "Екатерина", "Антон", "Олег", "Ольга", "Джаред"))