# Flyweight Pattern
We use this pattern in applications where we have large number of objects and these objects take significant amount of memory, with this pattern we can reduce the amount of memory.

lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

## Pros
- You can save lots of RAM, assuming your program has tons of similar objects

## Cons
- You might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time somebody calls a flyweight method.
- The code becomes much more complicated. New team members will always be wondering why the state of an entity was separated in such a way.

