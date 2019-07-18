import re


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.a-zA-Z{2,4})
)''', re.VERBOSE)

emailRegex.search('sale@hytera.com voice@hytera.com').groups()



