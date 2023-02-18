# Visitor Design Pattern
Visitor Design Pattern allow us to add new operations to object storage without modifying.
It help us separate operation algorithms from object.<br/>
If our data storage is not stable and we have to add new operations continuously we had better use this design pattern.<br/>
Visitor DP help use implement single responsibility and open/close principals. 

Example:Imagine a seasoned insurance agent who’s eager to get new customers. He can visit every building in a neighborhood, trying to sell insurance to everyone he meets. Depending on the type of organization that occupies the building, he can offer specialized insurance policies

## Help:
1. Separate operation logic from multiple object storage in one object
2. Add new operations without modifying

## Pros 
- Open/Closed Principle. You can introduce a new behavior that can work with objects of different classes without changing these classes.
- Single Responsibility Principle. You can move multiple versions of the same behavior into the same class.

## Cons
- You need to update all visitors each time a class gets added to or removed from the element hierarchy.
- Visitors might lack the necessary access to the private fields and methods of the elements that they’re supposed to work with.

## Example




