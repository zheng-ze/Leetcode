class MyQueue {
    int[] s1;
    int index1;
    int[] s2;
    int index2;

    public MyQueue() {
        s1 = new int[100];
        index1 = -1;
        s2 = new int[100];
        index2 = 0;
    }
    
    public void push(int x) {
        s1[index1 + 1] = x;
        index1++;
    }
    
    public int pop() {
        int result = peek();
        index2--;
        return result;
    }
    
    public int peek() {
        if (index2 == 0) {
            while (index1 >= 0) {
                s2[index2++] = s1[index1--];
            }
        }
        return s2[index2 - 1];
    }
    
    public boolean empty() {
        return index1 == -1 && index2 == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */