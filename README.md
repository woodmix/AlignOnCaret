## Align on caret

"Align on caret" is a Sublime Text 3 plugin.

## Concept

"|" is caret

```
    var foo = |"foo"
    var foobar = |"foobar"
    var foobarbaz = |"foobarbaz"
```
Align on caret!
```
    var foo =       |"foo"
    var foobar =    |"foobar"
    var foobarbaz = |"foobarbaz"
```

shortcut key is ctrl+\\
You can also align via the Edit menu

## Use Case1

hmm...
```
|   var foo = "foo"
    var foobar = "foobar"
    var foobarbaz = "foobarbaz"
```
Sublime standard shortcut shift+alt+down
```
|   var foo = "foo"
|   var foobar = "foobar"
|   var foobarbaz = "foobarbaz"
```
OK, next standard shortcut ctrl+right, ctrl+right, ctrl+right, ctrl+right
```
    var foo =| "foo"
    var foobar =| "foobar"
    var foobarbaz =| "foobarbaz"
```
Align on caret!
```
    var foo =      | "foo"
    var foobar =   | "foobar"
    var foobarbaz =| "foobarbaz"
```
## Use Case2

I want to make comment-stage on end-of-line
```
|   var foo = "foo"
    var foobar = "foobar"
    var foobarbaz = "foobarbaz"
```
select. Sublime standard shortcut shift+ctrl+J (Expand Selection to Indentation)
```
--------------------
:   var foo = "foo":------
:   var foobar = "foobar":------
:   var foobarbaz = "foobarbaz":
--------------------------------
```
Sublime standard shortcut shift+ctrl+L (Split into Lines)
```
    var foo = "foo"|
    var foobar = "foobar"|
    var foobarbaz = "foobarbaz"|
```
Align on caret!
```
    var foo =       "foo"      |
    var foobar =    "foobar"   |
    var foobarbaz = "foobarbaz"|
```
I push tag all I want
```
    var foo =       "foo"           |
    var foobar =    "foobar"        |
    var foobarbaz = "foobarbaz"     |
```
yeah
```
    var foo =       "foo"           // |
    var foobar =    "foobar"        // |
    var foobarbaz = "foobarbaz"     // |
```
