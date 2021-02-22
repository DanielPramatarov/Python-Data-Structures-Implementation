class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):

        if self.size_stack() < 1:
            return None

        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_stack(self):
        return len(self.stack)


st = Stack()
st.push(3212)
st.push(32313)
st.push(1342425654)
st.push(78686)
st.push(99878)

print(st.pop())
