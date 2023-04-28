# Builder Factory
Builder factory lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code. 
With Builder factory we can separate construction of an object from its representations. like export as PDF, Image, etc in draw.io

## Pros
- You can construct objects step-by-step, defer construction steps or run steps recursively.
- You can reuse the same construction code when building various representations of products.
- Single Responsibility Principle. You can isolate complex construction code from the business logic of the product

## Cons
-  The overall complexity of the code increases since the pattern requires creating multiple new classes.

## Example

