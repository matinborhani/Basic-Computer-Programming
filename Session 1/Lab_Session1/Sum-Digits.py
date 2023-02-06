def sumDigits(num):
    if num == 0:
        return num
    else:
        return num % 10 + sumDigits(num // 10)

if __name__ == '__main__':
    num = int(input("please enter number: "));
    sum = sumDigits(num);
    print(sum);
