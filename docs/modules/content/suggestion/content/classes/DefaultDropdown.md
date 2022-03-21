Back to [All Modules](https://github.com/pyrustic/suggestion/blob/master/docs/modules/README.md#readme)

# Module Overview

**suggestion**
 
No description

> **Classes:** &nbsp; [DefaultDropdown](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/DefaultDropdown.md#class-defaultdropdown) &nbsp;&nbsp; [DefaultEngine](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/DefaultEngine.md#class-defaultengine) &nbsp;&nbsp; [Dropdown](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/Dropdown.md#class-dropdown) &nbsp;&nbsp; [Engine](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/Engine.md#class-engine) &nbsp;&nbsp; [Error](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/Error.md#class-error) &nbsp;&nbsp; [IllegalWidgetError](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/IllegalWidgetError.md#class-illegalwidgeterror) &nbsp;&nbsp; [Info](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/Info.md#class-info) &nbsp;&nbsp; [Suggestion](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion/content/classes/Suggestion.md#class-suggestion)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; SPECIAL_WORDS

# Class DefaultDropdown
This is the 'interface' that your Dropdown must respects 

## Base Classes
suggestion.Dropdown

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|body|getter|Get the body of this view.|viewable.Viewable|
|selected|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [\_build](#_build) &nbsp;&nbsp; [\_on\_destroy](#_on_destroy) &nbsp;&nbsp; [\_on\_map](#_on_map) &nbsp;&nbsp; [\_select\_line](#_select_line) &nbsp;&nbsp; [build](#build) &nbsp;&nbsp; [build\_grid](#build_grid) &nbsp;&nbsp; [build\_pack](#build_pack) &nbsp;&nbsp; [build\_place](#build_place) &nbsp;&nbsp; [build\_wait](#build_wait) &nbsp;&nbsp; [populate](#populate) &nbsp;&nbsp; [relocate](#relocate) &nbsp;&nbsp; [select\_down](#select_down) &nbsp;&nbsp; [select\_up](#select_up)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_build
Build the view layout here



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_on\_destroy
Put here the code that will be executed at destroy event



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_on\_map
Put here the code that will be executed once
the body is mapped.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_select\_line
None



**Signature:** (self, index)





**Return Value:** None.

[Back to Top](#module-overview)


## build
Build this view 

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## build\_grid
Build this view then grid it 

**Inherited from:** viewable.Viewable

**Signature:** (self, cnf=None, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)


## build\_pack
Build this view then pack it 

**Inherited from:** viewable.Viewable

**Signature:** (self, cnf=None, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)


## build\_place
Build this view then place it 

**Inherited from:** viewable.Viewable

**Signature:** (self, cnf=None, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)


## build\_wait
Build this view then wait till it closes.
The view should have a tk.Toplevel as body 

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## populate
Called by Suggestion after the engine sent results 



**Signature:** (self, data)





**Return Value:** None.

[Back to Top](#module-overview)


## relocate
Called by Suggestion to indicate the Dropdown to change its coords 



**Signature:** (self, info)





**Return Value:** None.

[Back to Top](#module-overview)


## select\_down
User pressed the down arrow key 



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## select\_up
User pressed the up arrow key 



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)



