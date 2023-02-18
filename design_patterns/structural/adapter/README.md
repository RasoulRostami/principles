# Adapter Pattern
We use this pattern to convert interface of our classes to different form. Like normal adapter we daily use (TypeC to TypeB). We use this solution where we have an existing class and use it some where but interface of this class doesn't form that we expect.

Adapter allows objects with incompatible interfaces to collaborate.

## Pros
- Single Responsibility Principle. You can separate the interface or data conversion code from the primary business logic of the program.
- Open/Closed Principle. You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the adapters through the client interface.

## Cons
-  The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it’s simpler just to change the service class so that it matches the rest of your code.

## Example
