people = {
'Alice': {
'phone': '2341',
'addr': 'Foo drive 23'
},
'Beth': {
'phone': '9102',
'addr': 'Bar street 42'
},
'Cecil': {
'phone': '3158',
'addr': 'Baz avenue 90'
}
}

name = input('Name: ')
if name in people:
    request = input('Phone number (p) or address (a)? ')
    if request == 'p': key = 'phone'
    elif request == 'a': key = 'addr'
    else: key = request
    print(name + "'s " + key + " is " + people.get(name).get(key, 'not available'))

else:
    print("No "+ name+ " in the list")


