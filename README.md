# MarbleComplete
_Build and simulate your own turing-complete marble runs with ascii/unicode art_

I have always had a love for mechanical computers. After reading a wonderful post on [turing-complete marble runs](https://nbickford.wordpress.com/2014/03/25/images-from-marble-runs-and-turing-machines/), I decided that I wanted to design a turing-complete marble tower. From this desire was born MarbleComplete, the 2d esolang for designing (turing-complete) marble runs using [AsciiDots](https://github.com/aaronduino/asciidots) syntax.

[![Join the chat at https://gitter.im/marble-complete/Lobby](https://badges.gitter.im/marble-complete/Lobby.svg)](https://gitter.im/marble-complete/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<a class="anchor" name="demo-gif"></a>
[![Fun demo looks cool](https://raw.githubusercontent.com/aaronduino/marble-complete/master/demo.gif)](https://aaronduino.github.io/marble-complete/demo?code=%0A%20%20%20%20o%0A%20%20%20%20%7C%0A%2F---v---%5C%0A%7C%20%20%20%7C%20%20%20%7C%0A%3A.%2F-t-%5C%20%7C%0A%7C.%2B..%20%7C%20%7C%0A%7C%20%7C%20%20%20%7C%20%7C%0A%5E-t%20%20%20t-%2F%0A%7C%20.....%0Ao%0A)

Unlike it's parent [AsciiDots](https://github.com/aaronduino/asciidots), the only logical operator in MarbleComplete is a _toggler_:

![Turing Tumble Bit Piece](https://raw.githubusercontent.com/aaronduino/marble-complete/master/toggler.gif)

The Turing Tumble kickstarter has a [gif of the real life equivalent](https://ksr-ugc.imgix.net/assets/016/325/165/19cae5d12c1d7fbeb07222b17ac63909_original.gif?w=680&fit=max&v=1492659230&auto=format&gif-q=50&q=92&s=d6d2f74ec54534198f285ee2f0672606).

## Running the Interpreter

Run `python3 interpret.py --help` to read about available flags.

For the demo gif, I ran the interpreter in auto-stepped debug mode with a delay of 0.25 seconds. The code was prettified, too.

```
python3 interpret.py test.marbles -a 0.25 -d -p
```

## Documentation

### Starting & Ending
A starting marble is represented with a lowercase o (`o`).  
Program execution ends when a marble rolls over an ampersand (`&`).

### Comments
Everything on a line after a pound symbol (`#`) is considered a comment and is ignored by the interpreter.

```
& # This text is a comment.
```

### Paths
Marbles travel down paths (`|` or `-`):

```
o # This is where the program starts
| # The marble travels downwards
| # Keep on going!
& # The program ends
```

Think as these two paths as mirrors:  
`/`  
`\`  

You can use them to make a path turn:

```
/-&         # This is where the program ends!
|
\-\ /-\
  | | |
/-/ | \-\
\---/   |
        |
        \-o # Here's where the program starts
```

#### Special Paths
`+` is the crossing of paths (they do not interact)

`>` acts like a regular, 2-way, horizontal, path, except marbles can be inserted into the path from the bottom or the top. Those marbles will go to the right<br>
`<` does likewise except new marbles go to the left<br>
`^` (caret) does this but upwards<br>
`v` (the lowercase letter 'v') does likewise but downwards

Here's a way to "bounce" a marble backwards along its original path using these symbols:

```
/->-- # Input/output comes through here
| |
\-/
```

But there's an easier way to do that:

`(` reflects a marble backwards along its original path. It accepts marble coming from the left, and lets them pass through to the right<br>
`)` does likewise but for the opposite direction

`*` duplicates a marble and distributes copies including the original marble to all attached paths except the origin of marble

Here's a fun example of using these special paths. Don't worry—we'll soon be able to do more than just start then end a program.

```
  /-\ /-& # End
  | | |
  \-+-v
    | | /-\
(-<-/ | | |
  |   \-<-/
  \-\
    |
    o    # Start
```

## Togglers

If you want to create a toggler that starts learning _left_ (like \\), use a lowercase t (`t` -> `↘`).  
If you want to create a toggler that starts learning _right_ (like /), use an uppercase T (`T` -> `↙`).

## Wires

In order to make togglers move in unison (thereby allowing turing-completeness), connect them with _wires_.

In ascii, wires are represented via periods (`.`). These can be automatically [prettified](#ascii-vs-unicode-source) into unicode lines (e.g. `┄`).

## Gates
Marbles can also be controlled via _gates_.  
An open gate is represented by a colon (`:`) and a closed gate is represented by an exclamation mark (`!`).

A gate can be opened/closed via a pulse from a toggler down a connected wire.

Gates are useful when you want to control the order in which marbles move.

## IO
Getting input from stdin is very simple. Whenever a marble rolls onto a question mark (`?`), it reads one character from stdin. If that character is a `0`, the marble moves to the left, and if the character is a `1`, the marble  moves to the right. If the character read from std in is neither a `0` nor a `1`, an exception is thrown.

Example:

```
  o
  |
/-?-\
|   |
|   \-- # the input was `1`
|
\------ # the input was `0`
```

If a wire activates a `1`, a `1` is printed to stdout. If a wire activates a `0`, a `0` is printed to stdout.  
`0`'s and `1`'s are conductive, meaning that can act like wires.

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

# Sample Programs

Memory Cell:

```
 o
 |
 v----------------- # query
 |
 |     /----------- # set to 0
 |     |   /------- # set to 1
 |     |   |
 |     |   |    /-- # toggle
 |     v\ /v    |
/t\   /t/ \t\  /t\
|.+.. |.   .|  |.|
\v/ ..+.....+..+.|
/t\ . |     |  | |
|.+.. |     |  | \-- # now 1
| |   |     |  \---- # now 0
0 1
```

Memory tape:

```
           /v----o
 o     o   \T
 |    \v\-\ .
 |     !+.+.*
/t\    || | .
|.+.. /T+-* .
\v/ ..+.| | .
 |  . | | | .
/+\ . *-+-v .
||t.. | | | .
\+----+-+-/ .
 |    \v\-\ .
 |     !+.+.*
/t\    || | .
|.+.. /T+-* .
\v/ ..+.| | .
 |  . | | | .
/+\ . *-+-v .
||t.. | | | .
\+----+-+-/ .
 |    \v\-\ .
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
