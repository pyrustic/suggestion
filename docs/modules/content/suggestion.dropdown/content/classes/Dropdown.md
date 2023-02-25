Back to [All Modules](https://github.com/pyrustic/suggestion/blob/master/docs/modules/README.md#readme)

# Module Overview

**suggestion.dropdown**
 
No description

> **Classes:** &nbsp; [DefaultDropdown](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion.dropdown/content/classes/DefaultDropdown.md#class-defaultdropdown) &nbsp;&nbsp; [Dropdown](https://github.com/pyrustic/suggestion/blob/master/docs/modules/content/suggestion.dropdown/content/classes/Dropdown.md#class-dropdown)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Dropdown
This is the 'interface' that your Dropdown must respects 

## Base Classes
viewable.Viewable

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|body|getter|Get the body of this view.|viewable.Viewable|
|selected|getter|Returns the selected word (string)||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [build](#build) &nbsp;&nbsp; [build\_grid](#build_grid) &nbsp;&nbsp; [build\_pack](#build_pack) &nbsp;&nbsp; [build\_place](#build_place) &nbsp;&nbsp; [build\_wait](#build_wait) &nbsp;&nbsp; [populate](#populate) &nbsp;&nbsp; [select\_down](#select_down) &nbsp;&nbsp; [select\_up](#select_up) &nbsp;&nbsp; [\_build](#_build) &nbsp;&nbsp; [\_create\_body](#_create_body) &nbsp;&nbsp; [\_on\_destroy](#_on_destroy) &nbsp;&nbsp; [\_on\_map](#_on_map) &nbsp;&nbsp; [\_on\_remap](#_on_remap) &nbsp;&nbsp; [\_on\_unmap](#_on_unmap)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## build
Build this view 

**Inherited from:** viewable.Viewable

**Signature:** (self, parent)





**Return Value:** None

[Back to Top](#module-overview)


## build\_grid
Build this view then grid it 

**Inherited from:** viewable.Viewable

**Signature:** (self, parent, cnf=None, \*\*kwargs)





**Return Value:** None

[Back to Top](#module-overview)


## build\_pack
Build this view then pack it 

**Inherited from:** viewable.Viewable

**Signature:** (self, parent, cnf=None, \*\*kwargs)





**Return Value:** None

[Back to Top](#module-overview)


## build\_place
Build this view then place it 

**Inherited from:** viewable.Viewable

**Signature:** (self, parent, cnf=None, \*\*kwargs)





**Return Value:** None

[Back to Top](#module-overview)


## build\_wait
Build this view then wait till it closes.
The view should have a tk.Toplevel as body 

**Inherited from:** viewable.Viewable

**Signature:** (self, parent)





**Return Value:** None

[Back to Top](#module-overview)


## populate
Called by Suggestion after the engine sent results 



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## select\_down
User pressed the down arrow key 



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## select\_up
User pressed the up arrow key 



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_build
Build the view layout here

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_body
No description

**Inherited from:** viewable.Viewable

**Signature:** (self, parent)





**Return Value:** None

[Back to Top](#module-overview)


## \_on\_destroy
Put here the code that will be executed at destroy event

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_on\_map
Put here the code that will be executed when
the body is mapped.

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_on\_remap
No description

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_on\_unmap
Put here the code that will be executed when
the body is unmapped.

**Inherited from:** viewable.Viewable

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



