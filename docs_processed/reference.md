API Reference
This is the long list of functions you can use. Remember that you don't need to remember all of those and that you can already make music with a small set of functions!

absoluteOrientationAlpha
Synonyms: absOriA, absOriZ, absoluteOrientationZ

The device's absolute orientation alpha value ranges from 0 to 1.


n(absoluteOrientationAlpha.segment(4).range(0,7)).scale("C:minor")
absoluteOrientationBeta
Synonyms: absOriB, absOriX, absoluteOrientationX

The device's absolute orientation beta value ranges from 0 to 1.


n(absoluteOrientationBeta.segment(4).range(0,7)).scale("C:minor")
absoluteOrientationGamma
Synonyms: absOriG, absOriY, absoluteOrientationY

The device's absolute orientation gamma value ranges from 0 to 1.


n(absoluteOrientationGamma.segment(4).range(0,7)).scale("C:minor")
accelerate
A pattern of numbers that speed up (or slow down) samples while they play. Currently only supported by osc / superdirt.


amount : number | Pattern - acceleration.
s("sax").accelerate("<0 1 2 4 8 16>").slow(2).osc()
accelerationX
Synonyms: accX

The accelerometer's x-axis value ranges from 0 to 1.


n(accelerationX.segment(4).range(0,7)).scale("C:minor")
accelerationY
Synonyms: accY

The accelerometer's y-axis value ranges from 0 to 1.


n(accelerationY.segment(4).range(0,7)).scale("C:minor")
accelerationZ
Synonyms: accZ

The accelerometer's z-axis value ranges from 0 to 1.


n(accelerationZ.segment(4).range(0,7)).scale("C:minor")
add
Assumes a pattern of numbers. Adds the given number to each item in the pattern.


// Here, the triad 0, 2, 4 is shifted by different amounts
n("0 2 4".add("<0 3 4 0>")).scale("C:major")
// Without add, the equivalent would be:
// n("<[0 2 4] [3 5 7] [4 6 8] [0 2 4]>").scale("C:major")
// You can also use add with notes:
note("c3 e3 g3".add("<0 5 7 0>"))
// Behind the scenes, the notes are converted to midi numbers:
// note("48 52 55".add("<0 5 7 0>"))
addVoicings
Adds a new custom voicing dictionary.


name : string - identifier for the voicing dictionary
dictionary : Object - maps chord symbol to possible voicings
range : Array - min, max note
addVoicings('cookie', {
  7: ['3M 7m 9M 12P 15P', '7m 10M 13M 16M 19P'],
  '^7': ['3M 6M 9M 12P 14M', '7M 10M 13M 16M 19P'],
  m7: ['8P 11P 14m 17m 19P', '5P 8P 11P 14m 17m'],
  m7b5: ['3m 5d 8P 11P 14m', '5d 8P 11P 14m 17m'],
  o7: ['3m 6M 9M 11A 15P'],
  '7alt': ['3M 7m 10m 13m 15P'],
  '7#11': ['7m 10m 13m 15P 17m'],
}, ['C3', 'C6'])
"<C^7 A7 Dm7 G7>".voicings('cookie').note()
adsr
ADSR envelope: Combination of Attack, Decay, Sustain, and Release.


time : number | Pattern - attack time in seconds
time : number | Pattern - decay time in seconds
gain : number | Pattern - sustain level (0 to 1)
time : number | Pattern - release time in seconds
note("[c3 bb2 f3 eb3]*2").sound("sawtooth").lpf(600).adsr(".1:.1:.5:.2")
aliasBank
Register an alias for a bank of sounds. Optionally accepts a single argument map of bank aliases. Optionally accepts a single argument string of a path to a JSON file containing bank aliases.


bank : string - The bank to alias
alias : string - The alias to use for the bank
all
Applies a function to all the running patterns. Note that the patterns are groups together into a single stack before the function is applied. This is probably what you want, but see each for a version that applies the function to each pattern separately.

$: sound("bd - cp sd")
$: sound("hh*8")
all(fast("<2 3>"))
$: sound("bd - cp sd")
$: sound("hh*8")
all(x => x.pianoroll())

almostAlways
Shorthand for .sometimesBy(0.9, fn)


s("hh*8").almostAlways(x=>x.speed("0.5"))
almostNever
Shorthand for .sometimesBy(0.1, fn)


s("hh*8").almostNever(x=>x.speed("0.5"))
always
Shorthand for .sometimesBy(1, fn) (always calls fn)


s("hh*8").always(x=>x.speed("0.5"))
amp
Like gain, but linear.


amount : number | Pattern - gain.
s("bd*8").amp(".1*2 .5 .1*2 .5 .1 .5").osc()
appBoth
When this method is called on a pattern of functions, it matches its haps with those in the given pattern of values. A new pattern is returned, with each matching value applied to the corresponding function.

In this _appBoth variant, where timespans of the function and value haps are not the same but do intersect, the resulting hap has a timespan of the intersection. This applies to both the part and the whole timespan.


pat_val : Pattern
appLeft
As with appBoth, but the whole timespan is not the intersection, but the timespan from the function of patterns that this method is called on. In practice, this means that the pattern structure, including onsets, are preserved from the pattern of functions (often referred to as the left hand or inner pattern).


pat_val : Pattern
apply
Like layer, but with a single function:


"<c3 eb3 g3>".scale('C minor').apply(scaleTranspose("0,2,4")).note()
applyGradualLowpass
Applies a constantly changing lowpass filter to the given sound.


input : AudioBuffer
lpFreqStart : number
lpFreqEnd : number
lpFreqEndAt : number
callback : function - May be called immediately within the current execution context, or later.
applyHannWindow
Apply Hann window in-place


appRight
As with appLeft, but whole timespans are instead taken from the pattern of values, i.e. structure is preserved from the right hand/outer pattern.


pat_val : Pattern
appWhole
Assumes 'this' is a pattern of functions, and given a function to resolve wholes, applies a given pattern of values to that pattern of functions.


whole_func : function
func : function
arp
Selects indices in in stacked notes.


note("<[c,eb,g]!2 [c,f,ab] [d,f,ab]>")
.arp("0 [0,2] 1 [0,2]")
arpWith
Selects indices in in stacked notes.


note("<[c,eb,g]!2 [c,f,ab] [d,f,ab]>")
.arpWith(haps => haps[2])
arrange
Allows to arrange multiple patterns together over multiple cycles. Takes a variable number of arrays with two elements specifying the number of cycles and the pattern to use.


arrange(
  [4, "<c a f e>(3,8)"],
  [2, "<g a>(5,8)"]
).note()
as
Sets properties in a batch.


mapping : String | Array - the control names that are set
"c:.5 a:1 f:.25 e:.8".as("note:clip")
"{0@2 0.25 0 0.5 .3 .5}%8".as("begin").s("sax_vib").clip(1)
attack
Synonyms: att

Amplitude envelope attack time: Specifies how long it takes for the sound to reach its peak value, relative to the onset.


attack : number | Pattern - time in seconds.
note("c3 e3 f3 g3").attack("<0 .1 .5>")
bank
Select the sound bank to use. To be used together with s. The bank name (+ "_") will be prepended to the value of s.


bank : string | Pattern - the name of the bank
s("bd sd [~ bd] sd").bank('RolandTR909') // = s("RolandTR909_bd RolandTR909_sd")
beat
creates a structure pattern from divisions of a cycle especially useful for creating rhythms


s("bd").beat("0,7,10", 16)
s("sd").beat("4,12", 16)
begin
a pattern of numbers from 0 to 1. Skips the beginning of each sample, e.g. 0.25 to cut off the first quarter from each sample.


amount : number | Pattern - between 0 and 1, where 1 is the length of the sample
samples({ rave: 'rave/AREUREADY.wav' }, 'github:tidalcycles/dirt-samples')
s("rave").begin("<0 .25 .5 .75>").fast(2)
berlin
Generates a continuous pattern of [berlin noise](conceived by Jame Coyne and Jade Rowland as a joke but turned out to be surprisingly cool and useful, like perlin noise but with sawtooth waves), in the range 0..1.


// ascending arpeggios
n("0!16".add(berlin.fast(4).mul(14))).scale("d:minor")
binary
Creates a pattern from a binary number.


n : number - input number to convert to binary
"hh".s().struct(binary(5))
// "hh".s().struct("1 0 1")
binaryN
Creates a pattern from a binary number, padded to n bits long.


n : number - input number to convert to binary
nBits : number - pattern length, defaults to 16
"hh".s().struct(binaryN(55532, 16))
// "hh".s().struct("1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 0")
bite
Splits a pattern into the given number of slices, and plays them according to a pattern of slice numbers. Similar to slice, but slices up patterns rather than sound samples.


number : number - of slices
slices : number - to play
note("0 1 2 3 4 5 6 7".scale('c:mixolydian'))
.bite(4, "3 2 1 0")
sound("bd - bd bd*2, - sd:6 - sd:5 sd:1 - [- sd:2] -, hh [- cp:7]")
  .bank("RolandTR909").speed(1.2)
  .bite(4, "0 0 [1 2] <3 2> 0 0 [2 1] 3")
bpattack
Synonyms: bpa

Sets the attack duration for the bandpass filter envelope.


attack : number | Pattern - time of the bandpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.bpf(500)
.bpa("<.5 .25 .1 .01>/4")
.bpenv(4)
bpdecay
Synonyms: bpd

Sets the decay duration for the bandpass filter envelope.


decay : number | Pattern - time of the bandpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.bpf(500)
.bpd("<.5 .25 .1 0>/4")
.bps(0.2)
.bpenv(4)
bpenv
Synonyms: bpe

Sets the bandpass filter envelope modulation depth.


modulation : number | Pattern - depth of the bandpass filter envelope between 0 and n
note("c2 e2 f2 g2")
.sound('sawtooth')
.bpf(500)
.bpa(.5)
.bpenv("<4 2 1 0 -1 -2 -4>/4")
bpf
Synonyms: bandf, bp

Sets the center frequency of the band-pass filter. When using mininotation, you can also optionally supply the 'bpq' parameter separated by ':'.


frequency : number | Pattern - center frequency
s("bd sd [~ bd] sd,hh*6").bpf("<1000 2000 4000 8000>")
bpq
Synonyms: bandq

Sets the band-pass q-factor (resonance).


q : number | Pattern - q factor
s("bd sd [~ bd] sd").bpf(500).bpq("<0 1 2 3>")
bprelease
Synonyms: bpr

Sets the release time for the bandpass filter envelope.


release : number | Pattern - time of the bandpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.clip(.5)
.bpf(500)
.bpenv(4)
.bpr("<.5 .25 .1 0>/4")
.release(.5)
bpsustain
Synonyms: bps

Sets the sustain amplitude for the bandpass filter envelope.


sustain : number | Pattern - amplitude of the bandpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.bpf(500)
.bpd(.5)
.bps("<0 .25 .5 1>/4")
.bpenv(4)
brak
Returns a new pattern where every other cycle is played once, twice as fast, and offset in time by one quarter of a cycle. Creates a kind of breakbeat feel.


brand
A continuous pattern of 0 or 1 (binary random)


s("hh*10").pan(brand)
brandBy
A continuous pattern of 0 or 1 (binary random), with a probability for the value being 1


