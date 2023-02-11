# Observer Design Pattern
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

Observer is very useful when state of objects are changes and we need to notify other objects about it.

Example: If you subscribe to a newspaper or magazine, you no longer need to go to the store to check if the next issue is available. Instead, the publisher sends new issues directly to your mailbox right after publication or even in advance. 

There are two method to send object's data to the publishers. Push method and Pull method.
we will see in the examples.

## Help
1. Separate business logic from unrelated object.
2. Extensible applications

## Pros
- Open/Closed Principle. You can introduce new subscriber classes without having to change the publisher’s code (and vice versa if there’s a publisher interface).
- You can establish relations between objects at runtime.

## Cons
- Subscribers are notified in random order.

## Example
- Django model signals
