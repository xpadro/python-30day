from datetime import date

return_list = list(map(int, input().rstrip().split()))
due_list = list(map(int, input().rstrip().split()))

return_date = date(return_list[2], return_list[1], return_list[0])
due_date = date(due_list[2], due_list[1], due_list[0])

fine = 0

if return_date > due_date:
    if return_date.year > due_date.year:
        fine = 10000
    elif return_date.month > due_date.month:
        fine = 500 * (return_date.month - due_date.month)
    else:
        fine = 15 * (return_date.day - due_date.day)

print(fine)
