# Command Design Pattern
Command design pattern is very useful design pattern and we can see it in lots of framework and libraries. It help up when

1. We want to design and implement a framework or a library. There are a few objects which contain common attributes and behaviors. But some behaviors are depends on situation and developer must to define it. we need dynamic behavior for a method
2. Undo mechanism. We have learned about Memento design pattern for undoing mechanism, but sometime memento is not good design, because memento take lot's of snapshot and need too much memory in heavy application like video-editors.

Story: after a long walk through the city, you get to a nice restaurant and sit at the table by the window. A friendly waiter approaches you and quickly takes your order, writing it down on a piece of paper. The waiter goes to the kitchen and sticks the order on the wall. After a while, the order gets to the chef, who reads it and cooks the meal accordingly. The cook places the meal on a tray along with the order. The waiter discovers the tray, checks the order to make sure everything is as you wanted it, and brings everything to your table.

The paper order serves as a command. It remains in a queue until the chef is ready to serve it. The order contains all the relevant information required to cook the meal. It allows the chef to start cooking right away instead of running around clarifying the order details from you directly.

## Help
1. implement dynamic method and behavior in framework or libraries
2. Undo mechanism for heavy application

## Pros
- Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform these operations.
- Open/Closed Principle. You can introduce new commands into the app without breaking existing client code.
- You can implement undo/redo.
- You can implement deferred execution of operations.
- You can assemble a set of simple commands into a complex one.

## Example
- Vuejs HTML tags
