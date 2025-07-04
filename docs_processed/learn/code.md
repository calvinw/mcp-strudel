# Coding Syntax

Let's take a step back and understand how the syntax in Strudel works.

Take a look at this simple example:



- We have a word `note` which is followed by some brackets `()` with some words/letters/numbers inside, surrounded by quotes `"c a f e"`
- Then we have a dot `.` followed by another similar piece of code `s("piano")`.
- We can also see these texts are _highlighted_ using colours: word `note` is purple, the brackets `()` are grey, and the content inside the `""` are green. (The colors could be different if you've changed the default theme)

What happens if we try to 'break' this pattern in different ways?







Ok, none of these seem to work...



This one does work, but now we only hear the first note...

So what is going on here?

# Functions, arguments and chaining

So far, we've seen the following syntax:

```
xxx("foo").yyy("bar")
```

Generally, `xxx` and `yyy` are called [_functions_](<https://en.wikipedia.org/wiki/Function_(computer_programming)>), while `foo` and `bar` are called function [_arguments_ or _parameters_](<https://en.wikipedia.org/wiki/Parameter_(computer_programming)>).
So far, we've used the functions to declare which aspect of the sound we want to control, and their arguments for the actual data.
The `yyy` function is called a [_chained_ function](https://en.wikipedia.org/wiki/Method_chaining), because it is appended with a dot (`.`).

Generally, the idea with chaining is that code such as `a("this").b("that").c("other")` allows `a`, `b` and `c` functions to happen in a specified order, without needing to write them as three separate lines of code.
You can think of this as being similar to chaining audio effects together using guitar pedals or digital audio effects.

Strudel makes heavy use of chained functions. Here is a more sophisticated example:



# Comments

The `//` in the example above is a line comment, resulting in the `delay` function being ignored.
It is a handy way to quickly turn code on and off.
Try uncommenting this line by deleting `//` and refreshing the pattern.
You can also use the keyboard shortcut `cmd-/` to toggle comments on and off.

You might noticed that some comments in the REPL samples include some words starting with a "@", like `@by` or `@license`.
Those are just a convention to define some information about the music. We will talk about it in the [Music metadata](/learn/metadata) section.

# Strings

Ok, so what about the content inside the quotes (e.g. `"c a f e"`)?
In JavaScript, as in most programming languages, this content is referred to as being a [_string_](<https://en.wikipedia.org/wiki/String_(computer_science)>).
A string is simply a sequence of individual characters.
In TidalCycles, double quoted strings are used to write _patterns_ using the mini-notation, and you may hear the phrase _pattern string_ from time to time.
If you want to create a regular string and not a pattern, you can use single quotes, e.g. `'C minor'` will not be parsed as Mini Notation.

The good news is, that this covers most of the JavaScript syntax needed for Strudel!

<br />