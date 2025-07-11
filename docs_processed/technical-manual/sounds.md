# Sounds

Let's take a closer look about how sounds are implemented in the webaudio output.

## Registering a sound

All sounds are registered in the sound map, using the the `registerSound` function:

```ts
function registerSound(
  name: string, // The name of the sound that should be given to `s`, e.g. `mysaw`
  // The function called by the scheduler to trigger the sound:
  (
    time: number, // The audio context time the sound should start
    value: object, // The value of the `Hap`
    onended: () => void // A callback that should be fired when the sound has ended
  ) => {
    node: AudioNode, // node to connect to rest of the effects chain
    stop: (time:number) => void // a function that will stop the sound
  },
  data: object // meta data, only for ui logic in sounds tab
);
```

When `registerSound` is called, it registers `{ onTrigger, data }` under the given `name` in a [nanostore map](https://github.com/nanostores/nanostores#maps).

### Example

This might be a bit abstract, so here is a minimal example:

```js
registerSound(
  'mysaw',
  (time, value, onended) => {
    let { freq } = value; // destructure control params
    const ctx = getAudioContext();
    // create oscillator
    const o = new OscillatorNode(ctx, { type: 'sawtooth', frequency: Number(freq) });
    o.start(time);
    // add gain node to level down osc
    const g = new GainNode(ctx, { gain: 0.3 });
    // connect osc to gain
    const node = o.connect(g);
    // this function can be called from outside to stop the sound
    const stop = (time) => o.stop(time);
    // ended will be fired when stop has been fired
    o.addEventListener('ended', () => {
      o.disconnect();
      g.disconnect();
      onended();
    });
    return { node, stop };
  },
  { type: 'synth' },
);
// use the sound
freq(220, 440, 330).s('mysaw');
```

You can actually use this code in the [REPL](https://strudel.cc/) and it'll work.
After evaluating the code, you should see `mysaw` in listed in the sounds tab.

## Playing sounds

Now here is what happens when a sound is played:
When the webaudio output plays a `Hap`, it will lookup and call the `onTrigger` function for the given `s`.
The returned `node` can then be connected to the rest of the standard effects chain
Having the stop function separate allows playing sounds via midi too, where you don't know how long the noteon will last