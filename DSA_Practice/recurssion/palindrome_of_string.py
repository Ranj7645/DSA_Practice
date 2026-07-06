def palindrome(str,index):

    if index == 0:
        return str[0]
    return str[index] + palindrome(str,index-1)

def palindrome1(str,index):

    if index < (len(str)//2):
        return True
    if str[len(str)-index-1] != str[index]:
        return False
    return palindrome1(str,index-1)
# str = "abbba"
# result = palindrome(str,len(str)-1)
# print("calling palindrome",str == result)
# result1 = palindrome1(str,len(str)-1)
# print("is str palindrome ? ",result1)

def digitSum(num):
    if num == 0:
        return 0
    return num%10 + digitSum(num//10)

print("digit sum of number",digitSum(14526))
