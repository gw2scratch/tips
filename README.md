# GW2 Scratch Tips & Tricks
A collection of Guild Wars 2 tips and tricks.

## Contributing

Any kind of contribution is very much welcome. Feel free to create an issue if you find an inaccuracy, a typo or even if you think of something that should be included.

The text of the tips is located in the [tips.html](tips.html) file. Pull requests are also welcome.

## The tip template

The [tips.html](tips.html) file uses a very simple template system. To generate the actual html file, run the convert script:

```
./convert.py tips.html output.html
```

The system implemented by simple regex replace in [convert.py](convert.py). Do not expect it to do anything intelligent. Only things in parantheses are taken out and placed into the current tip template, they may be multiline, use any html tag. Do not swap usefulness and importance, do not add extra attributes, all of these changes would make the tip get silently ignored.

```html
<scr-tip usefulness="(5)" importance="(5)">
  <tip-title>(Tip Title)</tip-title>
  <tip-desc>(Detailed Description)</tip-desc>
</scr-tip>
```
## HTML + CSS

The webpage uses the [Bulma](https://github.com/jgthms/bulma) CSS framework.

## Images

The [images/](images) folder contains screenshots from Guild Wars 2 relevant to the tips.
