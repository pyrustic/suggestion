
Back to [Reference Overview](https://github.com/pyrustic/suggestion/blob/master/docs/reference/README.md#readme)

# suggestion.\_\_init\_\_



<br>


```python
SPECIAL_WORDS = {'Return': '\n', 'space': ' ', 'Tab': '\t'}

```

<br>

```python

class DefaultDropdown:
    """
    This is the 'interface' that your Dropdown must respects 
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def selected(self):
        """
        
        """

    def populate(self, data):
        """
        Called by Suggestion after the engine sent results 
        """

    def relocate(self, info):
        """
        Called by Suggestion to indicate the Dropdown to change its coords 
        """

    def select_down(self):
        """
        User pressed the down arrow key 
        """

    def select_up(self):
        """
        User pressed the up arrow key 
        """

```

<br>

```python

class DefaultEngine:
    """
    
    """

    def __init__(self, dataset):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def process(self, info, callback):
        """
        
        """

```

<br>

```python

class Dropdown:
    """
    This is the 'interface' that your Dropdown must respects 
    """

    @property
    def selected(self):
        """
        Returns the selected word (string)
        """

    def populate(self, data):
        """
        Called by Suggestion after the engine sent results 
        """

    def relocate(self, info):
        """
        Called by Suggestion to indicate the Dropdown to change its coords 
        """

    def select_down(self):
        """
        User pressed the down arrow key 
        """

    def select_up(self):
        """
        User pressed the up arrow key 
        """

```

<br>

```python

class Engine:
    """
    
    """

    def process(self, info, callback):
        """
        
        """

```

<br>

```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class IllegalWidgetError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class Info:
    """
    
    """

    def __init__(self, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class Suggestion:
    """
    
    """

    def __init__(self, widget, dataset=None):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def activated(self):
        """
        
        """

    @property
    def dataset(self):
        """
        
        """

    @property
    def dropdown(self):
        """
        
        """

    @dropdown.setter
    def dropdown(self, val):
        """
        
        """

    @property
    def engine(self):
        """
        
        """

    @engine.setter
    def engine(self, val):
        """
        
        """

    @property
    def widget(self):
        """
        
        """

    def activate(self):
        """
        
        """

    def deactivate(self):
        """
        
        """

```

