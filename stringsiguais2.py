n = int(input())
string_a = input()
string_b = input()

i = 0
count = 0

while (i < n):
    if (string_a[i] != string_b[i]):

        if (i < n-1 and string_a[i] == string_b[i+1]
                and string_a[i+1] == string_b[i]):
            i += 1

        count += 1

    i += 1

print(count)
