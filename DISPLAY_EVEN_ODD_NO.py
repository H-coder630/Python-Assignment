def chkNum(no):
    if(no%2 == 0):
        return True
    else:
        return False


def main():
    print("Enter the number")
    no = int(input())
    ret = chkNum(no)
    if(ret == True):
        print("the number is Even number")
    else:
        print("the number is odd number")

if __name__ == "__main__":
    main()
