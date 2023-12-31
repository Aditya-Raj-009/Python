import re   # for regular expressions

mystr = "Landsman was educated "\
        "at Chigwell School and Oriel College," \
        " Oxford, then gained a PhD in linguistics from Clare" \
        " College, Cambridge in 1989 with a thesis entitled Theories of diglossia, " \
        "linguistic variation and speaker attitudes, with special reference to recent " \
        "developments in Modern Greek. He joined the Foreign & "\
    " ph : +44 5768686-7575777 Email: tata@tata.com.uk,pritnceAfj848484@gmail.com,aAkfkf%758@ind.com"\
    "fax = +1 (4959) 4575"

# Functions in regular expressions:
'''
findall() : jo specific string matches h usse utha kr ek string return karta h.
search() : returns a math object.
split() : return a list after spliting it for a given value.
sub(), finditer()
'''
# finditer() :
# print(r"\n")    # if u want to print escape sequence character.
patt = re.compile(r'fax')   # if u want to search. here it is use to search fax in mystr
matches = patt.finditer(mystr)    # return iterator for that match
for match in matches:
    print(match)    # <re.Match object; span=(357, 360), match='fax'> span gives location your searched obj.
    # now if u slice mystr[357:360] u get your search (fax):
    print(mystr[357:360])   # fax

# patt = re.compile(r'.') # '.' defines for any character.dot (.) is a meta character here
# patt = re.compile(r'.Chigwell') # '.' search for string which available after any character.
# patt = re.compile(r'^Chigwell') #  search string (Chigwell) if start with it.
# patt = re.compile(r'4575$') #  search string (Chigwell) if end with it.
# patt = re.compile(r'ai*') #  search in which there is 'a' in which there as much i. * represent for as much
# patt = re.compile(r'ai+') #  search in which there is 'a' in which there atleast 1 'i' .'+' represent for atleast one.
# patt = re.compile(r'ai{2}') #  search in which there is 'a' in which there exactly 2 'i' . {} represent for exactly.
# patt = re.compile(r'ai{2}|fax') #  | for or.


# special sequences:
# patt = re.compile(r'\ALandsman')
# patt = re.compile(r'Landsman\b')

# searching a pattern from mystr:
patt = re.compile(r'\d{7}-\d{7}')  # \d represent for digits

matches = patt.finditer(mystr)    # return iterator for that match
for match in matches:
    print(match)    # <re.Match object; span=(326, 341), match='5768686-7575777'>
    # now if u slice mystr[357:360] u get your search (fax):
    print(mystr[326:341])   # 5768686-7575777

# search for email in mystr by using findall() method:
email = re.findall(r"[0-9A-Za-z._+%]+@[0-9A-Za-z._+%]+[.][a-zA-Z.0-9]+",mystr)         # [] use to make group.
print(email)        # ['tata@tata.com.uk', 'pritnceAfj848484@gmail.com', 'aAkfkf%758@ind.comfax']

