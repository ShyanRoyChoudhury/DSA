from queue import LifoQueue

def interLeaveQueue(queue):
    n = int(len(queue)/2)
    
    st = LifoQueue()
    for i in range(n):  #   step 1: removing the first half and storing in a stack
        st.put(queue[0])
        del queue[0]
        
    
    while st.qsize()>0:     #   step 2: append the reverse order from stack in queue, behind the 2nd half already stored at queue
        queue.append(st.get())
        
        
   
    for i in range(n):      #   step 3: pop and push, and bringing the reversed 1st half in this original pos in front(left side of queue).
        queue.append(queue[0])
        del queue[0]
        
    
    for i in range(n):      # step 4:  step 1 again to reverse the order of 1st half and storing it in stack
        st.put(queue[0])
        del queue[0]
        
    
    while st.qsize()> 0:    # final step:   one by one pushing the element from stack in queue as according to the question(Interleaving).
        queue.append(st.get())
        queue.append(queue[0])
        del queue[0]
        
    return queue


"""
T.C: O(N)
S.C: O(N)
"""
