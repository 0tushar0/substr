# given string, find length of longest substring without repeating build_str

s = 'abscdsef'

build_str = ""
final_str = ""

if len(s) == 0:
    print(0)
elif len(s) == 1:
    print(1)

for i in range(len(s)):
    build_str += s[i]
    j = i + 1
    while j < len(s) and s[j] not in build_str:
        build_str += s[j]
        j += 1
    if len(build_str) > len(final_str):
        final_str = build_str
    build_str = ""
print(len(final_str))

