NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']
def dedup_and_title_case_names(names):
    names = [name.title() for name in names]
    result = []
    for name in names:
        if name not in result:
            result.append(name)
    return result

def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    names = sorted(names, key = lambda name: name.split(" ")[-1], reverse = 1)
    return names    

def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    names = [name.split(" ")[0] for name in names]
    return min(names, key = len)
print (dedup_and_title_case_names(PY_CONTENT_CREATORS))
print (sort_by_surname_desc(PY_CONTENT_CREATORS))
print (shortest_first_name(NAMES))