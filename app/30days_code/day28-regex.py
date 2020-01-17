N = int(input())

emails = []

for N_itr in range(N):
    firstNameEmailID = input().split()

    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]

    if emailID.endswith('@gmail.com'):
        emails.append([firstName, emailID])

emails.sort(key=lambda tup: tup[0])

for email in emails:
    print(email[0])