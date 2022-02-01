
def isPalindrome(s):
    newStr=s[::-1]
    if s==newStr:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isPalindrome("racecar , racecar , mom , racecar , racecar"))