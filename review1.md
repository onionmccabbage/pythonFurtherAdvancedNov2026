## Further Advanced Python Review Exercise 1 (40 mins)

Individually or in groups, tackle as many of these challenges as you like, in any order

There will be a chance to show your thinking after the exercise

### Decorator Pattern
- Write a decorator function that ensures all positional arguments (*args) are non-empty string
  Any positional arguments that fail validation should raise a typeError
- exercise the code to show it works as expected
- optionally: expand this decorator (or write separate decorators) for other kinds of validation (eg int, float, numeric, instance-of)
- optionally: also validate keyword-args (**kwargs)

### Facade and Factory patterns
- Re-write the creature factory example as a facade to all the creatures 
  (so they are all instantiated and all make a noise)
- consider if the 'Manager' facade could be sensibly implemented as a factory
  (probably a bad idea)

### Using System arguments
- if you know how to use system arguments, implement sys.argv such that the factory 
  conditionally acts upon a creature provided at run-time (i.e. sys.argv includes a creature)
- Also implement conditions on the facade, so sys.argv can determine 
  which assets (and maybe how many of each) the manager should deploy

### Constructor Pattern
- Write an abstract base class that insists __str__ is implemented
- Extend all the classes in the 'facade' pattern to implement this base class
- Write __str__ methods to satisfy this restriction
- optionally, do this also for __repr__