probability : number - a number between 0 and 1
s("hh*10").pan(brandBy(0.2))
byteBeatExpression
Synonyms: bbexpr

Create byte beats with custom expressions


byteBeatExpression : number | Pattern - bitwise expression for creating bytebeat
s("bytebeat").bbexpr('t*(t>>15^t>>66)')
byteBeatStartTime
Synonyms: bbst

Create byte beats with custom expressions


byteBeatStartTime : number | Pattern - in samples (t)
note("c3!8".add("{0 0 12 0 7 5 3}%8")).s("bytebeat:5").bbst("<3 1>".mul(10000))._scope()
cat
Synonyms: slowcat

The given items are concatenated, where each one takes one cycle.


items : any - The items to concatenate
cat("e5", "b4", ["d5", "c5"]).note()
// "<e5 b4 [d5 c5]>".note()
// As a chained function:
s("hh*4").cat(
   note("c4(5,8)")
)
ccn
MIDI control number: Sends a MIDI control change message.


MIDI : number | Pattern - control number (0-127)
ccv
MIDI control value: Sends a MIDI control change message.


MIDI : number | Pattern - control value (0-127)
ceil
Assumes a numerical pattern. Returns a new pattern with all values set to their mathematical ceiling. E.g. 3.2 replaced with 4, and -4.2 replaced with -4.


note("42 42.1 42.5 43".ceil())
channel
choose the channel the pattern is sent to in superdirt


channel : number | Pattern - channel number
channels
Synonyms: ch

Allows you to set the output channels on the interface


channels : number | Pattern - pattern the output channels
note("e a d b g").channels("3:4")
choose
Chooses randomly from the given list of elements.


xs : any - values / patterns to choose from.
note("c2 g2!2 d2 f1").s(choose("sine", "triangle", "bd:6"))
choose
Chooses from the given list of values (or patterns of values), according to the pattern that the method is called on. The pattern should be in the range 0 .. 1.


xs : any
choose2
As with choose, but the pattern that this method is called on should be in the range -1 .. 1


xs : any
chooseCycles
Synonyms: randcat

Picks one of the elements at random each cycle.


chooseCycles("bd", "hh", "sd").s().fast(8)
s("bd | hh | sd").fast(8)
chooseInWith
As with {chooseWith}, but the structure comes from the chosen values, rather than the pattern you're using to choose with.


pat : Pattern
xs : *
chooseWith
Choose from the list of values (or patterns of values) using the given pattern of numbers, which should be in the range of 0..1


pat : Pattern
xs : *
note("c2 g2!2 d2 f1").s(chooseWith(sine.fast(2), ["sawtooth", "triangle", "bd:6"]))
chop
Cuts each sample into the given number of parts, allowing you to explore a technique known as 'granular synthesis'. It turns a pattern of samples into a pattern of parts of samples.


samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes")
 .chop(4)
 .rev() // reverse order of chops
 .loopAt(2) // fit sample into 2 cycles
chunk
Synonyms: slowChunk, slowchunk

Divides a pattern into a given number of parts, then cycles through those parts in turn, applying the given function to each part in turn (one part per cycle).


"0 1 2 3".chunk(4, x=>x.add(7))
.scale("A:minor").note()
chunkBack
Synonyms: chunkback

Like chunk, but cycles through the parts in reverse order. Known as chunk' in tidalcycles


"0 1 2 3".chunkBack(4, x=>x.add(7))
.scale("A:minor").note()
chyx
BYTE BEATS


clip
Synonyms: legato

Multiplies the duration with the given number. Also cuts samples off at the end if they exceed the duration.


factor : number | Pattern - = 0
note("c a f e").s("piano").clip("<.5 1 2>")
coarse
fake-resampling for lowering the sample rate. Caution: This effect seems to only work in chromium based browsers


factor : number | Pattern - 1 for original 2 for half, 3 for a third and so on.
s("bd sd [~ bd] sd,hh*8").coarse("<1 4 8 16 32>")
color
Synonyms: colour

Sets the color of the hap in visualizations like pianoroll or highlighting.


color : string - Hexadecimal or CSS color name
compress
Compress each cycle into the given timespan, leaving a gap


cat(
  s("bd sd").compress(.25,.75),
  s("~ bd sd ~")
)
compressor
Dynamics Compressor. The params are compressor("threshold:ratio:knee:attack:release") More info here


s("bd sd [~ bd] sd,hh*8")
.compressor("-20:20:10:.002:.02")
computeMagnitudes
Compute squared magnitudes for peak finding


contract
Experimental

Contracts the step size of the pattern by the given factor. See also expand.


sound("tha dhi thom nam").bank("mridangam").contract("3 2 1 1 2 3").pace(8)
control
MIDI control: Sends a MIDI control change message.


MIDI : number | Pattern - control number (0-127)
MIDI : number | Pattern - controller value (0-127)
cosine
A cosine signal between 0 and 1.


n(stack(sine,cosine).segment(16).range(0,15))
.scale("C:minor")
cosine2
A cosine signal between -1 and 1 (like cosine, but bipolar).


cpm
Plays the pattern at the given cycles per minute.


s("<bd sd>,hh*2").cpm(90) // = 90 bpm
crush
bit crusher effect.


depth : number | Pattern - between 1 (for drastic reduction in bit-depth) to 16 (for barely no reduction).
s("<bd sd>,hh*3").fast(2).crush("<16 8 7 6 5 4 3 2>")
csoundm
Sends notes to Csound for rendering with MIDI semantics. The hap value is translated to these Csound pfields:

