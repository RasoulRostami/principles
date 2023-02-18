# Strategy Design Pattern
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
In other hand it let us create, manage and use diffrent strategy in our application.


Imagine that you have to get to the airport. You can catch a bus, order a cab, or get on your bicycle. These are your transportation strategies. You can pick one of the strategies depending on factors such as budget or time constraints.

## strategy vs state design pattern
If you see strategy and state design pattern UML, they are same
so what is different?

In State we have one current state, and all behavior are presents by sub classes of Tools
But in Strategy we haven't an state and we have different behavior that present we different strategy objects


## Help
1. Create, manage and use diffrent of strategies

## Pros
- You can isolate the implementation details of an algorithm from the code that uses it.
- Open/Closed Principle. You can introduce new strategies without having to change the context.

## Cons
- If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern.
- Clients must be aware of the differences between strategies to be able to select a proper one.j
