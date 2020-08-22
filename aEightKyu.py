def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return (a * 50) + 6


def array(string):
    strings = string.split(',')
    del strings[0]
    if len(strings) > 0:
        del strings[len(strings)-1]
    result = ''
    for i in strings:
        result = result + str(i) + ' '
    if len(result) > 0:
        return result.strip()
    else:
        return None


print(problem(1))
print(array(''))
