def checkNo(no):
    if(no%5==0):
        return True
    else:
        return False

def main():
    print("Enter number")
    no = int(input())
    ret = checkNo(no)
    if(ret == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

