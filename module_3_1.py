calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(stroka):
    count_calls()
    result = (len(stroka), stroka.upper(), stroka.lower())
    return result


def is_contains(stroka, spisok):
    count_calls()
    flag = False
    for i in range(len(spisok)):
        if stroka.lower() == str(spisok[i]).lower():
            flag = True
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
