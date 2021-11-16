Back to [Modules overview](https://github.com/pyrustic/suggestion/blob/master/docs/modules/README.md)
  
# Module documentation
>## suggestion.\_\_init\_\_
No description
<br>
[constants (1)](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion.__init__/constants.md) &nbsp;.&nbsp; [classes (8)](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion.__init__/classes.md)


## Classes
```python
class DefaultDropdown(suggestion.__init__.Dropdown):
    """
    This is the 'interface' that your Dropdown must respects 
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    @property
    def selected(self):
        """
        
        """

    # inherited from viewable.Viewable
    @property
    def state(self):
        """
        Return the current state of the Viewable instance.
        States are integers, you can use these constants:
            - pyrustic.view.NEW: the state just after instantiation;
            - pyrustic.view.BUILT: the state after the call of _built
            - pyrustic.view.MAPPED: the state after the call of on_map
            - pyrustic.view.DESTROYED: the state after the call of on_destroy
        """

    # inherited from viewable.Viewable
    def build(self):
        """
        Build this view object. It returns the body 
        """

    # inherited from viewable.Viewable
    def build_grid(self, cnf=None, **kwargs):
        """
        Build this view then grid it 
        """

    # inherited from viewable.Viewable
    def build_pack(self, cnf=None, **kwargs):
        """
        Build this view then pack it 
        """

    # inherited from viewable.Viewable
    def build_place(self, cnf=None, **kwargs):
        """
        Build this view then place it 
        """

    # inherited from viewable.Viewable
    def build_wait(self):
        """
        Build this view then wait till it closes.
        The view should have a tk.Toplevel as body 
        """

    # inherited from viewable.Viewable
    def destroy(self):
        """
        Destroy the body of this view 
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

    def _build(self):
        """
        Build the view here by defining the _body instance
        """

    def _on_destroy(self):
        """
        Put here the code that will be executed at destroy event
        """

    def _on_map(self):
        """
        Put here the code that will be executed once
        the body is mapped.
        """

    def _select_line(self, index):
        """
        
        """

```

```python
class DefaultEngine(suggestion.__init__.Engine):
    """
    
    """

    def __init__(self, dataset):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def process(self, info, callback):
        """
        
        """

    def _prepare_dataset(self):
        """
        
        """

    def _search(self, word, callback):
        """
        
        """

    def _setup(self):
        """
        
        """

```

```python
class Dropdown(viewable.Viewable):
    """
    This is the 'interface' that your Dropdown must respects 
    """

    # inherited from viewable.Viewable
    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    @property
    def selected(self):
        """
        Returns the selected word (string)
        """

    # inherited from viewable.Viewable
    @property
    def state(self):
        """
        Return the current state of the Viewable instance.
        States are integers, you can use these constants:
            - pyrustic.view.NEW: the state just after instantiation;
            - pyrustic.view.BUILT: the state after the call of _built
            - pyrustic.view.MAPPED: the state after the call of on_map
            - pyrustic.view.DESTROYED: the state after the call of on_destroy
        """

    # inherited from viewable.Viewable
    def build(self):
        """
        Build this view object. It returns the body 
        """

    # inherited from viewable.Viewable
    def build_grid(self, cnf=None, **kwargs):
        """
        Build this view then grid it 
        """

    # inherited from viewable.Viewable
    def build_pack(self, cnf=None, **kwargs):
        """
        Build this view then pack it 
        """

    # inherited from viewable.Viewable
    def build_place(self, cnf=None, **kwargs):
        """
        Build this view then place it 
        """

    # inherited from viewable.Viewable
    def build_wait(self):
        """
        Build this view then wait till it closes.
        The view should have a tk.Toplevel as body 
        """

    # inherited from viewable.Viewable
    def destroy(self):
        """
        Destroy the body of this view 
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

    # inherited from viewable.Viewable
    def _build(self):
        """
        Build the view here by defining the _body instance
        """

    # inherited from viewable.Viewable
    def _on_destroy(self):
        """
        Put here the code that will be executed at destroy event
        """

    # inherited from viewable.Viewable
    def _on_map(self):
        """
        Put here the code that will be executed once
        the body is mapped.
        """

```

```python
class Engine(object):
    """
    
    """

    def process(self, info, callback):
        """
        
        """

```

```python
class Error(Exception):
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class IllegalWidgetError(suggestion.__init__.Error):
    """
    Common base class for all non-exit exceptions.
    """

    # inherited from suggestion.__init__.Error
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class Info(object):
    """
    
    """

    def __init__(self, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

```python
class Suggestion(object):
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

    def _cache_word(self, word):
        """
        
        """

    def _clear(self, focus_set=True):
        """
        
        """

    def _edit_field(self):
        """
        
        """

    def _extract_word(self, cursor_index, line):
        """
        
        """

    def _get_word(self):
        """
        
        """

    def _hide_dropdown(self, focus_set=True):
        """
        
        """

    def _on_key_press(self, event):
        """
        
        """

    def _on_key_release(self, event):
        """
        
        """

    def _process_word(self, event):
        """
        
        """

    def _report_results(self, data=None):
        """
        
        """

    def _setup(self):
        """
        
        """

    def _unhide_dropdown(self):
        """
        
        """

```

