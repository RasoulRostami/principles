# Chain of responsibility
It is useful design pattern when we have got pipelines or chain of objects call after each other.

Chain of responsibility lets you pass requests along a chain of handlers. Upon receiving a request,
each handler decides either to process the request or to pass it to the next handler in the chain.


## Help 
1. If a pipeline is failed, process doesn't go to the next pipeline
2. Have extensible application

## Pros
- You can control the order of request handling.
- Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform operations.
- Open/Closed Principle. You can introduce new handlers into the app without breaking the existing client code.

## Cons
- Some requests may end up unhandled.

## Example
- Django Rest Framework permission classes
- Django middlewares