p1 -- Csound instrument either as a number (1-based, can be a fraction), or as a string name. p2 -- time in beats (usually seconds) from start of performance. p3 -- duration in beats (usually seconds). p4 -- MIDI key number (as a real number, not an integer but in [0, 127]. p5 -- MIDI velocity (as a real number, not an integer but in [0, 127]. p6 -- Strudel controls, as a string.


cut
In the style of classic drum-machines, cut will stop a playing sample as soon as another samples with in same cutgroup is to be played. An example would be an open hi-hat followed by a closed one, essentially muting the open.


group : number | Pattern - cut group number
s("[oh hh]*4").cut(1)
decay
Amplitude envelope decay time: the time it takes after the attack time to reach the sustain level. Note that the decay is only audible if the sustain value is lower than 1.


time : number | Pattern - decay time in seconds
note("c3 e3 f3 g3").decay("<.1 .2 .3 .4>").sustain(0)
defaultmidimap
configures the default midimap, which is used when no "midimap" port is set


defaultmidimap({ lpf: 74 })
$: note("c a f e").midi();
$: lpf(sine.slow(4).segment(16)).midi();
defragmentHaps
Combines adjacent haps with the same value and whole. Only intended for use in tests.


degrade
Randomly removes 50% of events from the pattern. Shorthand for .degradeBy(0.5)


s("hh*8").degrade()
s("[hh?]*8")
degradeBy
Randomly removes events from the pattern by a given amount. 0 = 0% chance of removal 1 = 100% chance of removal


amount : number - a number between 0 and 1
s("hh*8").degradeBy(0.2)
s("[hh?0.2]*8")
//beat generator
s("bd").segment(16).degradeBy(.5).ribbon(16,1)
delay
Sets the level of the delay signal.

When using mininotation, you can also optionally add the 'delaytime' and 'delayfeedback' parameter, separated by ':'.


level : number | Pattern - between 0 and 1
s("bd bd").delay("<0 .25 .5 1>")
s("bd bd").delay("0.65:0.25:0.9 0.65:0.125:0.7")
delayfeedback
Synonyms: delayfb, dfb

Sets the level of the signal that is fed back into the delay. Caution: Values >= 1 will result in a signal that gets louder and louder! Don't do it


feedback : number | Pattern - between 0 and 1
s("bd").delay(.25).delayfeedback("<.25 .5 .75 1>")
delaytime
Synonyms: delayt, dt

Sets the time of the delay effect.


seconds : number | Pattern - between 0 and Infinity
s("bd bd").delay(.25).delaytime("<.125 .25 .5 1>")
density
Noise crackle density


density : number | Pattern - between 0 and x
s("crackle*4").density("<0.01 0.04 0.2 0.5>".slow(4))
detune
Synonyms: det

Set detune for stacked voices of supported oscillators


amount : number | Pattern
note("d f a a# a d3").fast(2).s("supersaw").detune("<.1 .2 .5 24.1>")
discreteOnly
Returns a new pattern, with 'continuous' haps (those without 'whole' timespans) removed from query results.


distort
Synonyms: dist

Wave shaping distortion. CAUTION: it can get loud. Second option in optional array syntax (ex: ".9:.5") applies a postgain to the output. Most useful values are usually between 0 and 10 (depending on source gain). If you are feeling adventurous, you can turn it up to 11 and beyond ;)


distortion : number | Pattern
s("bd sd [~ bd] sd,hh*8").distort("<0 2 3 10:.5>")
note("d1!8").s("sine").penv(36).pdecay(.12).decay(.23).distort("8:.4")
div
Divides each number by the given factor.


djf
DJ filter, below 0.5 is low pass filter, above is high pass filter.


cutoff : number | Pattern - below 0.5 is low pass filter, above is high pass filter
n("0 3 7 [10,24]").s('superzow').octave(3).djf("<.5 .25 .5 .75>").osc()
drawLine
Intended for a debugging, drawLine renders the pattern as a string, where each character represents the same time span. Should only be used with single characters as values, otherwise the character slots will be messed up. Character legend:

"|" cycle separator
"-" hold previous value
"." silence

pattern : Pattern - the pattern to use
chars : number - max number of characters (approximately)
const line = drawLine("0 [1 2 3]", 10); // |0--123|0--123
console.log(line);
silence;
drive
filter overdrive for supported filter types


amount : number | Pattern
note("{f g g c d a a#}%16".sub(17)).s("supersaw").lpenv(8).lpf(150).lpq(.8).ftype('ladder').drive("<.5 4>")
drop
Experimental

Drops the given number of steps from a pattern. A positive number will drop steps from the start of a pattern, and a negative number from the end.


"tha dhi thom nam".drop("1").sound().bank("mridangam")
"tha dhi thom nam".drop("-1").sound().bank("mridangam")
"tha dhi thom nam".drop("0 1 2 3").sound().bank("mridangam")
"tha dhi thom nam".drop("0 -1 -2 -3").sound().bank("mridangam")
dry
Set dryness of reverb. See room and size for more information about reverb.


dry : number | Pattern - 0 = wet, 1 = dry
n("[0,3,7](3,8)").s("superpiano").room(.7).dry("<0 .5 .75 1>").osc()
duration
Synonyms: dur

Sets the duration of the event in cycles. Similar to clip / legato, it also cuts samples off at the end if they exceed the duration.


seconds : number | Pattern - = 0
note("c a f e").s("piano").dur("<.5 1 2>")
each
Applies a function to each of the running patterns separately. This is intended for future use with upcoming 'stepwise' features. See all for a version that applies the function to all the patterns stacked together into a single pattern.

$: sound("bd - cp sd")
$: sound("hh*8")
each(fast("<2 3>"))

early
Nudge a pattern to start earlier in time. Equivalent of Tidal's <~ operator


cycles : number | Pattern - number of cycles to nudge left
"bd ~".stack("hh ~".early(.1)).s()
echo
Superimpose and offset multiple times, gradually decreasing the velocity


times : number - how many times to repeat
time : number - cycle offset between iterations
feedback : number - velocity multiplicator for each iteration
s("bd sd").echo(3, 1/6, .8)
echoWith
Synonyms: echowith, stutWith, stutwith

Superimpose and offset multiple times, applying the given function each time.


times : number - how many times to repeat
time : number - cycle offset between iterations
func : function - function to apply, given the pattern and the iteration index
"<0 [2 4]>"
.echoWith(4, 1/8, (p,n) => p.add(n*2))
.scale("C:minor").note()
end
The same as .begin, but cuts off the end off each sample.


length : number | Pattern - 1 = whole sample, .5 = half sample, .25 = quarter sample etc..
s("bd*2,oh*4").end("<.1 .2 .5 1>").fast(2)
euclid
Changes the structure of the pattern to form an Euclidean rhythm. Euclidean rhythms are rhythms obtained using the greatest common divisor of two numbers. They were described in 2004 by Godfried Toussaint, a Canadian computer scientist. Euclidean rhythms are really useful for computer/algorithmic music because they can describe a large number of rhythms with a couple of numbers.


pulses : number - the number of onsets/beats
steps : number - the number of steps to fill
// The Cuban tresillo pattern.
note("c3").euclid(3,8)
euclidLegato
Similar to euclid, but each pulse is held until the next pulse, so there will be no gaps.


pulses : number - the number of onsets/beats
steps : number - the number of steps to fill
rotation : - offset in steps
pat :
note("c3").euclidLegato(3,8)
euclidLegatoRot
Similar to euclid, but each pulse is held until the next pulse, so there will be no gaps, and has an additional parameter for 'rotating' the resulting sequence


pulses : number - the number of onsets/beats
steps : number - the number of steps to fill
rotation : number - offset in steps
note("c3").euclidLegatoRot(3,5,2)
euclidRot
Like euclid, but has an additional parameter for 'rotating' the resulting sequence.


pulses : number - the number of onsets/beats
steps : number - the number of steps to fill
rotation : number - offset in steps
// A Samba rhythm necklace from Brazil
note("c3").euclidRot(3,16,14)
every
An alias for firstOf


n : number - how many cycles
func : function - function to apply
note("c3 d3 e3 g3").every(4, x=>x.rev())
expand
Experimental

Expands the step size of the pattern by the given factor.


sound("tha dhi thom nam").bank("mridangam").expand("3 2 1 1 2 3").pace(8)
extend
Experimental

extend is similar to fast in that it increases its density, but it also increases the step count accordingly. So stepcat("a b".extend(2), "c d") would be the same as "a b a b c d", whereas stepcat("a b".fast(2), "c d") would be the same as "[a b] [a b] c d".


stepcat(
  sound("bd bd - cp").extend(2),
  sound("bd - sd -")
).pace(8)
fanchor
controls the center of the filter envelope. 0 is unipolar positive, .5 is bipolar, 1 is unipolar negative


center : number | Pattern - 0 to 1
note("{f g g c d a a#}%8").s("sawtooth").lpf("{1000}%2")
.lpenv(8).fanchor("<0 .5 1>")
fast
Synonyms: density

Speed up a pattern by the given factor. Used by "*" in mini notation.


factor : number | Pattern - speed up factor
s("bd hh sd hh").fast(2) // s("[bd hh sd hh]*2")
fastChunk
Synonyms: fastchunk

Like chunk, but the cycles of the source pattern aren't repeated for each set of chunks.


"<0 8> 1 2 3 4 5 6 7"
.fastChunk(4, x => x.color('red')).slow(2)
.scale("C2:major").note()
fastGap
Synonyms: fastgap

speeds up a pattern like fast, but rather than it playing multiple times as fast would it instead leaves a gap in the remaining space of the cycle. For example, the following will play the sound pattern "bd sn" only once but compressed into the first half of the cycle, i.e. twice as fast.


s("bd sd").fastGap(2)
filter
Filters haps using the given function


test : function - function to test Hap
s("hh!7 oh").filter(hap => hap.value.s==='hh')
filterHaps
Returns a new Pattern, which only returns haps that meet the given test.


hap_test : function - a function which returns false for haps to be removed from the pattern
filterValues
As with filterHaps, but the function is applied to values inside haps.


value_test : function
filterWhen
Filters haps by their begin time


test : function - function to test Hap.whole.begin
findPeaks
Find peaks in spectrum magnitudes


firstCycle
Queries the pattern for the first cycle, returning Haps. Mainly of use when debugging a pattern.


with_context : Boolean - set to true, otherwise the context field will be stripped from the resulting haps.
firstCycleValues
Accessor for a list of values returned by querying the first cycle.


firstOf
Applies the given function every n cycles, starting from the first cycle.


n : number - how many cycles
func : function - function to apply
note("c3 d3 e3 g3").firstOf(4, x=>x.rev())
fit
Makes the sample fit its event duration. Good for rhythmical loops like drum breaks. Similar to loopAt.


samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes/2").fit()
floor
Assumes a numerical pattern. Returns a new pattern with all values set to their mathematical floor. E.g. 3.7 replaced with to 3, and -4.2 replaced with -5.


note("42 42.1 42.5 43".floor())
fm
Synonyms: fmi

Sets the Frequency Modulation of the synth. Controls the modulation index, which defines the brightness of the sound.


brightness : number | Pattern - modulation index
note("c e g b g e")
.fm("<0 1 2 8 32>")
._scope()
fmap
see withValue


fmattack
Attack time for the FM envelope: time it takes to reach maximum modulation


time : number | Pattern - attack time
note("c e g b g e")
.fm(4)
.fmattack("<0 .05 .1 .2>")
._scope()
fmdecay
Decay time for the FM envelope: seconds until the sustain level is reached after the attack phase.


time : number | Pattern - decay time
note("c e g b g e")
.fm(4)
.fmdecay("<.01 .05 .1 .2>")
.fmsustain(.4)
._scope()
fmenv
Ramp type of fm envelope. Exp might be a bit broken..


type : number | Pattern - lin | exp
note("c e g b g e")
.fm(4)
.fmdecay(.2)
.fmsustain(0)
.fmenv("<exp lin>")
._scope()
fmh
Sets the Frequency Modulation Harmonicity Ratio. Controls the timbre of the sound. Whole numbers and simple ratios sound more natural, while decimal numbers and complex ratios sound metallic.


harmonicity : number | Pattern
note("c e g b g e")
.fm(4)
.fmh("<1 2 1.5 1.61>")
._scope()
fmsustain
Sustain level for the FM envelope: how much modulation is applied after the decay phase


level : number | Pattern - sustain level
note("c e g b g e")
.fm(4)
.fmdecay(.1)
.fmsustain("<1 .75 .5 0>")
._scope()
focus
Similar to compress, but doesn't leave gaps, and the 'focus' can be bigger than a cycle


s("bd hh sd hh").focus(1/4, 3/4)
freq
Set frequency of sound.


frequency : number | Pattern - in Hz. the audible range is between 20 and 20000 Hz
freq("220 110 440 110").s("superzow").osc()
freq("110".mul.out(".5 1.5 .6 [2 3]")).s("superzow").osc()
fromBipolar
Assumes a numerical pattern, containing bipolar values in the range -1 .. 1 Returns a new pattern with values scaled to the unipolar range 0 .. 1


fscope
Renders an oscilloscope for the frequency domain of the audio signal.


color : string - line color as hex or color name. defaults to white.
scale : number - scales the y-axis. Defaults to 0.25
pos : number - y-position relative to screen height. 0 = top, 1 = bottom of screen
lean : number - y-axis alignment where 0 = top and 1 = bottom
min : number - min value
max : number - max value
s("sawtooth").fscope()
ftype
Sets the filter type. The ladder filter is more aggressive. More types might be added in the future.


type : number | Pattern - 12db (0), ladder (1), or 24db (2)
note("{f g g c d a a#}%8").s("sawtooth").lpenv(4).lpf(500).ftype("<0 1 2>").lpq(1)
note("c f g g a c d4").fast(2)
.sound('sawtooth')
.lpf(200).fanchor(0)
.lpenv(3).lpq(1)
.ftype("<ladder 12db 24db>")
gain
Controls the gain by an exponential amount.


amount : number | Pattern - gain.
s("hh*8").gain(".4!2 1 .4!2 1 .4 1").fast(2)
gap
Does absolutely nothing, but with a given metrical 'steps'


steps : number
gap(3) // "~@3"
generateGraph
Creates a canvas element showing a graph of the given data.


data : Float32Array - An array of numbers, or a Float32Array.
width : number - Width in pixels of the canvas.
height : number - Height in pixels of the canvas.
min : number - Minimum value of data for the graph (lower edge).
max : number - Maximum value of data in the graph (upper edge).
generateReverb
Generates a reverb impulse response.


params : Object - TODO: Document the properties.
callback : function - Function to call when the impulse response has been generated. The impulse response is passed to this function as its parameter. May be called immediately within the current execution context, or later.
gravityX
Synonyms: gravX

The device's gravity x-axis value ranges from 0 to 1.


n(gravityX.segment(4).range(0,7)).scale("C:minor")
gravityY
Synonyms: gravY

The device's gravity y-axis value ranges from 0 to 1.


n(gravityY.segment(4).range(0,7)).scale("C:minor")
gravityZ
Synonyms: gravZ

The device's gravity z-axis value ranges from 0 to 1.


n(gravityZ.segment(4).range(0,7)).scale("C:minor")
grow
Experimental

Progressively grows the pattern by 'n' steps until the full pattern is played, or if a second value is given (using mininotation list syntax with :), that number of times. A positive number will progressively grow steps from the start of a pattern, and a negative number from the end.


"tha dhi thom nam".grow("1").sound()
.bank("mridangam")
"tha dhi thom nam".grow("-1").sound()
.bank("mridangam")
"tha dhi thom nam".grow("1 -1").sound().bank("mridangam").pace(4)
note("0 1 2 3 4 5 6 7".scale("C:ritusen")).sound("folkharp")
   .grow("1 -1").pace(8)
handleOutputBuffersToRetrieve
Add contents of output buffers just processed to output buffers


hpattack
Synonyms: hpa

Sets the attack duration for the highpass filter envelope.


attack : number | Pattern - time of the highpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpa("<.5 .25 .1 .01>/4")
.hpenv(4)
hpdecay
Synonyms: hpd

Sets the decay duration for the highpass filter envelope.


decay : number | Pattern - time of the highpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpd("<.5 .25 .1 0>/4")
.hps(0.2)
.hpenv(4)
hpenv
Synonyms: hpe

Sets the highpass filter envelope modulation depth.


modulation : number | Pattern - depth of the highpass filter envelope between 0 and n
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpa(.5)
.hpenv("<4 2 1 0 -1 -2 -4>/4")
hpf
Synonyms: hp, hcutoff

Applies the cutoff frequency of the high-pass filter.

When using mininotation, you can also optionally add the 'hpq' parameter, separated by ':'.


frequency : number | Pattern - audible between 0 and 20000
s("bd sd [~ bd] sd,hh*8").hpf("<4000 2000 1000 500 200 100>")
s("bd sd [~ bd] sd,hh*8").hpf("<2000 2000:25>")
hpq
Synonyms: hresonance

Controls the high-pass q-value.


q : number | Pattern - resonance factor between 0 and 50
s("bd sd [~ bd] sd,hh*8").hpf(2000).hpq("<0 10 20 30>")
hprelease
Synonyms: hpr

Sets the release time for the highpass filter envelope.


release : number | Pattern - time of the highpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.clip(.5)
.hpf(500)
.hpenv(4)
.hpr("<.5 .25 .1 0>/4")
.release(.5)
hpsustain
Synonyms: hps

Sets the sustain amplitude for the highpass filter envelope.


sustain : number | Pattern - amplitude of the highpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpd(.5)
.hps("<0 .25 .5 1>/4")
.hpenv(4)
hurry
Both speeds up the pattern (like 'fast') and the sample playback (like 'speed').


s("bd sd:2").hurry("<1 2 4 3>").slow(1.5)
hush
Silences a pattern.


stack(
  s("bd").hush(),
  s("hh*3")
)
inhabit
Synonyms: pickSqueeze

Picks patterns (or plain values) either from a list (by index) or a lookup table (by name). Similar to pick, but cycles are squeezed into the target ('inhabited') pattern.


pat : Pattern
xs : *
"<a b [a,b]>".inhabit({a: s("bd(3,8)"),
                            b: s("cp sd")
                           })
s("a@2 [a b] a".inhabit({a: "bd(3,8)", b: "sd sd"})).slow(4)
inhabitmod
Synonyms: pickmodSqueeze

The same as inhabit, but if you pick a number greater than the size of the list, it wraps around, rather than sticking at the maximum value. For example, if you pick the fifth pattern of a list of three, you'll get the second one.


pat : Pattern
xs : *
inside
Carries out an operation 'inside' a cycle.


"0 1 2 3 4 3 2 1".inside(4, rev).scale('C major').note()
// "0 1 2 3 4 3 2 1".slow(4).rev().fast(4).scale('C major').note()
invert
Synonyms: inv

Swaps 1s and 0s in a binary pattern.


s("bd").struct("1 0 0 1 0 0 1 0".lastOf(4, invert))
irand
A continuous pattern of random integers, between 0 and n-1.


n : number - max value (exclusive)
// randomly select scale notes from 0 - 7 (= C to C)
n(irand(8)).struct("x x*2 x x*3").scale("C:minor")
iresponse
Synonyms: ir

Sets the sample to use as an impulse response for the reverb.


sample : string | Pattern - to use as an impulse response
s("bd sd [~ bd] sd").room(.8).ir("<shaker_large:0 shaker_large:2>")
isaw
A sawtooth signal between 1 and 0 (like saw, but flipped).


note("<c3 [eb3,g3] g2 [g3,bb3]>*8")
.clip(isaw.slow(2))
n(isaw.range(0,8).segment(8))
.scale('C major')
isaw2
A sawtooth signal between 1 and -1 (like saw2, but flipped).


iter
Divides a pattern into a given number of subdivisions, plays the subdivisions in order, but increments the starting subdivision each cycle. The pattern wraps to the first subdivision after the last subdivision is played.


note("0 1 2 3".scale('A minor')).iter(4)
iterBack
Synonyms: iterback

Like iter, but plays the subdivisions in reverse order. Known as iter' in tidalcycles


note("0 1 2 3".scale('A minor')).iterBack(4)
itri
An inverted triangle signal between 1 and 0 (like tri, but flipped).


n(itri.segment(8).range(0,7)).scale("C:minor")
itri2
An inverted triangle signal between -1 and 1 (like itri, but bipolar).


jux
The jux function creates strange stereo effects, by applying a function to a pattern, but only in the right-hand channel.


s("bd lt [~ ht] mt cp ~ bd hh").jux(rev)
s("bd lt [~ ht] mt cp ~ bd hh").jux(press)
s("bd lt [~ ht] mt cp ~ bd hh").jux(iter(4))
juxBy
Synonyms: juxby

Jux with adjustable stereo width. 0 = mono, 1 = full stereo.


s("bd lt [~ ht] mt cp ~ bd hh").juxBy("<0 .5 1>/2", rev)
keyDown
returns true when a key or array of keys is held Key name reference


keyDown("Control:j").pick([s("bd(5,8)"), s("cp(3,8)")])
label
Sets the displayed text for an event on the pianoroll


label : string - text to display
lastOf
Applies the given function every n cycles, starting from the last cycle.


n : number - how many cycles
func : function - function to apply
note("c3 d3 e3 g3").lastOf(4, x=>x.rev())
late
Nudge a pattern to start later in time. Equivalent of Tidal's ~> operator


cycles : number | Pattern - number of cycles to nudge right
"bd ~".stack("hh ~".late(.1)).s()
layer
Synonyms: apply

Layers the result of the given function(s). Like superimpose, but without the original pattern:


"<0 2 4 6 ~ 4 ~ 2 0!3 ~!5>*8"
  .layer(x=>x.add("0,2"))
  .scale('C minor').note()
leslie
Emulation of a Leslie speaker: speakers rotating in a wooden amplified cabinet.


wet : number | Pattern - between 0 and 1
n("0,4,7").s("supersquare").leslie("<0 .4 .6 1>").osc()
linger
Selects the given fraction of the pattern and repeats that part to fill the remainder of the cycle.


fraction : number - fraction to select
s("lt ht mt cp, [hh oh]*2").linger("<1 .5 .25 .125>")
loop
Loops the sample. Note that the tempo of the loop is not synced with the cycle tempo. To change the loop region, use loopBegin / loopEnd.


on : number | Pattern - If 1, the sample is looped
s("casio").loop(1)
loopAt
Makes the sample fit the given number of cycles by changing the speed.


samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes").loopAt(2)
loopAtCps
Makes the sample fit the given number of cycles and cps value, by changing the speed. Please note that at some point cps will be given by a global clock and this function will be deprecated/removed.


samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes").loopAtCps(4,1.5).cps(1.5)
loopBegin
Synonyms: loopb

Begin to loop at a specific point in the sample (inbetween begin and end). Note that the loop point must be inbetween begin and end, and before loopEnd! Note: Samples starting with wt_ will automatically loop! (wt = wavetable)


time : number | Pattern - between 0 and 1, where 1 is the length of the sample
s("space").loop(1)
.loopBegin("<0 .125 .25>")._scope()
loopEnd
Synonyms: loope

End the looping section at a specific point in the sample (inbetween begin and end). Note that the loop point must be inbetween begin and end, and after loopBegin!


time : number | Pattern - between 0 and 1, where 1 is the length of the sample
s("space").loop(1)
.loopEnd("<1 .75 .5 .25>")._scope()
lpattack
Synonyms: lpa

Sets the attack duration for the lowpass filter envelope.


attack : number | Pattern - time of the filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpa("<.5 .25 .1 .01>/4")
.lpenv(4)
lpdecay
Synonyms: lpd

Sets the decay duration for the lowpass filter envelope.


decay : number | Pattern - time of the filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpd("<.5 .25 .1 0>/4")
.lpenv(4)
lpenv
Synonyms: lpe

Sets the lowpass filter envelope modulation depth.


modulation : number | Pattern - depth of the lowpass filter envelope between 0 and n
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpa(.5)
.lpenv("<4 2 1 0 -1 -2 -4>/4")
lpf
Synonyms: cutoff, ctf, lp

Applies the cutoff frequency of the low-pass filter.

When using mininotation, you can also optionally add the 'lpq' parameter, separated by ':'.


frequency : number | Pattern - audible between 0 and 20000
s("bd sd [~ bd] sd,hh*6").lpf("<4000 2000 1000 500 200 100>")
s("bd*16").lpf("1000:0 1000:10 1000:20 1000:30")
lpq
Synonyms: resonance

Controls the low-pass q-value.


q : number | Pattern - resonance factor between 0 and 50
s("bd sd [~ bd] sd,hh*8").lpf(2000).lpq("<0 10 20 30>")
lprelease
Synonyms: lpr

Sets the release time for the lowpass filter envelope.


release : number | Pattern - time of the filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.clip(.5)
.lpf(300)
.lpenv(4)
.lpr("<.5 .25 .1 0>/4")
.release(.5)
lpsustain
Synonyms: lps

Sets the sustain amplitude for the lowpass filter envelope.


sustain : number | Pattern - amplitude of the lowpass filter envelope
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpd(.5)
.lps("<0 .25 .5 1>/4")
.lpenv(4)
lrate
Rate of modulation / rotation for leslie effect


rate : number | Pattern - 6.7 for fast, 0.7 for slow
n("0,4,7").s("supersquare").leslie(1).lrate("<1 2 4 8>").osc()
lsize
Physical size of the cabinet in meters. Be careful, it might be slightly larger than your computer. Affects the Doppler amount (pitch warble)


meters : number | Pattern - somewhere between 0 and 1
n("0,4,7").s("supersquare").leslie(1).lrate(2).lsize("<.1 .5 1>").osc()
markcss
Overrides the css of highlighted events. Make sure to use single quotes!


note("c a f e")
.markcss('text-decoration:underline')
mask
Returns silence when mask is 0 or "~"


note("c [eb,g] d [eb,g]").mask("<1 [0 1]>")
midi
MIDI output: Opens a MIDI output port.


midiport : string | number - MIDI device name or index defaulting to 0
options : object - Additional MIDI configuration options
note("c4").midichan(1).midi('IAC Driver Bus 1')
note("c4").midichan(1).midi('IAC Driver Bus 1', { controller: true, latency: 50 })
midibend
MIDI pitch bend: Sends a MIDI pitch bend message.


midibend : number | Pattern - MIDI pitch bend (-1 - 1)
note("c4").midibend(sine.slow(4).range(-0.4,0.4)).midi()
midichan
MIDI channel: Sets the MIDI channel for the event.


channel : number | Pattern - MIDI channel number (0-15)
note("c4").midichan(1).midi()
midicmd
MIDI command: Sends a MIDI command message.


command : number | Pattern - MIDI command
midicmd("clock*48,<start stop>/2").midi()
midimaps
Adds midimaps to the registry. Inside each midimap, control names (e.g. lpf) are mapped to cc numbers.


midimaps({ mymap: { lpf: 74 } })
$: note("c a f e")
.lpf(sine.slow(4))
.midimap('mymap')
.midi()
midimaps({ mymap: {
  lpf: { ccn: 74, min: 0, max: 20000, exp: 0.5 }
}})
$: note("c a f e")
.lpf(sine.slow(2).range(400,2000))
.midimap('mymap')
.midi()
midin
MIDI input: Opens a MIDI input port to receive MIDI control change messages.


input : string | number - MIDI device name or index defaulting to 0
let cc = await midin('IAC Driver Bus 1')
note("c a f e").lpf(cc(0).range(0, 1000)).lpq(cc(1).range(0, 10)).sound("sawtooth")
midiport
MIDI port: Sets the MIDI port for the event.


port : number | Pattern - MIDI port
note("c a f e").midiport("<0 1 2 3>").midi()
miditouch
MIDI key after touch: Sends a MIDI key after touch message.


miditouch : number | Pattern - MIDI key after touch (0-1)
note("c4").miditouch(sine.slow(4).range(0,1)).midi()
mousex
The mouse's x position value ranges from 0 to 1.


n(mousex.segment(4).range(0,7)).scale("C:minor")
mousey
The mouse's y position value ranges from 0 to 1.


n(mousey.segment(4).range(0,7)).scale("C:minor")
mul
Multiplies each number by the given factor.


"<1 1.5 [1.66, <2 2.33>]>*4".mul(150).freq()
n
Selects the given index from the sample map. Numbers too high will wrap around. n can also be used to play midi numbers, but it is recommended to use note instead.


value : number | Pattern - sample index starting from 0
s("bd sd [~ bd] sd,hh*6").n("<0 1>")
never
Shorthand for .sometimesBy(0, fn) (never calls fn)


s("hh*8").never(x=>x.speed("0.5"))
noise
Adds pink noise to the mix


wet : number | Pattern - wet amount
sound("<white pink brown>/2")
note
Plays the given note name or midi number. A note name consists of

a letter (a-g or A-G)
optional accidentals (b or #)
optional octave number (0-9). Defaults to 3
Examples of valid note names: c, bb, Bb, f#, c3, A4, Eb2, c#5

You can also use midi numbers instead of note names, where 69 is mapped to A4 440Hz in 12EDO.


note("c a f e")
note("c4 a4 f4 e4")
note("60 69 65 64")
nrpnn
MIDI NRPN non-registered parameter number: Sends a MIDI NRPN non-registered parameter number message.


nrpnn : number | Pattern - MIDI NRPN non-registered parameter number (0-127)
note("c4").nrpnn("1:8").nrpv("123").midichan(1).midi()
nrpv
MIDI NRPN non-registered parameter value: Sends a MIDI NRPN non-registered parameter value message.


nrpv : number | Pattern - MIDI NRPN non-registered parameter value (0-127)
note("c4").nrpnn("1:8").nrpv("123").midichan(1).midi()
octave
Sets the default octave of a synth.


octave : number | Pattern - octave number
n("0,4,7").s('supersquare').octave("<3 4 5 6>").osc()
off
Superimposes the function result on top of the original pattern, delayed by the given time.


time : Pattern | number - offset time
func : function - function to apply
"c3 eb3 g3".off(1/8, x=>x.add(7)).note()
often
Shorthand for .sometimesBy(0.75, fn)


s("hh*8").often(x=>x.speed("0.5"))
onsetsOnly
Returns a new pattern, with all haps without onsets filtered out. A hap with an onset is one with a whole timespan that begins at the same time as its part timespan.


onTriggerTime
make something happen on event time uses browser timeout which is innacurate for audio tasks


s("bd!8").onTriggerTime((hap) => {console.info(hap)})
orbit
An orbit is a global parameter context for patterns. Patterns with the same orbit will share the same global effects.


number : number | Pattern
stack(
  s("hh*6").delay(.5).delaytime(.25).orbit(1),
  s("~ sd ~ sd").delay(.5).delaytime(.125).orbit(2)
)
orientationAlpha
Synonyms: oriA, oriZ, orientationZ

The device's orientation alpha value ranges from 0 to 1.


n(orientationAlpha.segment(4).range(0,7)).scale("C:minor")
orientationBeta
Synonyms: oriB, oriX, orientationX

The device's orientation beta value ranges from 0 to 1.


n(orientationBeta.segment(4).range(0,7)).scale("C:minor")
orientationGamma
Synonyms: oriG, oriY, orientationY

The device's orientation gamma value ranges from 0 to 1.


n(orientationGamma.segment(4).range(0,7)).scale("C:minor")
osc
Sends each hap as an OSC message, which can be picked up by SuperCollider or any other OSC-enabled software. For more info, read MIDI & OSC in the docs


outside
Carries out an operation 'outside' a cycle.


"<[0 1] 2 [3 4] 5>".outside(4, rev).scale('C major').note()
// "<[0 1] 2 [3 4] 5>".fast(4).rev().slow(4).scale('C major').note()
pace
Experimental

Speeds a pattern up or down, to fit to the given number of steps per cycle.


sound("bd sd cp").pace(4)
// The same as sound("{bd sd cp}%4") or sound("<bd sd cp>*4")
palindrome
Applies rev to a pattern every other cycle, so that the pattern alternates between forwards and backwards.


note("c d e g").palindrome()
pan
Sets position in stereo.


pan : number | Pattern - between 0 and 1, from left to right (assuming stereo), once round a circle (assuming multichannel)
s("[bd hh]*2").pan("<.5 1 .5 0>")
s("bd rim sd rim bd ~ cp rim").pan(sine.slow(2))
panchor
Sets the range anchor of the envelope:

anchor 0: range = [note, note + penv]
anchor 1: range = [note - penv, note] If you don't set an anchor, the value will default to the psustain value.

anchor : number | Pattern - anchor offset
note("c c4").penv(12).panchor("<0 .5 1 .5>")
pattack
Synonyms: patt

Attack time of pitch envelope.


time : number | Pattern - time in seconds
note("c eb g bb").pattack("0 .1 .25 .5").slow(2)
Pattern
Create a pattern. As an end user, you will most likely not create a Pattern directly.


query : function - The function that maps a State to an array of Hap.
pcurve
Curve of envelope. Defaults to linear. exponential is good for kicks


type : number | Pattern - 0 = linear, 1 = exponential
note("g1*4")
.s("sine").pdec(.5)
.penv(32)
.pcurve("<0 1>")
pdecay
Synonyms: pdec

Decay time of pitch envelope.


time : number | Pattern - time in seconds
note("<c eb g bb>").pdecay("<0 .1 .25 .5>")
penv
Amount of pitch envelope. Negative values will flip the envelope. If you don't set other pitch envelope controls, pattack:.2 will be the default.


semitones : number | Pattern - change in semitones
note("c")
.penv("<12 7 1 .5 0 -1 -7 -12>")
perlin
Generates a continuous pattern of perlin noise, in the range 0..1.


// randomly change the cutoff
s("bd*4,hh*8").cutoff(perlin.range(500,8000))
phaser
Synonyms: ph

Phaser audio effect that approximates popular guitar pedals.


speed : number | Pattern - speed of modulation
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser("<1 2 4 8>")
phasercenter
Synonyms: phc

The center frequency of the phaser in HZ. Defaults to 1000


centerfrequency : number | Pattern - in HZ
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser(2).phasercenter("<800 2000 4000>")
phaserdepth
Synonyms: phd

The amount the signal is affected by the phaser effect. Defaults to 0.75


depth : number | Pattern - number between 0 and 1
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser(2).phaserdepth("<0 .5 .75 1>")
phasersweep
Synonyms: phs

The frequency sweep range of the lfo for the phaser effect. Defaults to 2000


phasersweep : number | Pattern - most useful values are between 0 and 4000
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser(2).phasersweep("<800 2000 4000>")
pianoroll
Synonyms: punchcard

Visualises a pattern as a scrolling 'pianoroll', displayed in the background of the editor. To show a pianoroll for all running patterns, use all(pianoroll). To have a pianoroll appear below a pattern instead, prefix with _, e.g.: sound("bd sd")._pianoroll().


options : Object - Object containing all the optional following parameters as key value pairs:
cycles : integer - number of cycles to be displayed at the same time - defaults to 4
playhead : number - location of the active notes on the time axis - 0 to 1, defaults to 0.5
vertical : boolean - displays the roll vertically - 0 by default
labels : boolean - displays labels on individual notes (see the label function) - 0 by default
flipTime : boolean - reverse the direction of the roll - 0 by default
flipValues : boolean - reverse the relative location of notes on the value axis - 0 by default
overscan : number - lookup X cycles outside of the cycles window to display notes in advance - 1 by default
hideNegative : boolean - hide notes with negative time (before starting playing the pattern) - 0 by default
smear : boolean - notes leave a solid trace - 0 by default
fold : boolean - notes takes the full value axis width - 0 by default
active : string - hexadecimal or CSS color of the active notes - defaults to #FFCA28
inactive : string - hexadecimal or CSS color of the inactive notes - defaults to #7491D2
background : string - hexadecimal or CSS color of the background - defaults to transparent
playheadColor : string - hexadecimal or CSS color of the line representing the play head - defaults to white
fill : boolean - notes are filled with color (otherwise only the label is displayed) - 0 by default
fillActive : boolean - active notes are filled with color - 0 by default
stroke : boolean - notes are shown with colored borders - 0 by default
strokeActive : boolean - active notes are shown with colored borders - 0 by default
hideInactive : boolean - only active notes are shown - 0 by default
colorizeInactive : boolean - use note color for inactive notes - 1 by default
fontFamily : string - define the font used by notes labels - defaults to 'monospace'
minMidi : integer - minimum note value to display on the value axis - defaults to 10
maxMidi : integer - maximum note value to display on the value axis - defaults to 90
autorange : boolean - automatically calculate the minMidi and maxMidi parameters - 0 by default
note("c2 a2 eb2")
.euclid(5,8)
.s('sawtooth')
.lpenv(4).lpf(300)
.pianoroll({ labels: 1 })
pick
Picks patterns (or plain values) either from a list (by index) or a lookup table (by name). Similar to inhabit, but maintains the structure of the original patterns.


pat : Pattern
xs : *
note("<0 1 2!2 3>".pick(["g a", "e f", "f g f g" , "g c d"]))
sound("<0 1 [2,0]>".pick(["bd sd", "cp cp", "hh hh"]))
sound("<0!2 [0,1] 1>".pick(["bd(3,8)", "sd sd"]))
s("<a!2 [a,b] b>".pick({a: "bd(3,8)", b: "sd sd"}))
pickF
pickF lets you use a pattern of numbers to pick which function to apply to another pattern.


pat : Pattern
lookup : Pattern - a pattern of indices
funcs : Array.<function()> - the array of functions from which to pull
s("bd [rim hh]").pickF("<0 1 2>", [rev,jux(rev),fast(2)])
note("<c2 d2>(3,8)").s("square")
    .pickF("<0 2> 1", [jux(rev),fast(2),x=>x.lpf(800)])
pickmod
The same as pick, but if you pick a number greater than the size of the list, it wraps around, rather than sticking at the maximum value. For example, if you pick the fifth pattern of a list of three, you'll get the second one.


pat : Pattern
xs : *
pickmodF
The same as pickF, but if you pick a number greater than the size of the functions list, it wraps around, rather than sticking at the maximum value.


pat : Pattern
lookup : Pattern - a pattern of indices
funcs : Array.<function()> - the array of functions from which to pull
pickmodOut
The same as pickOut, but if you pick a number greater than the size of the list, it wraps around, rather than sticking at the maximum value.


pat : Pattern
xs : *
pickmodReset
The same as pickReset, but if you pick a number greater than the size of the list, it wraps around, rather than sticking at the maximum value.


pat : Pattern
xs : *
pickmodRestart
The same as pickRestart, but if you pick a number greater than the size of the list, it wraps around, rather than sticking at the maximum value.


pat : Pattern
xs : *
"<a@2 b@2 c@2 d@2>".pickRestart({
        a: n("0 1 2 0"),
        b: n("2 3 4 ~"),
        c: n("[4 5] [4 3] 2 0"),
        d: n("0 -3 0 ~")
      }).scale("C:major").s("piano")
pickOut
Similar to pick, but it applies an outerJoin instead of an innerJoin.


pat : Pattern
xs : *
pickReset
Similar to pick, but the choosen pattern is reset when its index is triggered.


pat : Pattern
xs : *
pickRestart
Similar to pick, but the choosen pattern is restarted when its index is triggered.


pat : Pattern
xs : *
pitchwheel
Renders a pitch circle to visualize frequencies within one octave


hapcircles : number
circle : number
edo : number
root : string
thickness : number
hapRadius : number
mode : string
margin : number
n("0 .. 12").scale("C:chromatic")
.s("sawtooth")
.lpf(500)
._pitchwheel()
ply
The ply function repeats each event the given number of times.


s("bd ~ sd cp").ply("<1 2 3>")
polymeter
Synonyms: pm

Experimental

Aligns the steps of the patterns, creating polymeters. The patterns are repeated until they all fit the cycle. For example, in the below the first pattern is repeated twice, and the second is repeated three times, to fit the lowest common multiple of six steps.


// The same as note("{c eb g, c2 g2}%6")
polymeter("c eb g", "c2 g2").note()
postgain
Gain applied after all effects have been processed.


s("bd sd [~ bd] sd,hh*8")
.compressor("-20:20:10:.002:.02").postgain(1.5)
prelease
Synonyms: prel

Release time of pitch envelope


time : number | Pattern - time in seconds
note("<c eb g bb> ~")
.release(.5) // to hear the pitch release
.prelease("<0 .1 .25 .5>")
prepareInputBuffersToSend
Copy contents of input buffers to buffer actually sent to process


press
Syncopates a rhythm, by shifting each event halfway into its timespan.


stack(s("hh*4"),
      s("bd mt sd ht").every(4, press)
     ).slow(2)
pressBy
Like press, but allows you to specify the amount by which each event is shifted. pressBy(0.5) is the same as press, while pressBy(1/3) shifts each event by a third of its timespan.


stack(s("hh*4"),
      s("bd mt sd ht").pressBy("<0 0.5 0.25>")
     ).slow(2)
progNum
MIDI program number: Sends a MIDI program change message.


program : number | Pattern - MIDI program number (0-127)
note("c4").progNum(10).midichan(1).midi()
pure
A discrete value that repeats once per cycle.


pure('e4') // "e4"
pw
controls the pulsewidth of the pulse oscillator


pulsewidth : number | Pattern
note("{f a c e}%16").s("pulse").pw(".8:1:.2")
n(run(8)).scale("D:pentatonic").s("pulse").pw("0 .75 .5 1")
pwrate
controls the lfo rate for the pulsewidth of the pulse oscillator


rate : number | Pattern
n(run(8)).scale("D:pentatonic").s("pulse").pw("0.5").pwrate("<5 .1 25>").pwsweep("<0.3 .8>")
pwsweep
controls the lfo sweep for the pulsewidth of the pulse oscillator


sweep : number | Pattern
n(run(8)).scale("D:pentatonic").s("pulse").pw("0.5").pwrate("<5 .1 25>").pwsweep("<0.3 .8>")
queryArc
Query haps inside the given time span.


begin : Fraction | number - from time
end : Fraction | number - to time
const pattern = sequence('a', ['b', 'c'])
const haps = pattern.queryArc(0, 1)
console.log(haps)
silence
rand
A continuous pattern of random numbers, between 0 and 1.


// randomly change the cutoff
s("bd*4,hh*8").cutoff(rand.range(500,8000))
rand2
A continuous pattern of random numbers, between -1 and 1


range
Assumes a numerical pattern, containing unipolar values in the range 0 .. 1. Returns a new pattern with values scaled to the given min/max range. Most useful in combination with continuous patterns.


s("[bd sd]*2,hh*8")
.cutoff(sine.range(500,4000))
range2
Assumes a numerical pattern, containing bipolar values in the range -1 .. 1 Returns a new pattern with values scaled to the given min/max range.


s("[bd sd]*2,hh*8")
.cutoff(sine2.range2(500,4000))
rangex
Assumes a numerical pattern, containing unipolar values in the range 0 .. 1 Returns a new pattern with values scaled to the given min/max range, following an exponential curve.


s("[bd sd]*2,hh*8")
.cutoff(sine.rangex(500,4000))
rarely
Shorthand for .sometimesBy(0.25, fn)


s("hh*8").rarely(x=>x.speed("0.5"))
ratio
Allows dividing numbers via list notation using ":". Returns a new pattern with just numbers.


ratio("1, 5:4, 3:2").mul(110)
.freq().s("piano")
readInputs
Read next web audio block to input buffers


reallocateChannelsIfNeeded
Handles dynamic reallocation of input/output channels buffer (channel numbers may lety during lifecycle)


ref
exposes a custom value at query time. basically allows mutating state without evaluation


register
Registers a new pattern method. The method is added to the Pattern class + the standalone function is returned from register.


name : string - name of the function
func : function - function with 1 or more params, where last is the current pattern
release
Synonyms: rel

Amplitude envelope release time: The time it takes after the offset to go from sustain level to zero.


time : number | Pattern - release time in seconds
note("c3 e3 g3 c4").release("<0 .1 .4 .6 1>/2")
removeUndefineds
Returns a new pattern, with haps containing undefined values removed from query results.


repeatCycles
Repeats each cycle the given number of times.


note(irand(12).add(34)).segment(4).repeatCycles(2).s("gm_acoustic_guitar_nylon")
reset
Resets the pattern to the start of the cycle for each onset of the reset pattern.


s("[<bd lt> sd]*2, hh*8").reset("<x@3 x(5,8)>")
restart
Restarts the pattern for each onset of the restart pattern. While reset will only reset the current cycle, restart will start from cycle 0.


s("[<bd lt> sd]*2, hh*8").restart("<x@3 x(5,8)>")
rev
Reverse all haps in a pattern


note("c d e g").rev()
ribbon
Loops the pattern inside an offset for cycles. If you think of the entire span of time in cycles as a ribbon, you can cut a single piece and loop it.


offset : number - start point of loop in cycles
cycles : number - loop length in cycles
note("<c d e f>").ribbon(1, 2)
// Looping a portion of randomness
n(irand(8).segment(4)).scale("c:pentatonic").ribbon(1337, 2)
// rhythm generator
s("bd!16?").ribbon(29,.5)
room
Sets the level of reverb.

When using mininotation, you can also optionally add the 'size' parameter, separated by ':'.


level : number | Pattern - between 0 and 1
s("bd sd [~ bd] sd").room("<0 .2 .4 .6 .8 1>")
s("bd sd [~ bd] sd").room("<0.9:1 0.9:4>")
roomdim
Synonyms: rdim

Reverb lowpass frequency at -60dB (in hertz). When this property is changed, the reverb will be recaculated, so only change this sparsely..


frequency : number - between 0 and 20000hz
s("bd sd [~ bd] sd").room(0.5).rlp(10000).rdim(8000)
s("bd sd [~ bd] sd").room(0.5).rlp(5000).rdim(400)
roomfade
Synonyms: rfade

Reverb fade time (in seconds). When this property is changed, the reverb will be recaculated, so only change this sparsely..


seconds : number - for the reverb to fade
s("bd sd [~ bd] sd").room(0.5).rlp(10000).rfade(0.5)
s("bd sd [~ bd] sd").room(0.5).rlp(5000).rfade(4)
roomlp
Synonyms: rlp

Reverb lowpass starting frequency (in hertz). When this property is changed, the reverb will be recaculated, so only change this sparsely..


frequency : number - between 0 and 20000hz
s("bd sd [~ bd] sd").room(0.5).rlp(10000)
s("bd sd [~ bd] sd").room(0.5).rlp(5000)
roomsize
Synonyms: rsize, sz, size

Sets the room size of the reverb, see room. When this property is changed, the reverb will be recaculated, so only change this sparsely..


size : number | Pattern - between 0 and 10
s("bd sd [~ bd] sd").room(.8).rsize(1)
s("bd sd [~ bd] sd").room(.8).rsize(4)
rootNotes
Maps the chords of the incoming pattern to root notes in the given octave.


octave : octave - octave to use
"<C^7 A7 Dm7 G7>".rootNotes(2).note()
rotationAlpha
Synonyms: rotA, rotZ, rotationZ

The device's rotation around the alpha-axis value ranges from 0 to 1.


n(rotationAlpha.segment(4).range(0,7)).scale("C:minor")
rotationBeta
Synonyms: rotB, rotX, rotationX

The device's rotation around the beta-axis value ranges from 0 to 1.


n(rotationBeta.segment(4).range(0,7)).scale("C:minor")
rotationGamma
Synonyms: rotG, rotY, rotationY

The device's rotation around the gamma-axis value ranges from 0 to 1.


n(rotationGamma.segment(4).range(0,7)).scale("C:minor")
round
Assumes a numerical pattern. Returns a new pattern with all values rounded to the nearest integer.


n("0.5 1.5 2.5".round()).scale("C:major")
run
A discrete pattern of numbers from 0 to n-1


n(run(4)).scale("C4:pentatonic")
// n("0 1 2 3").scale("C4:pentatonic")
s
Synonyms: sound

Select a sound / sample by name. When using mininotation, you can also optionally supply 'n' and 'gain' parameters separated by ':'.


sound : string | Pattern - The sound / pattern of sounds to pick
s("bd hh")
s("bd:0 bd:1 bd:0:0.3 bd:1:1.4")
samples
Loads a collection of samples to use with s


samples('github:tidalcycles/dirt-samples');
s("[bd ~]*2, [~ hh]*2, ~ sd")
samples({
 bd: '808bd/BD0000.WAV',
 sd: '808sd/SD0010.WAV'
 }, 'https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/');
s("[bd ~]*2, [~ hh]*2, ~ sd")
samples('shabda:noise,chimp:2')
s("noise <chimp:0*2 chimp:1>")
samples('shabda/speech/fr-FR/f:chocolat')
s("chocolat*4")
saw
A sawtooth signal between 0 and 1.


note("<c3 [eb3,g3] g2 [g3,bb3]>*8")
.clip(saw.slow(2))
n(saw.range(0,8).segment(8))
.scale('C major')
saw2
A sawtooth signal between -1 and 1 (like saw, but bipolar).


scale
Turns numbers into notes in the scale (zero indexed). Also sets scale for other scale operations, like {@link Pattern#scaleTranspose}.

A scale consists of a root note (e.g. c4, c, f#, bb4) followed by semicolon (':') and then a scale type.

The root note defaults to octave 3, if no octave number is given.


scale : string - Name of scale
n("0 2 4 6 4 2").scale("C:major")
n("[0,7] 4 [2,7] 4")
.scale("C:<major minor>/2")
.s("piano")
n(rand.range(0,12).segment(8))
.scale("C:ritusen")
.s("piano")
scaleTranspose
Transposes notes inside the scale by the number of steps. Expected to be called on a Pattern which already has a {@link Pattern#scale}


offset : offset - number of steps inside the scale
"-8 [2,4,6]"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>")
.note()
scope
Synonyms: tscope

Renders an oscilloscope for the time domain of the audio signal.


config : object - optional config with options:
align : boolean - if 1, the scope will be aligned to the first zero crossing. defaults to 1
color : string - line color as hex or color name. defaults to white.
thickness : number - line thickness. defaults to 3
scale : number - scales the y-axis. Defaults to 0.25
pos : number - y-position relative to screen height. 0 = top, 1 = bottom of screen
trigger : number - amplitude value that is used to align the scope. defaults to 0.
s("sawtooth")._scope()
scramble
Slices a pattern into the given number of parts, then plays those parts at random. Similar to shuffle, but parts might be played more than once, or not at all, per cycle.


note("c d e f").sound("piano").scramble(4)
note("c d e f".scramble(4), "g").sound("piano")
scrub
Allows you to scrub an audio file like a tape loop by passing values that represents the position in the audio file in the optional array syntax ex: "0.5:2", the second value controls the speed of playback


samples('github:switchangel/pad')
s("swpad:0").scrub("{0.1!2 .25@3 0.7!2 <0.8:1.5>}%8")
samples('github:yaxu/clean-breaks/main');
s("amen/4").fit().scrub("{0@3 0@2 4@3}%8".div(16))
segment
Synonyms: seg

Samples the pattern at a rate of n events per cycle. Useful for turning a continuous pattern into a discrete one.


segments : number - number of segments per cycle
note(saw.range(40,52).segment(24))
seq
Synonyms: sequence, fastcat

Like cat, but the items are crammed into one cycle.


seq("e5", "b4", ["d5", "c5"]).note()
// "e5 b4 [d5 c5]".note()
// As a chained function:
s("hh*4").seq(
  note("c4(5,8)")
)
seqPLoop
Similarly to arrange, allows you to arrange multiple patterns together over multiple cycles. Unlike arrange, you specify a start and stop time for each pattern rather than duration, which means that patterns can overlap.


seqPLoop([0, 2, "bd(3,8)"],
         [1, 3, "cp(3,8)"]
        )
  .sound()
sequence
See fastcat


sequenceP
Takes a list of patterns, and returns a pattern of lists.


setContext
Returns a new pattern with the context field set to every hap set to the given value.


context : *
setcpm
Changes the global tempo to the given cycles per minute


cpm : number - cycles per minute
setcpm(140/4) // =140 bpm in 4/4
$: s("bd*4,[- sd]*2").bank('tr707')
shape
(Deprecated) Wave shaping distortion. WARNING: can suddenly get unpredictably loud. Please use distort instead, which has a more predictable response curve second option in optional array syntax (ex: ".9:.5") applies a postgain to the output


distortion : number | Pattern - between 0 and 1
s("bd sd [~ bd] sd,hh*8").shape("<0 .2 .4 .6 .8>")
shiftInputBuffers
Shift left content of input buffers to receive new web audio block


shiftOutputBuffers
Shift left content of output buffers to receive new web audio block


shiftPeaks
Shift peaks and regions of influence by pitchFactor into new specturm


showFirstCycle
More human-readable version of the firstCycleValues accessor.


shrink
Experimental

Progressively shrinks the pattern by 'n' steps until there's nothing left, or if a second value is given (using mininotation list syntax with :), that number of times. A positive number will progressively drop steps from the start of a pattern, and a negative number from the end.


"tha dhi thom nam".shrink("1").sound()
.bank("mridangam")
"tha dhi thom nam".shrink("-1").sound()
.bank("mridangam")
"tha dhi thom nam".shrink("1 -1").sound().bank("mridangam").pace(4)
note("0 1 2 3 4 5 6 7".scale("C:ritusen")).sound("folkharp")
   .shrink("1 -1").pace(8)
shuffle
Slices a pattern into the given number of parts, then plays those parts in random order. Each part will be played exactly once per cycle.


note("c d e f").sound("piano").shuffle(4)
note("c d e f".shuffle(4), "g").sound("piano")
silence
Does absolutely nothing..


silence // "~"
sine
A sine signal between 0 and 1.


n(sine.segment(16).range(0,15))
.scale("C:minor")
sine2
A sine signal between -1 and 1 (like sine, but bipolar).


slice
Chops samples into the given number of slices, triggering those slices with a given pattern of slice numbers. Instead of a number, it also accepts a list of numbers from 0 to 1 to slice at specific points.


samples('github:tidalcycles/dirt-samples')
s("breaks165").slice(8, "0 1 <2 2*2> 3 [4 0] 5 6 7".every(3, rev)).slow(0.75)
samples('github:tidalcycles/dirt-samples')
s("breaks125").fit().slice([0,.25,.5,.75], "0 1 1 <2 3>")
slider
Displays a slider widget to allow the user manipulate a value


value : number - Initial value
min : number - Minimum value - optional, defaults to 0
max : number - Maximum value - optional, defaults to 1
step : number - Step size - optional
slow
Synonyms: sparsity

Slow down a pattern over the given number of cycles. Like the "/" operator in mini notation.


factor : number | Pattern - slow down factor
s("bd hh sd hh").slow(2) // s("[bd hh sd hh]/2")
slowcat
Concatenation: combines a list of patterns, switching between them successively, one per cycle:

synonyms: cat


slowcat("e5", "b4", ["d5", "c5"])
slowcatPrime
Concatenation: combines a list of patterns, switching between them successively, one per cycle. Unlike slowcat, this version will skip cycles.


items : any - The items to concatenate
someCycles
Shorthand for .someCyclesBy(0.5, fn)


s("bd,hh*8").someCycles(x=>x.speed("0.5"))
someCyclesBy
Randomly applies the given function by the given probability on a cycle by cycle basis. Similar to sometimesBy


probability : number | Pattern - a number between 0 and 1
function : function - the transformation to apply
s("bd,hh*8").someCyclesBy(.3, x=>x.speed("0.5"))
sometimes
Applies the given function with a 50% chance


function : function - the transformation to apply
s("hh*8").sometimes(x=>x.speed("0.5"))
sometimesBy
Randomly applies the given function by the given probability. Similar to someCyclesBy


probability : number | Pattern - a number between 0 and 1
function : function - the transformation to apply
s("hh*8").sometimesBy(.4, x=>x.speed("0.5"))
sortHapsByPart
Returns a new pattern, which returns haps sorted in temporal order. Mainly of use when comparing two patterns for equality, in tests.


source
Synonyms: src

Define a custom webaudio node to use as a sound source.


getSource : function
spectrum
Renders a spectrum analyzer for the incoming audio signal.


config : object - optional config with options:
thickness : integer - line thickness in px (default 3)
speed : integer - scroll speed (default 1)
min : integer - min db (default -80)
max : integer - max db (default 0)
n("<0 4 <2 3> 1>*3")
.off(1/8, add(n(5)))
.off(1/5, add(n(7)))
.scale("d3:minor:pentatonic")
.s('sine')
.dec(.3).room(.5)
._spectrum()
speed
Changes the speed of sample playback, i.e. a cheap way of changing pitch.


speed : number | Pattern - inf to inf, negative numbers play the sample backwards.
s("bd*6").speed("1 2 4 1 -2 -4")
speed("1 1.5*2 [2 1.1]").s("piano").clip(1)
spiral
Displays a spiral visual.


options : Object - Object containing all the optional following parameters as key value pairs:
stretch : number - controls the rotations per cycle ratio, where 1 = 1 cycle / 360 degrees
size : number - the diameter of the spiral
thickness : number - line thickness
cap : string - style of line ends: butt (default), round, square
inset : string - number of rotations before spiral starts (default 3)
playheadColor : string - color of playhead, defaults to white
playheadLength : number - length of playhead in rotations, defaults to 0.02
playheadThickness : number - thickness of playheadrotations, defaults to thickness
padding : number - space around spiral
steady : number - steadyness of spiral vs playhead. 1 = spiral doesn't move, playhead does.
activeColor : number - color of active segment. defaults to foreground of theme
inactiveColor : number - color of inactive segments. defaults to gutterForeground of theme
colorizeInactive : boolean - wether or not to colorize inactive segments, defaults to 0
fade : boolean - wether or not past and future should fade out. defaults to 1
logSpiral : boolean - wether or not the spiral should be logarithmic. defaults to 0
note("c2 a2 eb2")
.euclid(5,8)
.s('sawtooth')
.lpenv(4).lpf(300)
._spiral({ steady: .96 })
splice
Works the same as slice, but changes the playback speed of each slice to match the duration of its step.


samples('github:tidalcycles/dirt-samples')
s("breaks165")
.splice(8,  "0 1 [2 3 0]@2 3 0@2 7")
splitQueries
Returns a new pattern, with queries split at cycle boundaries. This makes some calculations easier to express, as all haps are then constrained to happen within a cycle.


spread
Set the stereo pan spread for supported oscillators


spread : number | Pattern - between 0 and 1
note("d f a a# a d3").fast(2).s("supersaw").spread("<0 .3 1>")
square
A square signal between 0 and 1.


n(square.segment(4).range(0,7)).scale("C:minor")
square2
A square signal between -1 and 1 (like square, but bipolar).


squeeze
Pick from the list of values (or patterns of values) via the index using the given pattern of integers. The selected pattern will be compressed to fit the duration of the selecting event


pat : Pattern
xs : *
note(squeeze("<0@2 [1!2] 2>", ["g a", "f g f g" , "g a c d"]))
squiz
Made by Calum Gunn. Reminiscent of some weird mixture of filter, ring-modulator and pitch-shifter. The SuperCollider manual defines Squiz as:

"A simplistic pitch-raising algorithm. It's not meant to sound natural; its sound is reminiscent of some weird mixture of filter, ring-modulator and pitch-shifter, depending on the input. The algorithm works by cutting the signal into fragments (delimited by upwards-going zero-crossings) and squeezing those fragments in the time domain (i.e. simply playing them back faster than they came in), leaving silences inbetween. All the parameters apart from memlen can be modulated."


squiz : number | Pattern - Try passing multiples of 2 to it - 2, 4, 8 etc.
squiz("2 4/2 6 [8 16]").s("bd").osc()
stack
Synonyms: polyrhythm, pr

The given items are played at the same time at the same length.


stack("g3", "b3", ["e4", "d4"]).note()
// "g3,b3,[e4,d4]".note()
// As a chained function:
s("hh*4").stack(
  note("c4(5,8)")
)
stepalt
Experimental

Concatenates patterns stepwise, according to an inferred 'steps per cycle'. Similar to stepcat, but if an argument is a list, the whole pattern will alternate between the elements in the list.


stepalt(["bd cp", "mt"], "bd").sound()
// The same as "bd cp bd mt bd".sound()
stepcat
Synonyms: timeCat, timecat

'Concatenates' patterns like fastcat, but proportional to a number of steps per cycle. The steps can either be inferred from the pattern, or provided as a [length, pattern] pair. Has the alias timecat.


stepcat([3,"e3"],[1, "g3"]).note()
// the same as "e3@3 g3".note()
stepcat("bd sd cp","hh hh").sound()
// the same as "bd sd cp hh hh".sound()
stretch
Changes the speed of sample playback, i.e. a cheap way of changing pitch.


factor : number | Pattern - inf to inf, negative numbers play the sample backwards.
s("gm_flute").stretch("1 2 .5")
striate
Cuts each sample into the given number of parts, triggering progressive portions of each sample at each loop.


s("numbers:0 numbers:1 numbers:2").striate(6).slow(3)
stripContext
Returns a new pattern with the context field of every hap set to an empty object.


struct
Applies the given structure to the pattern:


note("c,eb,g")
  .struct("x ~ x ~ ~ x ~ x ~ ~ ~ x ~ x ~ ~")
  .slow(2)
stut
Deprecated. Like echo, but the last 2 parameters are flipped.


times : number - how many times to repeat
feedback : number - velocity multiplicator for each iteration
time : number - cycle offset between iterations
s("bd sd").stut(3, .8, 1/6)
sub
Like add, but the given numbers are subtracted.


n("0 2 4".sub("<0 1 2 3>")).scale("C4:minor")
// See add for more information.
superimpose
Superimposes the result of the given function(s) on top of the original pattern:


"<0 2 4 6 ~ 4 ~ 2 0!3 ~!5>*8"
  .superimpose(x=>x.add(2))
  .scale('C minor').note()
sustain
Synonyms: sus

Amplitude envelope sustain level: The level which is reached after attack / decay, being sustained until the offset.


gain : number | Pattern - sustain level between 0 and 1
note("c3 e3 f3 g3").decay(.2).sustain("<0 .1 .4 .6 1>")
swing
Shorthand for swingBy with 1/3:


subdivision : number
s("hh*8").swing(4)
// s("hh*8").swingBy(1/3, 4)
swingBy
The function swingBy x n breaks each cycle into n slices, and then delays events in the second half of each slice by the amount x, which is relative to the size of the (half) slice. So if x is 0 it does nothing, 0.5 delays for half the note duration, and 1 will wrap around to doing nothing again. The end result is a shuffle or swing-like rhythm


subdivision : number
offset : number
s("hh*8").swingBy(1/3, 4)
sysex
MIDI sysex: Sends a MIDI sysex message.


id : number | Pattern - Sysex ID
data : number | Pattern - Sysex data
note("c4").sysex(["0x77", "0x01:0x02:0x03:0x04"]).midichan(1).midi()
sysexdata
MIDI sysex data: Sends a MIDI sysex message.


data : number | Pattern - Sysex data
note("c4").sysexid("0x77").sysexdata("0x01:0x02:0x03:0x04").midichan(1).midi()
sysexid
MIDI sysex ID: Sends a MIDI sysex identifier message.


id : number | Pattern - Sysex ID
note("c4").sysexid("0x77").sysexdata("0x01:0x02:0x03:0x04").midichan(1).midi()
tag
Tags each Hap with an identifier. Good for filtering. The function populates Hap.context.tags (Array).


tag : string - anything unique
take
Experimental

Takes the given number of steps from a pattern (dropping the rest). A positive number will take steps from the start of a pattern, and a negative number from the end.


"bd cp ht mt".take("2").sound()
// The same as "bd cp".sound()
"bd cp ht mt".take("1 2 3").sound()
// The same as "bd bd cp bd cp ht".sound()
"bd cp ht mt".take("-1 -2 -3").sound()
// The same as "mt ht mt cp ht mt".sound()
time
A signal representing the cycle time.


timecat
Aliases for stepcat


toBipolar
Assumes a numerical pattern, containing unipolar values in the range 0 ..

Returns a new pattern with values scaled to the bipolar range -1 .. 1

tour
Experimental

Inserts a pattern into a list of patterns. On the first repetition it will be inserted at the end of the list, then moved backwards through the list on successive repetitions. The patterns are added together stepwise, with all repetitions taking place over a single cycle. Using pace to set the number of steps per cycle is therefore usually recommended.


"[c g]".tour("e f", "e f g", "g f e c").note()
   .sound("folkharp")
   .pace(8)
transpose
Change the pitch of each value by the given amount. Expects numbers or note strings as values. The amount can be given as a number of semitones or as a string in interval short notation. If you don't care about enharmonic correctness, just use numbers. Otherwise, pass the interval of the form: ST where S is the degree number and T the type of interval with

M = major
m = minor
P = perfect
A = augmented
d = diminished
Examples intervals:

1P = unison
3M = major third
3m = minor third
4P = perfect fourth
4A = augmented fourth
5P = perfect fifth
5d = diminished fifth

amount : string | number - Either number of semitones or interval string.
"c2 c3".fast(2).transpose("<0 -2 5 3>".slow(2)).note()
"c2 c3".fast(2).transpose("<1P -2M 4P 3m>".slow(2)).note()
tri
A triangle signal between 0 and 1.


n(tri.segment(8).range(0,7)).scale("C:minor")
tri2
A triangle signal between -1 and 1 (like tri, but bipolar).


undegrade
Inverse of degrade: Randomly removes 50% of events from the pattern. Shorthand for .undegradeBy(0.5) Events that would be removed by degrade are let through by undegrade and vice versa (see second example).


s("hh*8").undegrade()
s("hh*10").layer(
  x => x.degrade().pan(0),
  x => x.undegrade().pan(1)
)
undegradeBy
Inverse of degradeBy: Randomly removes events from the pattern by a given amount. 0 = 100% chance of removal 1 = 0% chance of removal Events that would be removed by degradeBy are let through by undegradeBy and vice versa (see second example).


amount : number - a number between 0 and 1
s("hh*8").undegradeBy(0.2)
s("hh*10").layer(
  x => x.degradeBy(0.2).pan(0),
  x => x.undegradeBy(0.8).pan(1)
)
unison
Set number of stacked voices for supported oscillators


numvoices : number | Pattern
note("d f a a# a d3").fast(2).s("supersaw").unison("<1 2 7>")
unit
Used in conjunction with speed, accepts values of "r" (rate, default behavior), "c" (cycles), or "s" (seconds). Using unit "c" means speed will be interpreted in units of cycles, e.g. speed "1" means samples will be stretched to fill a cycle. Using unit "s" means the playback speed will be adjusted so that the duration is the number of seconds specified by speed.


unit : number | string | Pattern - see description above
speed("1 2 .5 3").s("bd").unit("c").osc()
velocity
Sets the velocity from 0 to 1. Is multiplied together with gain.


s("hh*8")
.gain(".4!2 1 .4!2 1 .4 1")
.velocity(".4 1")
vib
Synonyms: vibrato, v

Applies a vibrato to the frequency of the oscillator.


frequency : number | Pattern - of the vibrato in hertz
note("a e")
.vib("<.5 1 2 4 8 16>")
._scope()
// change the modulation depth with ":"
note("a e")
.vib("<.5 1 2 4 8 16>:12")
._scope()
vibmod
Synonyms: vmod

Sets the vibrato depth in semitones. Only has an effect if vibrato | vib | v is is also set


depth : number | Pattern - of vibrato (in semitones)
note("a e").vib(4)
.vibmod("<.25 .5 1 2 12>")
._scope()
// change the vibrato frequency with ":"
note("a e")
.vibmod("<.25 .5 1 2 12>:8")
._scope()
voicing
Turns chord symbols into voicings. You can use the following control params:

chord: Note, followed by chord symbol, e.g. C Am G7 Bb^7
dict: voicing dictionary to use, falls back to default dictionary
anchor: the note that is used to align the chord
mode: how the voicing is aligned to the anchor
below: top note <= anchor
duck: top note <= anchor, anchor excluded
above: bottom note >= anchor
offset: whole number that shifts the voicing up or down to the next voicing
n: if set, the voicing is played like a scale. Overshooting numbers will be octaved
All of the above controls are optional, except chord. If you pass a pattern of strings to voicing, they will be interpreted as chords.


n("0 1 2 3").chord("<C Am F G>").voicing()
voicings
DEPRECATED: still works, but it is recommended you use .voicing instead (without s). Turns chord symbols into voicings, using the smoothest voice leading possible. Uses chord-voicings package.


dictionary : string - which voicing dictionary to use.
stack("<C^7 A7 Dm7 G7>".voicings('lefthand'), "<C3 A2 D3 G2>").note()
vowel
Formant filter to make things sound like vowels.


vowel : string | Pattern - You can use a e i o u ae aa oe ue y uh un en an on, corresponding to [a] [e] [i] [o] [u] [æ] [ɑ] [ø] [y] [ɯ] [ʌ] [œ̃] [ɛ̃] [ɑ̃] [ɔ̃]. Aliases: aa = å = ɑ, oe = ø = ö, y = ı, ae = æ.
note("[c2 <eb2 <g2 g1>>]*2").s('sawtooth')
.vowel("<a e i <o u>>")
s("bd sd mt ht bd [~ cp] ht lt").vowel("[a|e|i|o|u]")
wchoose
Chooses randomly from the given list of elements by giving a probability to each element


pairs : any - arrays of value and weight
note("c2 g2!2 d2 f1").s(wchoose(["sine",10], ["triangle",1], ["bd:6",1]))
wchooseCycles
Synonyms: wrandcat

Picks one of the elements at random each cycle by giving a probability to each element


wchooseCycles(["bd",10], ["hh",1], ["sd",1]).s().fast(8)
wchooseCycles(["bd bd bd",5], ["hh hh hh",3], ["sd sd sd",1]).fast(4).s()
// The probability can itself be a pattern
wchooseCycles(["bd(3,8)","<5 0>"], ["hh hh hh",3]).fast(4).s()
when
Applies the given function whenever the given pattern is in a true state.


binary_pat : Pattern
func : function
"c3 eb3 g3".when("<0 1>/2", x=>x.sub("5")).note()
whenKey
Do something on a keypress, or array of keypresses Key name reference


s("bd(5,8)").whenKey("Control:j", x => x.segment(16).color("red")).whenKey("Control:i", x => x.fast(2).color("blue"))
withContext
Returns a new pattern with the given function applied to the context field of every hap.


func : function
withHap
As with withHaps, but applies the function to every hap, rather than every list of haps.


func : function
withHaps
Returns a new pattern with the given function applied to the list of haps returned by every query.


func : function
withHapSpan
Similar to withQuerySpan, but the function is applied to the timespans of all haps returned by pattern queries (both part timespans, and where present, whole timespans).


func : function
withHapTime
As with withHapSpan, but the function is applied to both the begin and end time of the hap timespans.


func : function - the function to apply
within
Use within to apply a function to only a part of a pattern.


start : number - start within cycle (0 - 1)
end : number - end within cycle (0 - 1). Must be > start
func : function - function to be applied to the sub-pattern
withLoc
Returns a new pattern with the given location information added to the context of every hap.


start : Number - start offset
end : Number - end offset
withQuerySpan
Returns a new pattern, where the given function is applied to the query timespan before passing it to the original pattern.


func : function - the function to apply
withQueryTime
As with withQuerySpan, but the function is applied to both the begin and end time of the query timespan.


func : function - the function to apply
withValue
Synonyms: fmap

Returns a new pattern, with the function applied to the value of each hap. It has the alias fmap.


func : function - to to apply to the value
"0 1 2".withValue(v => v + 10).log()
wordfall
Displays a vertical pianoroll with event labels. Supports all the same options as pianoroll.


writeOutputs
Write next web audio block from output buffers


xfade
Cross-fades between left and right from 0 to 1:

0 = (full left, no right)
.5 = (both equal)
1 = (no left, full right)

xfade(s("bd*2"), "<0 .25 .5 .75 1>", s("hh*8"))
zip
Experimental

'zips' together the steps of the provided patterns. This can create a long repetition, taking place over a single, dense cycle. Using pace to set the number of steps per cycle is therefore usually recommended.


zip("e f", "e f g", "g [f e] a f4 c").note()
   .sound("folkharp")
   .pace(8)
zoom
Plays a portion of a pattern, specified by the beginning and end of a time span. The new resulting pattern is played over the time period of the original pattern:


s("bd*2 hh*3 [sd bd]*2 perc").zoom(0.25, 0.75)
// s("hh*3 [sd bd]*2") // equivalent
