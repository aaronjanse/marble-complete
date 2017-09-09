A fork of AsciiDots based on turing-complete marble runs

Inspired by:
https://nbickford.wordpress.com/2014/03/25/images-from-marble-runs-and-turing-machines/

The only operator in this esolang is _toggle_. It works like this (taken from site page for Turing Tumble):
![Turing Tumble Bit Piece](https://ksr-ugc.imgix.net/assets/016/325/165/19cae5d12c1d7fbeb07222b17ac63909_original.gif?w=680&fit=max&v=1492659230&auto=format&gif-q=50&q=92&s=d6d2f74ec54534198f285ee2f0672606)

A starting marble is represented with a lowercase o (`o`)

If you want to create a toggler that starts learning _left_ (like \\), use a lowercase t (`t` -> `↘`).  
If you want to create a toggler that starts learning _right_ (like /), use an uppercase T (`T` -> `↙`).

In order to make togglers move in unison (thereby allowing turing-completeness), connect them with _wires_.  
In ascii, wires are represented via periods (`.`). These are prettified into unicode lines (e.g. `┄`).

Marbles can also be controlled via _gates_.  
An open gate is represented by a colon (`:`) and a closed gate is represented by an exclamation mark (`!`).

A gate can be opened/closed via a pulse from a toggler down a connected wire.

<sub>
## Ascii vs Unicode source
Programs are typically written with AsciiDots' ascii path rules:

```
 /---
 |
 |
/t\
|.+..
\v/ .
/t\ .
|.+./
| |
| *---
| |
| |
| |
```

... And then translated into Unicode box drawings via `prettify.py`:

```
 ╔═══
 ║    
 ║    
╔↘╗   
║╰+┄╮
╚⇓╝ ┆
╔↘╗ ┆
║╰+┄╯
║ ║   
║ *══
║ ║   
║ ║   
║ ║
```

Prettified code can always be re-asciified via `asciify.py`.
</sub>

---

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
