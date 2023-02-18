# Proxy Pattern
Allow us to create a proxy or agent for a real object. when we want to talk with target, we talk to agent and forward it to the target object.

It lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

## Pros
- You can control the service object without clients knowing about it.
- You can manage the lifecycle of the service object when clients don’t care about it.
- The proxy works even if the service object isn’t ready or is not available.
- Open/Closed Principle. You can introduce new proxies without changing the service or clients.


## Cons
- The code may become more complicated since you need to introduce a lot of new classes.
- The response from the service might get delayed.

## Example
- Django ORM lazy-loading
