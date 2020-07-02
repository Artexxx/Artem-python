# nfriction

a tool for viewing items from your massive collection of pornographic manga at
random

## features

- can scan a library of thousands of mangas in less than a second
- handles mangas saved as directories full of images, or as .rar/cbr or
  .zip/cbz archives
- support for keyboard shortcuts and touch devices via [photoswipe]
- in-browser rotation, just in case you're lying down and using a widescreen
  laptop
- quick filtering, just in case you're in the mood for something specific
- right-to-left layout, just in case you're a weeb nerd

## requirements

- python 3.5 or newer (`os.scandir` is just too good)
- unrar, which is probably available from your package manager as `unrar`
- libjpeg and zlib (so that we can run [PIL][pil] and determine image
  resolutions)
- a directory full of porn manga (more details in [library
  format](#library-format) below)

### optional extras:

- magic (for improving archive file type detection), probably `magic` or
  `libmagic` in your package manager

[pil]: http://pillow.readthedocs.io/en/3.0.x/installation.html

## setup

```
pip3 install nfriction
```

or, to upgrade from an older version:

```
pip3 install -U nfriction
```

## use

```

>>> cd 'home/user/Sexual-Girls'  # or wherever your porn is
>>> nfriction
```

then open <http://localhost:5000/> in your browser of choice

for quick navigation between pages, you can swipe if you're on a touchscreen
device, or you can use your arrow keys

when you want something new, hit enter or swipe vertically and it'll pick
another thing for you

if you do this accidentally, just hit back in your browser and you'll go back
to the thing you were looking at before

if you have something in particular in mind, press o or tap/click at the bottom
left of the screen and you'll get a menu with a field you can type into to
filter what the choices are being made from. the filtering is pretty basic, it
just checks to see if your query is present in the file's path. it's case
insensitive. on a computer with a keyboard, the intended workflow to change
your filter is to hit o, type something, and hit enter

the form that the filter field lives in also has rotation options, for if
you're using a computer with an inappropriate aspect ratio or you're lying down
or whatever

## caveats

### library format

your library can be structured and nested however you like, but nfriction has a
particular idea of what counts as a single manga, inspired by what i've
encountered in batches of scans i've seen

basically, one manga is either a flat directory containing images or a
zip/rar/cbz/cbr archive containing images in any structure

this precludes, for instance, archives that contain other archives, as i've not
seen anyone distributing scans in such a format with any regularity

if you have a library that's formatted differently and would like nfriction to
support it, please let me know

### fullscreen

nfriction doesn't use photoswipe's built-in fullscreen support, primarily
because it'd break every time you reloaded the page, and that'd be awful

your browser probably has an option to go fullscreen and hide the UI
completely; i know at least that desktop chrome and safari do
