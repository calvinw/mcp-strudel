# Tonal Functions

These functions use [tonaljs](https://github.com/tonaljs/tonal) to provide helpers for musical operations.

### voicing()

##voicing##

*Function documentation for `voicing`*

Here's an example of how you can play chords and a bassline:

```javascript
chord("<C^7 A7b13 Dm7 G7>*2")
  .dict('ireal').layer(
  x=>x.struct("[~ x]*2").voicing()
  ,
  x=>n("0*4").set(x).mode("root:g2").voicing()
  .s('sawtooth').cutoff("800:4:2")
)
```

### scale(name)

##scale##

*Function documentation for `scale`*

### transpose(semitones)

Transposes all notes to the given number of semitones:

```javascript
"[c2 c3]*4".transpose("<0 -2 5 3>").note()
```

This method gets really exciting when we use it with a pattern as above.

Instead of numbers, scientific interval notation can be used as well:

```javascript
"[c2 c3]*4".transpose("<1P -2M 4P 3m>").note()
```

### scaleTranspose(steps)

Transposes notes inside the scale by the number of steps:

```javascript
"[-8 [2,4,6]]*2"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>*2")
.note()
```

### rootNotes(octave = 2)

Turns chord symbols into root notes of chords in given octave.

```javascript
"<C^7 A7b13 Dm7 G7>*2".rootNotes(3).note()
```

Together with layer, struct and voicings, this can be used to create a basic backing track:

```javascript
"<C^7 A7b13 Dm7 G7>*2".layer(
  x => x.voicings('lefthand').struct("[~ x]*2").note(),
  x => x.rootNotes(2).note().s('sawtooth').cutoff(800)
)
```