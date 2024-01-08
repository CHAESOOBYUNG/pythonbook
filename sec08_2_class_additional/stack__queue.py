# 스택
# 선입후출(First in Last out)(FILO)
# 후입선출(Last in First out)(LIFO)
# 구조를 갖는 자료 구조
class Stack:
    def __init__(self) -> None:
        self.__list = []
    
    def push(self, value):
        self.__list.append(value)

    def pop(self):
        output = self.__list[-1]
        del self.__list[-1]
        return output

stack = Stack()
stack.push(10) # [10]
stack.push(20) # [10, 20]
stack.push(30) # [10, 20, 30]
print(stack.pop()) # 30 [10, 20]
print(stack.pop()) # 20 [10]
print(stack.pop()) # 10

# 큐
# 선입선출(First in First out)(FIFO)
class Queue:
    def __init__(self) -> None:
        self.__list = []
    def enqueue(self, value):
        self.__list.append(value)
    def dequeue(self):
        output = self.__list[0]
        del self.__list[0]
        return output

queue = Queue()
queue.enqueue(10) # [10]
queue.enqueue(20) # [10, 20]
queue.enqueue(30) # [10, 20, 30]
print(queue.dequeue())   # 10 [20, 30]
print(queue.dequeue())    # 20 [30]
print(queue.dequeue())    # 30