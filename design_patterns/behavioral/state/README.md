# State Design Pattern
State design patterns is used when we have multi state in our object which have different behavior.
State lets an object alter its behavior when its internal state changes.

In the Photoshop application, we have got diffrent tools with diffrent behavior, user use one tool 
at the moment. what does this tool do? we want to solve this problem.

## Help
1. Handle diffrent state 

## Pros
- Single Responsibility Principle. Organize the code related to particular states into separate classes.
- Open/Closed Principle. Introduce new states without changing existing state classes or the context

## Cons
- Applying the pattern can be overkill if a state machine has only a few states or rarely changes.
