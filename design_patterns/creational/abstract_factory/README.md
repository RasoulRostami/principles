# Abstract Factory
Abstract factory lets you produce families of related objects.

## Pros
- You can be sure that the products you’re getting from a factory are compatible with each other.
- You avoid tight coupling between concrete products and client code.
- Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.
- Open/Closed Principle. You can introduce new variants of products without breaking existing client code.

## Cons
- The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.

## Example

