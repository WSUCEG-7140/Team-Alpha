/*
 * Copyright 2015 brutusin.org
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 * @author Ignacio del Valle Alles idelvall@brutusin.org
 */
if ("undefined" === typeof brutusin || "undefined" === typeof brutusin["json-forms"]) {
    throw new Error("brutusin-json-forms-bootstrap.js requires brutusin-json-forms.js");
}
if ("undefined" === typeof markdown && window.console) {
    console.warn("Include markdown.js (https://github.com/evilstreak/markdown-js) to add markdown support in property description popups");
}

if (("undefined" === typeof $ || "undefined" === typeof $.fn || "undefined" === typeof $.fn.selectpicker) && window.console) {
    console.warn("Include bootstrap-select.js (https://github.com/silviomoreto/bootstrap-select) to turn native selects into bootstrap components");
}

//@description Issue#68 - Add new field to support file format type [https://github.com/WSUCEG-7140/Team-Alpha/pull/75]
if ("undefined" === typeof bsCustomFileInput && window.console) {
    console.warn("Include bs-custom-file-input.min.js (https://github.com/Johann-S/bs-custom-file-input) to have a more interative UI for file selection");
}

(function () {
    var BrutusinForms = brutusin["json-forms"];

    /**
     * **This is callback function extended from the main class**
     * @description Add bootstrap class into the input fields.
     * 
     * @param {HTMLElement} element - The HTMLElement
     * @param {Object} schema - The JSON schema
     *
     * @pre 
	 * element must be a valid non-null HTMLElement.
	 * schema must be a valid object or undefined.
	 *
	 * @post 
	 * The element must have the necessary CSS classes and DOM modifications based on the schema. 
	 * 
	 * @invariant
	 * The BrutusinForms.addDecorator function adds specific CSS classes and DOM modifications to the provided element based on the provided schema.
     */
    BrutusinForms.addDecorator(function (element, schema) {
        if (element.tagName) {
            var tagName = element.tagName.toLowerCase();
			//@description Issue#68 - Add new field to support file format type [https://github.com/WSUCEG-7140/Team-Alpha/pull/75]
			//@description Issue#51 - Add new field to support range input type. [https://github.com/WSUCEG-7140/Team-Alpha/pull/59]
			//@description Issue#24 - Adding new field to support radio button [https://github.com/WSUCEG-7140/Team-Alpha/pull/25]
            if (tagName === "input" && (element.type !== "file" && element.type !== "checkbox" && element.type !== "radio" && element.type !== "range") || tagName === "textarea") {
                element.className += " form-control";
            } else if (tagName === "select") {
				//@description Issue#45 - Update bootstrap version to 4.6 and give website modern look [https://github.com/WSUCEG-7140/Team-Alpha/pull/47]
                element.className += " form-control";
            } else if (tagName === "button") {
                if (element.className === "remove") {
					//@description Issue#55 - Abstract usage of glyphicon as bootstrap 4 doesn't support it. [https://github.com/WSUCEG-7140/Team-Alpha/pull/62]
                    element.className += " bi bi-x";
                    while (element.firstChild) {
                        element.removeChild(element.firstChild);
                    }
                }
                element.className += " btn btn-warning btn-sm";
			//@description Issue#68 - Add new field to support file format type [https://github.com/WSUCEG-7140/Team-Alpha/pull/75]
            } else if (tagName === "input" && element.type === "file") {
                element.className += " custom-file-input";
                var label = document.createElement("label");
                label.className = "custom-file-label";
                label.innerHTML = "Choose file";
                label.setAttribute("for", element.id);
                element.parentNode.classList.add("custom-file");
                element.parentNode.appendChild(label);
                if ("undefined" !== typeof bsCustomFileInput || "undefined" !== typeof $) {
                    $(document).ready(function () {
                        bsCustomFileInput.init();
                    });
                }
            }
        }
    });

    /**
     * **This is callback function extended from the main class**
     * @description Customize the range input value
     * 
     * @param {HTMLElement} element - The HTMLElement
     * @param {Object} schema - The JSON schema
     *
     * 
	 * @pre 
	 * element must be a valid non-null HTMLElement.
	 * schema must be a valid non-null object.
	 *
	 * @post 
	 * The element must have the necessary CSS classes and DOM modifications based on the schema.
	 * 
	 * @invariant
	 * The BrutusinForms.addDecorator function adds specific CSS classes and DOM modifications to the provided input element if it is of type "range".
     *
     */
    BrutusinForms.addDecorator(function (element, schema) {
        if (element.tagName) {
            var tagName = element.tagName.toLowerCase();
            if (tagName === "input" && element.type === "range") {
                element.className += " form-control-range";
                var elementId = element.id;
                element.setAttribute("oninput", "rangevalue" + elementId.substring(elementId.length - 3, elementId.length) + ".value=value");
                var output = document.createElement("output");
                output.id = "rangevalue" + elementId.substring(elementId.length - 3, elementId.length);
                element.parentNode.appendChild(output);
            }
        }
    });

    /**
     * **This is callback function extended from the main class**
     * @description Add a collapsible form
     * 
     * @param {HTMLElement} element - The HTMLElement
     * @param {Object} schema - The JSON schema
     *	 
     * @pre 
	 * element must be a valid non-null HTMLElement.
	 * schema must be a valid object or undefined.
	 *
	 * @post 
	 * The element must have the necessary popover with the help content based on the title.
	 * 
	 * @invariant
	 * The BrutusinForms.addDecorator function adds a collapsible behavior to the provided form element if the schema object specifies it as collapsible.
     */
	//@description Issue#12 - Adding Collapsible Form support [https://github.com/WSUCEG-7140/Team-Alpha/pull/28]
    BrutusinForms.addDecorator(function (element, schema) {
        if (schema !== undefined) {
            if (schema.collapsible !== undefined && schema.collapsible === true) {
                var parentElement = element.parentElement;
                var tagName = parentElement.tagName.toLowerCase();
                if (tagName === "form") {
                    parentElement.className += " brutusin-card-body";
                    var formParentElement = parentElement.parentElement;

                    var divCard = document.createElement("div");
                    divCard.className = "brutusin-card";
                    divCard.innerHTML = "<div class='brutusin-card-header'><a id='expand-btn' class='btn btn-link' data-toggle='collapse' data-target='#brutusin-form-collapsible' aria-expanded='true' aria-controls='brutusin-form-collapsible'></a></div>";

                    var divCardBody = document.createElement("div");
                    divCardBody.className = "collapse show";
                    divCardBody.id = "brutusin-form-collapsible";
                    divCardBody.setAttribute("aria-expanded", "true");
                    divCardBody.appendChild(parentElement);
                    divCard.appendChild(divCardBody);
                    
                    formParentElement.appendChild(divCard);

                    if (schema.title !== undefined) {
                        document.getElementById("expand-btn").textContent = schema.title;
                    }
                }
            } 
        }
    });
    

    /**
     * **This is callback function extended from the main class**
     * @description Add an info icon beside the label to show the description
     * 
     * @param {HTMLElement} element - The HTMLElement
     * @param {Object} schema - The JSON schema
     *
	 * @pre 
	 * element must be a valid non-null HTMLElement.
	 * schema must be a valid object or undefined.
	 *
	 * @post 
	 * The element must have the necessary popover with the help content based on the title.
	 * 
	 * @invariant
	 * The BrutusinForms.addDecorator function adds a help icon with appropriate attributes and behavior to the provided label or button elements based on the provided element and schema. 
     *
     */
    BrutusinForms.addDecorator(function (element, schema) {
        if (element.tagName) {
            var tagName = element.tagName.toLowerCase();
            if (tagName === "label" || tagName === "button") {
                if (element.title) {
					//@description Issue#55 - Abstract usage of glyphicon as bootstrap 4 doesn't support it [https://github.com/WSUCEG-7140/Team-Alpha/pull/62]
                    var helpLink = document.createElement("i");
                    helpLink.setAttribute("style", "outline: 0; text-decoration: none; margin-left: 2px;");
                    helpLink.setAttribute("tabIndex", -1);
                    helpLink.className = "bi bi-info-circle-fill"
                    helpLink.setAttribute("data-toggle", "popover");
                    helpLink.setAttribute("data-trigger", "hover");
                    if ("undefined" === typeof markdown) {
                        helpLink.setAttribute("data-content", element.title);
                    } else {
                        helpLink.setAttribute("data-content", markdown.toHTML(element.title));
                    }
                    if (schema.title) {
                        helpLink.title = schema.title;
                    } else {
                        helpLink.title = "Help";
                    }
                    $(helpLink).popover({
                        placement: 'top',
                        container: 'body',
                        html: !("undefined" === typeof markdown)
                    });
                    if (tagName === "label") {
                        element.appendChild(helpLink);
                    }
                    else if (tagName === "button") {
                        element.parentNode.appendChild(helpLink);
                    }
                }
            }
        }
    });

// Popover over inputs
//BrutusinForms.addDecorator(function (element, schema) {
//if (element.tagName) {
//        if (element.title && (tagName === "input" || tagName === "textarea" || tagName === "select")) {
//            element.setAttribute("data-toggle", "tooltip");
//            element.setAttribute("data-trigger", "focus");
//            if ("undefined" === typeof markdown) {
//                element.setAttribute("data-content", element.title);
//            } else {
//                element.setAttribute("data-content", markdown.toHTML(element.title));
//            }
//            if (schema.title) {
//                element.title = schema.title;
//            } else {
//                element.title = "Help";
//            }
//            $(element).popover({
//                placement: 'top',
//                container: 'body',
//                html: !("undefined" === typeof markdown)
//            });
//        }input
//    }
//});

    /**
     * **This is callback function extended from the main class**
     * @description Add a 3rd party library bootstrap-select for changing the `select` UI layout
     * 
     * @param {HTMLElement} element - The HTMLElement
     * @param {Object} schema - The JSON schema
     */
    BrutusinForms.addDecorator(function (element, schema) {
        if (element.tagName) {
            var tagName = element.tagName.toLowerCase();
            // https://github.com/silviomoreto/bootstrap-select
            if (!("undefined" === typeof $ || "undefined" === typeof $.fn || "undefined" === typeof $.fn.selectpicker) && tagName === "select") {
                element.title = "";
                element.className += " selectpicker";
                element.setAttribute("data-live-search", true);
                $(element).selectpicker();
            }
        }
    });

    BrutusinForms.bootstrap = new Object();

    /**
     * **This is callback function extended from the main class**
     * @description Add `format` type to the input field
     * 
     * @param {string} format - The format type. Eg: "password", "email"
     * @param {string} inputType - The input type from the JSON schema
     * @param {string} bootstrapIcon - The Bootstrap Icon name
     * @param {string} titleDecorator - The title decorator
     * @param {CallableFunction} cb - Callback function
     *
     * @pre 
	 * schema must be a valid non-null object.
	 * input must be a valid non-null HTMLElement.
	 *
	 * @post 
	 * The returned value must be of a valid type according to the schema definition.
	 * 
	 * @invariant
	 * The BrutusinForms.bootstrap.addFormatDecorator function adds format-specific decorations to the provided form elements based on the specified format, inputType, bootstrapIcon, titleDecorator, and cb parameters.
     *
     */
	//@description Issue#55 - Abstract usage of glyphicon as bootstrap 4 doesn't support it [https://github.com/WSUCEG-7140/Team-Alpha/pull/62]
    BrutusinForms.bootstrap.addFormatDecorator = function (format, inputType, bootstrapIcon, titleDecorator, cb) {
        BrutusinForms.addDecorator(function (element, schema) {
            if (element.tagName) {
                var tagName = element.tagName.toLowerCase();
                if (tagName === "input" && schema.type === "string" && schema.format === format) {
                    if (inputType) {
                        element.type = inputType;
                    }
                    if (bootstrapIcon) {
                        var parent = element.parentNode;
                        var table = document.createElement("table");
                        table.setAttribute("style", "border:none;margin:0");
                        var tr = document.createElement("tr");
                        var td1 = document.createElement("td");
                        td1.setAttribute("style", "width:100%; padding:0;padding-right:4px");
                        table.appendChild(tr);
                        tr.appendChild(td1);
                        parent.removeChild(element);
                        td1.appendChild(element);
                        parent.appendChild(table);
                        var td = document.createElement("td");
                        tr.appendChild(td);
                        td.setAttribute("style", "padding:0");
                        var searchButton = document.createElement("button");
                        searchButton.className = "btn btn-default bi " + bootstrapIcon;
                        searchButton.onclick = function () {
                            cb(element);
                        };
                        td.appendChild(searchButton);
                    }
                }
            }

            if (element instanceof Text) {
                var tagName = element.parentElement.tagName.toLowerCase();
                if (tagName === "label" && titleDecorator) {
                    element.textContent = element.textContent + titleDecorator;
                }
            }
        });
    };

    /**
     * @description Adds a loading animation
     * 
     * @param {HTMLElement} element - The HTMLElement
	 * 
	 * @pre 
	 * element must be a valid non-null HTMLElement.
	 *
	 * @post The loading spinner and loading layer must be added to the parent of the element, and their visibility must be set to "visible".	
	 * 
	 * @invariant
	 * The BrutusinForms.bootstrap.showLoading function shows a loading spinner on the specified element by adding the necessary HTML elements and CSS classes.
     *
     */
    BrutusinForms.bootstrap.showLoading = function (element) {
        if (element && element.parentNode) {
            var loadingId = element.id + "_loading";
            var loadingLayerId = element.id + "_loading-layer";
            var loading = document.getElementById(loadingId);
            var loadingLayer = document.getElementById(loadingLayerId);
            if (!loading) {
                var tagName = element.tagName.toLowerCase();
                element.parentNode.style.position = "relative";
                loading = document.createElement("span");
                loading.id = loadingId;
				//@description Issue#55 - Abstract usage of glyphicon as bootstrap 4 doesn't support it [https://github.com/WSUCEG-7140/Team-Alpha/pull/62]
                loading.className = "spinner-border";
                if (tagName === "select") {
                    loading.className += " loading-icon-select";
                } else if (element.type === "checkbox") {
                    loading.className += " loading-icon-checkbox";
                } else {
                    loading.className += " loading-icon";
                }
                element.parentNode.appendChild(loading);
                loadingLayer = document.createElement("div");
                loadingLayer.className = "loading-layer";
                loadingLayer.appendChild(document.createTextNode(""));
                loadingLayer.id = loadingLayerId;
                element.parentNode.appendChild(loadingLayer);
            }
            loading.style.visibility = "visible";
            loadingLayer.style.visibility = "visible";
        }
    }

    /**
     * @description Remove a loading animation
     * 
     * @param {HTMLElement} element - The HTMLElement
     */
    BrutusinForms.bootstrap.hideLoading = function (element) {
        if (element) {
            var loadingId = element.id + "_loading";
            var loadingLayerId = element.id + "_loading-layer";
            var loading = document.getElementById(loadingId);
            var loadingLayer = document.getElementById(loadingLayerId);
            if (loading) {
                loading.style.visibility = "hidden";
            }
            if (loadingLayer) {
                loadingLayer.style.visibility = "hidden";
            }
        }
    }

    BrutusinForms.onResolutionStarted = BrutusinForms.bootstrap.showLoading;
    BrutusinForms.onResolutionFinished = BrutusinForms.bootstrap.hideLoading;

    /**
     * **This is callback function extended from the main class**
     * @description Adds a Bootstrap class when the validation is success
     * 
     * @param {HTMLElement} element - The HTMLElement
     *
	 * @pre 
	 * element must be a valid non-null HTMLElement.
	 *
	 * @post 
	 * The "is-invalid" class must be removed from the element's class list.
	 * 
	 * @invariant
	 * The BrutusinForms.onValidationSuccess function removes the "is-invalid" class from the class list of the provided element, if it exists.
     *
     */
    BrutusinForms.onValidationSuccess = function (element) {
        element.className = element.className.replace(" is-invalid", "");
    }

    /**
     * **This is callback function extended from the main class**
     * @description Adds a Bootstrap class when the validation is failed
     * 
     * @param {HTMLElement} element - The HTMLElement
     *
	 * @pre 
	 * element must be a valid non-null HTMLElement.
	 * message must be a valid non-empty string.
	 *
	 * @post 
	 * The error message must be displayed near the element, and the "is-invalid" class must be added to the element's class list.
	 * 
	 * @invariant
	 * The BrutusinForms.onValidationError function appends an error message div (div) with the provided message to the parent node of the given element. It also sets the element's title attribute to the value of BrutusinForms.messages["validationError"] and adds the "is-invalid" class to the element's class list if it does not already exist.
     *
     */
    BrutusinForms.onValidationError = function (element, message) {

        var div = document.createElement("div");
        div.className = "invalid-feedback";
        if ("undefined" === typeof markdown) {
            div.innerHTML = message;
        } else {
            div.innerHTML = markdown.toHTML(message);
        }
        element.parentNode.appendChild(div);
        element.title = BrutusinForms.messages["validationError"];
        if (!element.className.includes("is-invalid")) {
            element.className += " is-invalid";
        }
    }
}());
