# json-forms
`org.brutusin:json-forms` is a javascript library that generates HTML forms from [JSON Schemas](http://json-schema.org).

## Status
> We have updated our own flavour of Brutusin forms to an extent where we have covered all the fields and attributes that a form possess. Our project mainly generates HTML Form from Json schemas.

---
**Table of Contents:** 
- [json-forms](#json-forms)
  - [Status](#status)
  - [Features](#features)
  - [Demo](#demo)
  - [API](#api)
    - [Static members:](#static-members)
    - [Instance members:](#instance-members)
  - [Issues](#issues)
  - [Documentation](#documentation)
  - [Program By Contract](#program-by-contract)
  - [Literate Programming](#literate-programming)
  - [Support bugs and requests](#support-bugs-and-requests)
  - [Authors](#authors)
  - [Credits](#credits)

## Features
* Dynamic schemas support
* Extensible and customizable
* No external libraries needed
* Validation
* Multiple forms per document supported


## Demo
[![demo](https://raw.githubusercontent.com/WSUCEG-7140/Team-Alpha/master/img/json-forms-demo.jpg)]


## API

### Static members:

Member|Description
------| -------
`BrutusinForms.create(schema)`|BrutusinForms factory method
`BrutusinForms.addDecorator(f(htmlElement, schema))`| Register a callback function to be notified after an HTML element has been rendered (passed as parameter). See [brutusin-json-forms-bootstrap.js](src/js/brutusin-json-forms-bootstrap.js) for an example of *bootstrap* decorator.
`BrutusinForms.postRender(instance)`|Callback function to be notified after a BrutusinForms instance has been rendered (passed as parameter)
`BrutusinForms.instances`|Array containing all the BrutusinForms instances created in the document by the factory method.

### Instance members:

Member|Description
------| -------
`bf.render(container, data)`| Renders the form inside the the container, with the specified data preloaded
`bf.validate()`| Returns `true` if the input data entered by the user passes validation
`bf.getData()`| Returns the javascript object with the data entered by the user
`bf.schemaResolver(schemaIdArray, data)`| Schema resolver for [dynamic schemas](#dynamic-schemas)


## Issues

[Issue#6](https://github.com/WSUCEG-7140/Team-Alpha/issues/6) - Remove Colon from Title in Json Schema's

[Issue#7](https://github.com/WSUCEG-7140/Team-Alpha/issues/7) - Make changes to string element to be empty rather than null.

[Issue#5](https://github.com/WSUCEG-7140/Team-Alpha/issues/5) - Write Documentation for changes to be done in the sprints.

[Issue#4](https://github.com/WSUCEG-7140/Team-Alpha/issues/4) - Write test cases to test ongoing changes.

[Issue#9](https://github.com/WSUCEG-7140/Team-Alpha/issues/9) - Remove eval function.

[Issue#10](https://github.com/WSUCEG-7140/Team-Alpha/issues/10) - Add new field to support email and its validation

[Issue#11](https://github.com/WSUCEG-7140/Team-Alpha/issues/11) - Clean data after onChange between oneOf

[Issue#12](https://github.com/WSUCEG-7140/Team-Alpha/issues/12) - Add collapsible form support

[Issue#13](https://github.com/WSUCEG-7140/Team-Alpha/issues/13) - Add new field to support Date and time

[Issue#15](https://github.com/WSUCEG-7140/Team-Alpha/issues/15) - Validation to fail if required field is empty

[Issue#17](https://github.com/WSUCEG-7140/Team-Alpha/issues/17) - Display default values in an array when initial data is passed

[Issue#19](https://github.com/WSUCEG-7140/Team-Alpha/issues/19) - Support Custom-Class Support

[Issue#24](https://github.com/WSUCEG-7140/Team-Alpha/issues/24) - Add new field to support radio buttons

[Issue#32](https://github.com/WSUCEG-7140/Team-Alpha/issues/32) - getData() function to get working with oneOf schema

[Issue#35](https://github.com/WSUCEG-7140/Team-Alpha/issues/35) - Add functionalities to work with radio buttons

[Issue#37](https://github.com/WSUCEG-7140/Team-Alpha/issues/37) - Add new field to support URL type

[Issue#38](https://github.com/WSUCEG-7140/Team-Alpha/issues/38) - Add new field to support checkboxes in a field

[Issue#41](https://github.com/WSUCEG-7140/Team-Alpha/issues/41) - Add new field to support phone number

[Issue#42](https://github.com/WSUCEG-7140/Team-Alpha/issues/42) - Add more test cases to additional functional UI changes

[Issue#43](https://github.com/WSUCEG-7140/Team-Alpha/issues/43) - Add a reset button in final page to update all fields to Null

[Issue#44](https://github.com/WSUCEG-7140/Team-Alpha/issues/44) - Fix data support for checkbox which is retrieving empty values

[Issue#45](https://github.com/WSUCEG-7140/Team-Alpha/issues/45) - Update bootstrap version to 4.6 and give website modern look

[Issue#48](https://github.com/WSUCEG-7140/Team-Alpha/issues/48) - Add new schema for URL Changes

[Issue#50](https://github.com/WSUCEG-7140/Team-Alpha/issues/50) - Fix the error message that are not appearing when there is an error in the schema

[Issue#51](https://github.com/WSUCEG-7140/Team-Alpha/issues/51) - Add new field to support range input type

[Issue#52](https://github.com/WSUCEG-7140/Team-Alpha/issues/52) - Update Radio Button and Checkbox UI with new Bootstrap Version

[Issue#53](https://github.com/WSUCEG-7140/Team-Alpha/issues/53) - Add new schema to create registration form

[Issue#54](https://github.com/WSUCEG-7140/Team-Alpha/issues/54) - Add Collapsible form changes as a new schema

[Issue#55](https://github.com/WSUCEG-7140/Team-Alpha/issues/55) - Abstract usage of glyphicon as bootstrap 4 doesn't support it

[Issue#64](https://github.com/WSUCEG-7140/Team-Alpha/issues/64) - Add Red border to text field when there is validation error

[Issue#65](https://github.com/WSUCEG-7140/Team-Alpha/issues/65) - Add new schema for Contact Form

[Issue#66](https://github.com/WSUCEG-7140/Team-Alpha/issues/66) - Beautify the form to loosen the fields with bootstrap 4

[Issue#67](https://github.com/WSUCEG-7140/Team-Alpha/issues/67) - Add new schema for Delivery Form

[Issue#68](https://github.com/WSUCEG-7140/Team-Alpha/issues/68) - Add new field to support file format type

[Issue#69](https://github.com/WSUCEG-7140/Team-Alpha/issues/69) - Add new schema for Product Listing Form

[Issue#70](https://github.com/WSUCEG-7140/Team-Alpha/issues/70) - Update Validation Error Popup with bootstrap 4 update

[Issue#71](https://github.com/WSUCEG-7140/Team-Alpha/issues/71) - Commit the changes of meeting minutes

[Issue#72](https://github.com/WSUCEG-7140/Team-Alpha/issues/72) - Add Design Documentation for the project

[Issue#87](https://github.com/WSUCEG-7140/Team-Alpha/issues/87) - Add Changes for Contract Programming


## Documentation

We have used both Doxygen and Jsdoc for documentation of code. [Jsdoc](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/JSDOC_Documentation.zip) supports documentation for javascript Files. [Doxygen](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/Doxygen_Documentation.zip) provides documentation for rest of the files.

Command to run Doxygen 	-	doxygen Doxyfile
Command to run JsDoc	-	jsdoc -c jsdoc.json

Documentation changes have been automated and able to run with [Action](https://github.com/WSUCEG-7140/Team-Alpha/actions/workflows/python_tests.yml) which uses configuration [file](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/.github/workflows/python_tests.yml)

## Program By Contract

Contract Programming has been implemented to this project code. Have croppped both modified and added functions of this project into below 2 text files for easy reference.
[File_1](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/program_by_contract/brutusin-json-forms.txt)
[File_2](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/program_by_contract/brutusin-json-forms-bootstrap.txt)

## Literate Programming

Literate Programming changes have been added to this project code. Attached files for reference.
[File_1](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/src/js/brutusin-json-forms.js)
[File_2](https://github.com/WSUCEG-7140/Team-Alpha/blob/master/src/js/brutusin-json-forms-bootstrap.js)

## Support bugs and requests

https://github.com/WSUCEG-7140/Team-Alpha/issues

## Authors

* Yaswanth Jonnakuti	-	jonna01
* Rakesh Gunturu		-	gunturuwsu
* Saikumar Pulluri		-	saikumarpulluri
* Rohith Kalakuntla		-	kalakuntlarohith


## Credits
- Ignacio del Valle Alles (<https://github.com/idelvall/>)

Contributions are always welcome and greatly appreciated!