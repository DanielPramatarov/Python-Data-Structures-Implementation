class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.size_queue() < 1:
            return "Queue is empty"
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]


    def size_queue(self):
        return len(self.queue)



st = Queue()
st.enqueue(3212)
st.enqueue(32313)
st.enqueue(1342425654)
st.enqueue(78686)
st.enqueue(99878)

print(st.peek())

print(st.dequeue())
print(st.dequeue())
print(st.dequeue())
print(st.dequeue())
print(st.dequeue())
print(st.dequeue())




print(f"Size of Queue is {st.size_queue()}")

