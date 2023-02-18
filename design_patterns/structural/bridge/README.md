# Bridge Pattern
This pattern help us build flexible hierarchies then can grow independent of each other.
it lets you split a large class or a set of closely related classes into two separate hierarchies


## Pros
- You can create platform-independent classes and apps.
- The client code works with high-level abstractions. It isn’t exposed to the platform details.
- Open/Closed Principle. You can introduce new abstractions and implementations independently from each other.
- Single Responsibility Principle. You can focus on high-level logic in the abstraction and on platform details in the implementation.
 
 
## Cons
- You might make the code more complicated by applying the pattern to a highly cohesive class.
