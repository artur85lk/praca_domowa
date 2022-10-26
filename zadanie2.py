def is_palindrome(tekst):
    new = [i for i in tekst.lower() if str.isalnum(i)]
    if new == new[::-1]:
        return True
    return False

print(is_palindrome("kajak"))
print(is_palindrome("Kobyła,ma mały bok!"))