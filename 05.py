from re import T


anything = input('1개 이상 100개 이하의 알파벳 소문자로 조합된 단어를 입력하세요 : ')

if (list(anything) == list(reversed(anything))):
    palindrome = 1
else:
    palindrome = 0

print(palindrome)
