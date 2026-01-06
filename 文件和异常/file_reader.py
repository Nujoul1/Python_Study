from pathlib import Path

path = Path('./文件和异常/pi_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)