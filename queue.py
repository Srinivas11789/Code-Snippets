# Queue Program
# Create a Queue
# Enqueue
# Dequeue


def enqueue(que,number):
   que.append(number)

def dequeue(que):
  if len(que) == 0:
      print "Queue Already Empty !!!!"
  else:
      que.pop(0)

def queue(que):
    print que

# Main Program
que = []
while(1):
  option = raw_input("Enter the option (enqueue/dequeue): ")
  if option == "enqueue":
   number = raw_input("Enter the number to add : ")
   enqueue(que,number)
   queue(que)
  else:
   dequeue(que)
   queue(que)
  




