# Using Strudel Offline

You can use Strudel even without a network! When you first visit the [Strudel REPL](https://strudel.cc/),
your browser will download the whole web app including documentation.
When the download is finished (&lt;1MB), you can visit the website even when offline,
getting the downloaded website instead of the online one.

When the site gets updated, your browser will download that update on the next online visit.
When an update is available, the site will refresh after the download is finished.

This works because Strudel is implemented as progessive web app (using [Vite PWA](https://vite-pwa-org.netlify.app/)).

## Samples

While the browser will download the app itself, samples are only downloaded when you're actively using them.
So to make sure a specific set of samples is available when offline, just use them.
Also, only samples from these domains will be cached for offline use:

- `https://raw.githubusercontent.com/*` for samples uploaded to github
- `https://freesound.org/*` / `https://cdn.freesound.org/*` for freesound
- `https://shabda.ndre.gr/.*` for shabda

## Inspecting / Clearing Cache

You can view all cached files in your browser.

### Firefox

- Open the Developer Tools (`Tools > Web Developer > Web Developer Tools`)
- go to `Storage` tab and expand `Cache Storage > https://strudel.cc`.
- or go to the `Application` tab and view the latest updates in `Service Workers`

### Chromium based Browsers

- Open Developer Tools (`Right Click > Inspect`)
- go to the `Application` tab
- view downloaded files under `Cache > Cache Storage`
- view the latest updates in `Service Workers`

## Strudel Standalone App

You can also install Strudel as a standalone app on most devices.
A standalone app has its own desktop / homescreen icon and launches in a separate window,
without the browser ui.

<figure>
  ![Strudel on MacOS](/pwa/strudel-macos.png)
  <figcaption>Strudel on MacOS</figcaption>
</figure>

### Desktop

With a chromium based browser:

1. go to the [Strudel REPL](https://strudel.cc).
2. on the right of the adress bar, click `install Strudel REPL`
3. the REPL should now run as a standalone chromium app

Without a chromium based browser, you can use [nativefier](https://github.com/nativefier/nativefier) to generate a desktop app:

1. make sure you have NodeJS installed
2. run `npx nativefier strudel.cc`

<figure>
  ![Strudel on Linux](/pwa/strudel-linux.png)
  <figcaption>Strudel on Linux</figcaption>
</figure>

### iOS

1. open to the [Strudel REPL](https://strudel.cc/) in safari
2. press the share icon and tab `Add to homescreen`
3. You should now have a strudel app icon that opens the repl in full screen

### Android

1. open to the [Strudel REPL](https://strudel.cc/)
2. Tab the install button at the bottom

Ok, what are [Patterns](/technical-manual/patterns) all about?