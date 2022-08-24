import re

def passwordChecker(password):
    eightRegex = re.compile(r'.{8,}')
    lowerRegex = re.compile(r'[a-z]+')
    upperRegex = re.compile(r'[A-Z]+')
    numRegex = re.compile(r'\d+')

    isStrong = True

    if not eightRegex.findall(password) or\
        not lowerRegex.findall(password) or\
        not upperRegex.findall(password) or\
        not numRegex.findall(password):
            isStrong = False
    
    if isStrong:
        print(f'{password} is a strong password')
    else:
        print(f'{password} is a weak password')

passwordChecker('123456789')
passwordChecker('password')
passwordChecker('3Sdfji48gsf')
passwordChecker('fffhhhhh')