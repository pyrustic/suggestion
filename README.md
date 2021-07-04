# Suggestion
`Suggestion` is a `Python` library for democratizing auto-complete(suggest) in desktop applications. It's part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).

[Installation](#installation) | [Website](https://pyrustic.github.io)

## Overview
Auto-complete(suggest) is a feature available in smartphone keyboards, browser search bars, and IDEs, so why not in your app too ?

`Suggestion` is the library you need to power your applications with auto-complete or auto-suggest feature.

This [article](https://uxmag.com/articles/designing-search-as-you-type-suggestions) shows the difference between auto-suggest and auto-complete.

Let's discover how to use `Suggestion`:

```python
import tkinter as tk
from suggestion import Suggestion


# the dataset
DATASET = ["friend", "family", "my", "monster"]

# root
root = tk.Tk()
root.title("Suggestion demo | built with Pyrustic")

# text field (it works with tk.Entry too !)
text_field = tk.Text(root)
text_field.pack()

# Suggestion
suggestion = Suggestion(text_field, dataset=DATASET)

# lift off !
root.mainloop()


```

This is what it looks like when you run the code:

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/suggestion-demo-1.gif" alt="Figure" width="600">
    <p align="center">
    <i> Figure 1 </i>
    </p>
</div>

Did my ridiculous dataset make you smile ? It's not realistic, right ? I agree.

Ok, let's download a [list](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) of 370K english words from [https://github.com/dwyl/english-words](https://github.com/dwyl/english-words).

```python
import tkinter as tk
from suggestion import Suggestion

# the dataset
DATASET = "/home/alex/words_alpha.txt"

# root
root = tk.Tk()
root.title("Suggestion demo | built with Pyrustic")

# text field (it works with tk.Entry too!)
text_field = tk.Text(root)
text_field.pack()

# Suggestion
suggestion = Suggestion(text_field, dataset=DATASET)

# lift off !
root.mainloop()

```

Watch how smooth it is:

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/suggestion-demo-2.gif" alt="Figure" width="600">
    <p align="center">
    <i> Figure 2 </i>
    </p>
</div>

I can type faster, duh !

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/suggestion-demo-3.gif" alt="Figure" width="600">
    <p align="center">
    <i> Figure 3 </i>
    </p>
</div>



What if I told you that so far you've only seen the default configuration/behavior of `Suggestion` ?


There are 3 main parts in `Suggestion`:
- the `dataset`: by default it is a sequence of words. You can set any data type you want if you have a custom `engine` that knows how to use the dataset.
- the `engine`: by default it is a basic algorithm which compares the words you type with the words of the dataset (provided that the dataset is a list of words). You can set your own engine and define your own type of dataset.
- the `dropdown`: by default this is a simple tk.Listbox in a headless window that displays the suggested words returned by the engine. You can define your own drop down list to display rich data, with icons or whatever you want.

Maybe you have a sophisticated dataset of words with metadata like probability of occurrence, and you need to keep track of words already typed to perform complex calculations. `Suggestion` is the library you need to implement your project !

If you want to create your custom auto-complete(suggest) `engine`, these links could be helpful:
- [https://norvig.com/spell-correct.html](https://norvig.com/spell-correct.html)
- [https://github.com/rodricios/autocomplete](https://github.com/rodricios/autocomplete)
- [https://www.jeremymikkola.com/posts/2019_03_19_rules_for_autocomplete.html](https://www.jeremymikkola.com/posts/2019_03_19_rules_for_autocomplete.html)
- [Rules of Autocomplete (Hackernews)](https://news.ycombinator.com/item?id=19438826)

As `Suggestion` is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io), it is compatible with the [Cyberpunk Theme](https://github.com/pyrustic/cyberpunk-theme):

```python
import tkinter as tk
from suggestion import Suggestion
from cyberpunk_theme import Cyberpunk


# the dataset
DATASET = "/home/alex/words_alpha.txt"

# root
root = tk.Tk()
root.title("Suggestion demo | built with Pyrustic")

# set the theme
Cyberpunk().target(root)

# text field (it works with tk.Entry too!)
text_field = tk.Text(root)
text_field.pack()

# Suggestion
suggestion = Suggestion(text_field, dataset=DATASET)

# lift off !
root.mainloop()

```

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/suggestion-demo-4.gif" alt="Figure" width="650">
    <p align="center">
    <i> Figure 4 </i>
    </p>
</div>


## Installation
### First time
Install for the first time:

```bash
$ pip install suggestion
```

### Upgrade
To upgrade `Suggestion`:

```bash
$ pip install suggestion --upgrade --upgrade-strategy eager
```

## Documentation
I will write it later. I invite you to clone the project and discover how it works ;) It's easy to understand. The engine and the dropdown must respect their respective "interface" `suggestion.Engine` and `suggestion.Dropdown`. Example, the dropdown must have a method `relocate` that is called by `Suggestion` to ask the dropdown to change its coords. 

Bookmark this project so you don't miss any updates !

You can visit my [website](https://pyrustic.github.io) to discover related cool projects !
