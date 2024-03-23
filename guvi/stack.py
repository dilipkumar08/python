#stack

class Stack:
    def __init__(self):
        self.arr=[]
        self.l=0
    def push(self,val):
        if val:
            self.arr.append(val)
            self.l+=1
        return val
    def pop(self):
        if self.l==0:
            return "The stack is empty"
        else:
            self.l-=1
            return (self.arr.pop(-1))
    def peek(self,ind):
        if self.l<ind:
            return "Out of index"
        else:
            return self.arr[ind]
    def display(self):
        return self.arr
    
if __name__=='__main__':
    stk=Stack()
    n=0
    while (n!=5):
        print("\n1.push\n2.pop\n3.peek\n4.display\n5.exit")
        n=int(input("Choose a operation: "))
        if n==1:
            push_count=int(input("Enter the number of values to be pushed: "))
            for i in range(push_count):
                p=int(input(f"Enter the value {i} : "))
                print(stk.push(p))
        elif n==2:
            pop_count=int(input("Enter the number of values to be popped: "))
            for i in range(pop_count):
                temp=stk.pop()
                if temp==None:
                    print("Stack is Empty")
                    break
                else:
                    print("Popped:",temp)
        elif n==3:
            peek_index=int(input("Enter the index to peek: "))
            print(stk.peek(peek_index))
        elif n==4:
            print(stk.display())
        elif n==5:
            break
        else:
            print("Please Enter a valid option!!")
           


    
