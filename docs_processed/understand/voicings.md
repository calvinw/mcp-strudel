# Understanding Chords and Voicings

Let's dig deeper into how chords and voicings work in strudel.
I'll try to keep theory jargon to a minimum, so hopefully this is approachable for anyone interested.

## What is a chord

Playing more than one note at a time is generally called a `chord`. Here's an example:

```javascript
note("<[c3,eb3,g3] [f3,a3,c4]>").room(.5)
```

Here's the same with midi numbers:

```javascript
note("<[48,51,55] [53,57,60]>").room(.5)
```

Here, we have two 3-note chords played in a loop.
You could already stop here and write chords in this style, which is totally fine and gives you control over individual notes.
One downside is that it can be difficult to find good sounding chords and maybe you're yearning for a way to organize chords in some other way.

## Labeling Chords

Chords are typically given different labels depending on the relationship of the notes within.
In the number example above, we have `48,51,55` and `53,57,60`.

To analyze the relationship of those notes, they are typically compared to some `root`, which is often the lowest note.
In our case, the `roots` would be `48` (= `c3`) and `53` (= `f3`).
We can express the same chords relative to those `roots` like this:

```javascript
note("<[0,3,7] [0,4,7]>".add("<48 53>")).room(.5)
```

Now within each chord, each number represents the distance from the root.
A distance between pitches is typically called `interval`, but let's stick to distance for now.

Now we can see that our 2 chords are actually quite similar, as the only difference is the middle note (and the root of course).
They are part of a group of chords called `triads` which are chords with 3 notes.

### Triads

These 4 shapes are the most common types of `triads` you will encounter:

| shape | label      |
| ----- | ---------- |
| 0,4,7 | major      |
| 0,3,7 | minor      |
| 0,3,6 | diminished |
| 0,4,8 | augmented  |

Here they are in succession:

```javascript
note("<[0,4,7] [0,3,7] [0,3,6] [0,4,8]>".add("60"))
.room(.5)._pitchwheel()
```

Many types of music often only use minor and major chords, so we already have the knowledge to accompany songs. Here's one:

<MiniRepl
  client:visible
  tune={`
note(\`<
[0,3,7] [0,4,7] [0,4,7] [0,4,7]
[0,3,7] [0,4,7] [0,3,7] [0,4,7]
>\`.add(\`<
a c d f
a e a e
>\`)).room(.5)`}
/>

These are the chords for "The House of the Rising Sun" by The Animals.
So far, it doesn't sound too exciting, but at least it's recognizable.

## Voicings

A `voicing` is one of many ways a certain chord shape can be arranged.
The term comes from choral music, where chords can be sung in different ways by assigning different notes to each voice.
For example we could add 12 semitones to one or more notes in the chord:

```javascript
note("<[0,3,7] [12,3,7] [12,15,7] [12,15,19]>".add("48"))
.room(.5)
```

Notes that are 12 semitone steps apart (= 1 `octave`) are considered to be equal in a harmonic sense, which is why they get the same note letter.
Here's the same example with note letters:

```javascript
note("<[c3,eb3,g3] [c4,eb3,g3] [c4,eb4,g3] [c4,eb4,g4]>")
.room(.5)
```

These types of voicings are also called `inversions`. There are many other ways we could `voice` this minor chord:

```javascript
note("<[0,3,7,12] [0,15,24] [0,3,12]>".add("48"))
.room(.5)
```

Here we are changing the flavour of the chord slightly by

1. doubling notes 12 steps higher,
2. using very wide distances
3. omitting notes

## Voice Leading

When we want to meaningfully connect chords in a sequence, the chosen voicings affect the way each chord transitions to the next.
Let's revisit "The House of the Rising Sun", this time using our newly acquired voicing techniques:

<MiniRepl
  client:visible
  tune={`note(\`<
[0,3,7] [7,12,16] [0,7,16] [4,7,12]
[0,3,7] [4,7,12] [0,3,7] [4,7,12]
>\`.add(\`<
a c d f
a e a e
>\`)).room(.5)`}
  punchcard
/>

These voicings make the chords sound more connected and less jumpy, compared to the earlier version, which didn't focus on voicing.
The way chords interact is also called `voice leading`, reminiscent of how an
individual choir voice would move through a sequence of chords.

For example, try singing the top voice in the above example. Then try the same
on the example not focusing on voice leading. Which one's easier?

Naturally, there are many ways a progression of chords could be voiced and there is no definitive right or wrong.

## Chord Symbols

Musicians playing chord-based music often use a `lead sheet`, which is a simplified notation for a piece of music.
These sheets condense the essential elements, such as chords, into symbols that make the music easy to read and follow.
For example, a lead sheet for "The House of the Rising Sun" might include chords written like this:

```
Am | C | D  | F
Am | E | Am | E
```

Here, each symbol consists of the `root` of the chord and optionally an `m` to signal it's a minor chord (just the root note means it's major).
We could mirror that notation in strudel using the `pick` function:

```javascript
"<Am C D F Am E Am E>"
  .pick({
    Am: "57,60,64",
    C: "55,60,64",
    D: "50,57,66",
    F: "57,60,65",
    E: "56,59,64",
  })
  .note().room(.5)
```
*This example includes visual pattern representation*

## The voicing function

Coming up with good sounding voicings that connect well can be a difficult and time consuming process.
The `chord` and `voicing` functions can be used to automate that:

```javascript
chord("<Am C D F Am E Am E>").voicing().room(.5)
```
*This example includes visual pattern representation*

Here we're also using chord symbols but the voicings will be automatically generated with smooth `voice leading`, minimizing jumps.
It is inspired by the way a piano or guitar player would pick chords to accompany a song.

