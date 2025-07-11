# Patterns

Patterns are the essence of Tidal. Its patterns are abstract entities that represent flows of time as functions, adapting a technique called pure functional reactive programming. Taking a time span as its input, a Pattern can output a set of events that happen within that time span. It depends on the structure of the Pattern how the events are located in time.
From now on, this process of generating events from a time span will be called **querying**.
Example:

```javascript
const pattern = sequence("c3", ["e3", "g3"])
const events = pattern.queryArc(0, 1)
console.log(events.map((e) => e.show()))
silence
```

In this example, we create a pattern using the `sequence` function and **query** it for the time span from `0` to `1`.
Those numbers represent units of time called **cycles**. The length of one cycle depends on the tempo, which defaults to one cycle per second.
The resulting events are:

```js
[
  '[ 0/1 -> 1/2 | c3 ]', //
  '[ 1/2 -> 3/4 | e3 ]',
  '[ 3/4 -> 1/1 | g3 ]',
];
```

Each event has a value, a begin time and an end time, where time is represented as a fraction. In the above case, the events are placed in sequential order, where c3 takes the first half, and e3 and g3 together take the second half. This temporal placement is the result of the `sequence` function, which divides its arguments equally over one cycle. If an argument is an array, the same rule applies to that part of the cycle. In the example, e3 and g3 are divided equally over the second half of the whole cycle.

Note that the query function is not just a way to access a pattern, but true to the principles of functional programming, is the pattern itself. This means that in theory there is no way to change a pattern, it is opaque as a pure function. In practice though, Strudel and Tidal are all about transforming patterns, so how is this done? The answer is, by replacing the pattern with a new one, that calls the old one. This new one is only able to manipulate the query before passing it to the old pattern, and manipulate the results from it before returning them to caller. But, this is enough to support all the temporal and structural manipulations provided by Strudel (and Tidal's) extensive library of functions.

The above examples do not represent how Strudel is used in practice. In the live coding editor, the user only has to type in the pattern itself, the querying will be handled by the scheduler. The scheduler will repeatedly query the pattern for events, which are then scheduled as sound synthesis or other event triggers.

Can we [align](/technical-manual/alignment) patterns?