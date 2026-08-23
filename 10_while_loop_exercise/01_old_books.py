searched_book = input()

checked_book = 0

while True:
    command = input()

    if command == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {checked_book} books.')
        break

    if command == searched_book:
        print(f'You checked {checked_book} books and found it.')
        break

    checked_book += 1