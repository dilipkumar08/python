#queue

class Queue():
    def __init__(self):
        self.que=[]
    def enqueue(self,value):
        self.que.append(value)
    def dequeue(self):
        self.que.pop()
    def view(self):
        print(self.que)
        
if __name__=="__main__":
    q1=Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q1.view()
    q1.dequeue()
    q1.dequeue()
    q1.view()
