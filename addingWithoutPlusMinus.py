def getSum(a, b):
   while b!= 0:
       carry = a & b
       a = a ^ b
       b = carry << 1
   return a

if __name__ == '__main__':
    a = 3
    b = 4
    print(getSum(a,b))
