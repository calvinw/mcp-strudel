# Using Hydra inside Strudel

You can write [hydra](https://hydra.ojack.xyz/) code in strudel! All you have to do is to call `await initHydra()` at the top:

```javascript
await initHydra()
// licensed with CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/
// by Zach Krall
// http://zachkrall.online/

osc(10, 0.9, 300)
.color(0.9, 0.7, 0.8)
.diff(
osc(45, 0.3, 100)
.color(0.9, 0.9, 0.9)
.rotate(0.18)
.pixelate(12)
.kaleid()
)
.scrollX(10)
.colorama()
.luma()
.repeatX(4)
.repeatY(4)
.modulate(
osc(1, -0.9, 300)
)
.scale(2)
.out()

note("[a,c,e,<a4 ab4 g4 gb4>,b4]/2")
.s("sawtooth").vib(2)
.lpf(600).lpa(2).lpenv(6)

```

## H patterns

There is a special function `H` that allows you to use a pattern as an input to hydra:



## detectAudio

To use hydra audio capture, call `initHydra` with `{detectAudio:true}` configuration param:

```javascript
await initHydra({detectAudio:true})
let pattern = "<3 4 5 [6 7]*2>"
shape(H(pattern)).repeat()
  .scrollY(
    ()=> a.fft[0]*.25
  )
  .add(src(o0).color(.71 ).scrollX(.005),.95)
.out(o0)
n(pattern).scale("A:minor").piano().room(1)

```

You might now be able to see this properly here: [open in REPL](/#YXdhaXQgaW5pdEh5ZHJhKCkKbGV0IHBhdHRlcm4gPSAiMyA0IDUgWzYgN10qMiIKc2hhcGUoSChwYXR0ZXJuKSkub3V0KG8wKQpuKHBhdHRlcm4pLnNjYWxlKCJBOm1pbm9yIikucGlhbm8oKS5yb29tKDEpIA%3D%3D)

Similar to `detectAudio`, all the [available hydra options](https://github.com/hydra-synth/hydra-synth#api) can be passed to `initHydra`.

## feedStrudel

Using the `feedStrudel` option, you can transform strudel visualizations with hydra:

```javascript
await initHydra({feedStrudel:1})
//
src(s0).kaleid(H("<4 5 6>"))
  .diff(osc(1,0.5,5))
  .modulateScale(osc(2,-0.25,1))
  .out()
//

$: s("bd*4,[hh:0:<.5 1>]*8,~ rim").bank("RolandTR909").speed(.9)

$: note("[<g1!3 <bb1 <f1 d1>>>]\*3").s("sawtooth")

.room(.75).sometimes(add(note(12))).clip(.3)
.lpa(.05).lpenv(-4).lpf(2000).lpq(8).ftype('24db')

all(x=>x.fft(4).scope({pos:0,smear:.95}))
```