## Voicing Dictionaries

The voicing function internally uses so called `voicing dictionaries`, which can also be customized:

```javascript
addVoicings('house', {
  '': ['7 12 16', '0 7 16', '4 7 12'],
  'm': ['0 3 7']
})
chord("<Am C D F Am E Am E>")
  .dict('house').anchor(66)
  .voicing().room(.5)
```
*This example includes visual pattern representation*

In a `voicing dictionary`, each chord symbol is assigned one or more voicings.
The `voicing` function then picks the voicing that is closest to the `anchor` (defaults to `c5`).

The handy thing about this approach is that a `voicing dictionary` can be used to play any chord progression with automated voice leading!

## The default dictionary

When using the default dictionary, you can use these chord symbols:

```
2 5 6 7 9 11 13 69 add9
o h sus ^ - ^7 -7 7sus
h7 o7 ^9 ^13 ^7#11 ^9#11
^7#5 -6 -69 -^7 -^9 -9
-add9 -11 -7b5 h9 -b6 -#5
7b9 7#9 7#11 7b5 7#5 9#11
9b5 9#5 7b13 7#9#5 7#9b5
7#9#11 7b9#11 7b9b5 7b9#5
7b9#9 7b9b13 7alt 13#11
13b9 13#9 7b9sus 7susadd3
9sus 13sus 7b13sus
aug M m M7 m7 M9 M13
M7#11 M9#11 M7#5 m6 m69
m^7 -M7 m^9 -M9 m9 madd9
m11 m7b5 mb6 m#5 mM7 mM9
```

The available chords and the format is very much inspired by [ireal pro chords](https://technimo.helpshift.com/hc/en/3-ireal-pro/faq/88-chord-symbols-used-in-ireal-pro/).
Some symbols are synonymous:

- "-" is the same as "m", for example C-7 = Cm7
- "^" is the same as "M", for example C^7 = CM7
- "+" is the same as "aug"

You can decide which ones you prefer. There is no international standard for these symbols.
To get a full chord, the symbols have to be prefixed with a root pitch, e.g. D7#11 is the 7#11 chord relative to the pitch D.

Here are all possible chords with root C:

<MiniRepl
  client:visible
  tune={`chord(\`<
C2 C5 C6 C7 C9 C11 C13 C69
Cadd9 Co Ch Csus C^ C- C^7 
C-7 C7sus Ch7 Co7 C^9 C^13 
C^7#11 C^9#11 C^7#5 C-6 C-69 
C-^7 C-^9 C-9 C-add9 C-11 
C-7b5 Ch9 C-b6 C-#5 C7b9 
C7#9 C7#11 C7b5 C7#5 C9#11 
C9b5 C9#5 C7b13 C7#9#5 C7#9b5 
C7#9#11 C7b9#11 C7b9b5 C7b9#5 
C7b9#9 C7b9b13 C7alt C13#11 
C13b9 C13#9 C7b9sus C7susadd3 
C9sus C13sus C7b13sus C Caug 
CM Cm CM7 Cm7 CM9 CM13 CM7#11 
CM9#11 CM7#5 Cm6 Cm69 Cm^7 
C-M7 Cm^9 C-M9 Cm9 Cmadd9 
Cm11 Cm7b5 Cmb6 Cm#5
>\`).voicing().room(.5)`}
  punchcard
/>

Note that the default dictionary contains multiple ways (= `voicings`) to play each chord symbol.
By default, the `voicing` function tries to minimize jumps.
You can alter the picked voicings in various ways, which are now explained in further detail:

## anchor

The `anchor` is a note that is used to align the voicings to:

```javascript
anchor("<c4 g4 c5 g5>").chord("C").voicing().room(.5)
```
*This example includes visual pattern representation*

By default, the anchor is the highest possible note the voicing can contain.
When deciding which voicing of the dictionary to pick for a certain chord, the voicing with a top note closest to the anchor wins.

Note that the anchors in the above example match up with the top notes in the pianoroll.
Like `note`, anchor accepts either midi numbers or note names.

## mode

With `mode`, you can change the way the voicing relates to the `anchor`:

```javascript
mode("<below above duck root>").chord("C").anchor("c5").voicing().room(.5)
```
*This example includes visual pattern representation*

The modes are:

- `below`: the top note of the voicing is lower than or equal to the anchor (default)
- `above`: the bottom note of the voicing is higher than or equal to the anchor
- `duck`: the top note of the voicing is lower than the anchor
- `root`: the bottom note of the voicing is always the root note closest to the anchor

The `anchor` can also be set from within the `mode` function:

```javascript
mode("<below above duck root>:c5").chord("C").voicing().room(.5)
```
*This example includes visual pattern representation*

## n

The `n` control can be used with `voicing` to select individual notes:

```javascript
n("0 3 1 2").chord("<C <Fm Db>>").voicing()
.clip("4 3 2 1").room(.5)
```
*This example includes visual pattern representation*

## Example

Here's an example of a Jazz Blues in F:

<MiniRepl
  client:visible
  tune={`let chords = chord(\`<
F7 Bb7 F7 [Cm7 F7]
Bb7 Bo F7 [Am7 D7]
Gm7 C7 [F7 D7] [Gm7 C7]
>\`)
$: n("7 8 [10 9] 8").set(chords).voicing().dec(.2)
$: chords.struct("- x - x").voicing().room(.5)
$: n("0 - 1 -").set(chords).mode("root:g2").voicing()
`}
  punchcard
/>

The chords are reused for melody, chords and bassline of the tune.