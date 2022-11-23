from Queue import *
queue=Queue(10)

for person in ["Don", "ken", "Ivan", "Raj", "Amir", "Adi"]:
    queue.insert(person)

print(f"After inserting {len(queue)} persons on the queue, \n"
      f"it contains {queue}")
print(f"Is queue full? {queue.isFull()}")

print(f"Removing items from queue: ")
while not queue.isEmpty():
    print(queue.remove(), end=' ')
print()