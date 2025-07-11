# Pattern Aligment & Combination

One core aspect of Strudel, inherited from Tidal, is the flexible way that patterns can be combined, irrespective of their structure. Its declarative approach means a live coder does not have to think about the details of _how_ this is done, only _what_ is to be done.

As a simple example, consider two number patterns `"0 [1 2] 3"`, and `"10 20"`. The first has three contiguous steps of equal lengths, with the second step broken down into two substeps, giving four events in total. There are a very large number of ways in which the structure of these two patterns could be combined, but the default method in both Strudel and Tidal is to line up the cycles of the two patterns, and then take events from the first pattern and match them with those in the second pattern. Therefore, the following two lines are equivalent:

```js
'0 [1 2] 3'.add('10 20');
('10 [11 22] 23');
```

Where the events only partially overlap, they are treated as fragments
of the event in the first pattern. This is a little difficult to
conceptualise, but lets start by comparing the two patterns in the
following example:

```js
'0 1 2'.add('10 20');
('10 [11 21] 22');
```

They are similar to the previous example in that the number `1` is split in two, with its two halves added to `10` and `20` respectively. However, the `11` 'remembers' that it is a fragment of that original `1` event, and so is treated as having a duration of a third of a cycle, despite only being active for a sixth of a cycle. Likewise, the `21` is also a fragment of that original `1` event, but a fragment of its second half. Because the start of its event is missing, it wouldn't actually trigger a sound (unless it underwent further pattern transformations/combinations).

In practice, the effect of this default, implicit method for combining two patterns is that the second pattern is added _in_ to the first one, and indeed this can be made explicit:

```js
'0 1 2'.add.in('10 20');
```

This makes way for other ways to align the pattern, and several are already defined, in particular:

- `in` - as explained above, aligns cycles, and applies values from the pattern on the right _in_ to the pattern on the left.
- `out` - as with `in`, but values are applied _out_ of the pattern on the left (i.e. _in_ to the one on the right).
- `mix` - structures from both patterns are combined, so that the new events are not fragments but are created at intersections of events from both sides.
- `squeeze` - cycles from the pattern on the right are squeezed into events on the left. So that e.g. `"0 1 2".add.squeeze("10 20")` is equivalent to `"[10 20] [11 21] [12 22]"`.
- `squeezeout` - as with `squeeze`, but cycles from the left are squeezed into events on the right. So, `"0 1 2".add.squeezeout("10 20")` is equivalent to `[10 11 12] [20 21 22]`.
- `reset` is similar to `squeezeout` in that cycles from the right are aligned with events on the left. However those cycles are not 'squeezed', rather they are truncated to fit the event. So `"0 1 2 3 4 5 6 7".add.reset("10 [20 30]")` would be equivalent to `10 11 12 13 20 21 30 31`. In effect, events on the right 'reset' cycles on the left.
- `restart` is similar to `reset`, but the pattern is 'restarted' from its very first cycle, rather than from the current cycle. `reset` and `restart` therefore only give different results where the leftmost pattern differs from one cycle to the next.

We will save going deeper into the background, design and practicalities of these alignment functions for future publications. However in the next section, we take them as a case study for looking at the different design affordances offered by Haskell to Tidal, and JavaScript to Strudel.

Ok, so how do Strudel and Tidal [compare](/learn/strudel-vs-tidal)?