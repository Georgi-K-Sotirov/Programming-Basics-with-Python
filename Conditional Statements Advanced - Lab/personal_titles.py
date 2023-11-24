age = float(input())
gender = input()
pronounce = ''

if gender == 'f':
    if age < 16:
        pronounce = 'Miss'
    else:
        pronounce = 'Ms.'
else:
    if age <16:
        pronounce = 'Master'
    else:
        pronounce = 'Mr.'

print(pronounce)