# Composite Pattern
Use this pattern in situation where we want to represent a hierarchy of objects and we want to treat objects of hierarchy the same way.

Composite pattern lets you compose objects into tree structures and then work with these structures as if they were individual objects.

We can see composite pattern in software like power-point and photoshop. In these applications you can select some objects (example: Squares) and move, resize or rotate them. Also you can combine two or more groups and create a new big group.

In file system manager we can see this behavior as files and folder, folders can contain several files and folder and we can move and delete folder and its child.

## Pros
- You can work with complex tree structures more conveniently: use polymorphism and recursion to your advantage.
- Open/Closed Principle. You can introduce new element types into the app without breaking the existing code, which now works with the object tree.

## Cons
- It might be difficult to provide a common interface for classes whose functionality differs too much. In certain scenarios, you’d need to overgeneralize the component interface, making it harder to comprehend.

## Example
- File system manager
- Powerpoint
