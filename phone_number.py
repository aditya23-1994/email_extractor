import pyperclip, re
#phone number regex

PhoneRegex = re.compile(r'''(
                   (\d{3}|\(\d{3}\))?
                   (\s|-|\.)?
                   (\d{3})
                   (\s|-|\.)
                   (\d{4})
                   (\S*(ext|X|ext.)\S*(\d{2, 5}))?
                   )''', re.VERBOSE)

EmailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9._%+-]+
                        (\.[a-zA-Z]{2,4})
                        )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in PhoneRegex.findall(text):
    phoneNum = '.'.join([groups[1], groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
for groups in EmailRegex.findall(text):
    matches.append(groups[0])

#copy to the clipboard
if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches))
    print('copied to the clipboard: ')
    print('\n'.join(matches))
else:
    print('no phone number or email address found')
    