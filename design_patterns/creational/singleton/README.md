# Singleton Pattern
Sigleton pattern lets you ensure that a class has only one instance, while providing a global access point to this instance.
Sometime we need only one instace on a class, For example settings class must be single one. Or Publishers in application use
same settings and all them are same, So we can create a single instace and save memory.

## Pros
- You can be sure that a class has only a single instance.
- You gain a global access point to that instance.
- The singleton object is initialized only when it’s requested for the first time.

## Cons
- Violates the Single Responsibility Principle. The pattern solves two problems at the time.
- The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.
- The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times.

## Example
