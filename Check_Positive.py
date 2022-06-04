def checkno(no):
    if(no>0):
        print("Positive number")
    elif(no<0):
        print("Negative number")
    else:
        print("zero")
def main():
    print("enter number")
    no = int(input())
    checkno(no)

if __name__ == "__main__":
    main()



