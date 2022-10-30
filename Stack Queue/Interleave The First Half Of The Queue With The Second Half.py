from queue import LifoQueue

def interLeaveQueue(queue):
    n = int(len(queue)/2)
    
    st = LifoQueue()
    for i in range(n):
        st.put(queue[0])
        del queue[0]
        
    
    while st.qsize()>0:
        queue.append(st.get())
        
        
   
    for i in range(n):
        queue.append(queue[0])
        del queue[0]
        
    
    for i in range(n):
        st.put(queue[0])
        del queue[0]
        
    
    while st.qsize()> 0:
        queue.append(st.get())
        queue.append(queue[0])
        del queue[0]
        
    return queue
