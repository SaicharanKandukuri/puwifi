var ajaxObject;
var sourceControl = null;
var destControl = null;
var selectIndex = 0;
var suggestList = new Array();

// Make Ajax Object as per browser.
function getAjaxObject() {
  try {
    // create XMLHttpRequest for firefox, safari, opera
    ajaxObject = new XMLHttpRequest();
  } catch (e) {
    try {
      // create XMLHttpRequest for IE 6.0+
      ajaxObject = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
      try {
        // create XMLHttpRequest for IE 6.0+
        ajaxObject = new ActiveXObject("Microsoft.XMLHTTP");
      } catch (e) {
        Cyberoam.messageBox({ message: "Your browser is not supporting AJAX" });
      }
    }
  }
  return ajaxObject;
}

// A Function which invokes an Ajax Request to a URL
function invokeAjaxURL(url, mode) {
  try {
    ajaxObject = getAjaxObject();
    ajaxObject.open(mode, url, true);
    ajaxObject.onreadystatechange = processResponse;
    ajaxObject.send("");
  } catch (e) {
    Cyberoam.messageBox({
      message: "Problem in sending request to Cyberoam Server:" + e,
    });
  }
}

function processResponse() {
  try {
    if (ajaxObject.readyState == 4) {
      parseXML(ajaxObject.responseXML);
    }
  } catch (e) {
    parseXML(null);
    //alert("Cyberoam Server is not Reachable.Please re-login after Sometime.");
  }
}
function parseXML(responsexml) {
  Cyberoam.messageBox({
    message:
      "invalid function call from cyberoamAjax.js. Please implement the function in your jsp/html file",
  });
}
/*
 * Returns a function that waits for the specified XMLHttpRequest to complete,
 * then passes it that XML response to the given handler function.
 * req - The XMLHttpRequest whose state is changing
 * responseXmlHandler - Function to pass the XML response to
 */
function getReadyStateHandler(req, responseXmlHandler) {
  try {
    // Return an anonymous function that listens to the XMLHttpRequest instance
    return function () {
      // If the request is completed successfully.
      if (req.readyState == 4) {
        // Check whether we have received a successful response from the server
        if (req.status == 200) {
          // Pass the XML payload of the response to the handler function.

          responseXmlHandler(req.responseXML);
        } else {
          // An HTTP problem has occurred
          Cyberoam.messageBox({
            message: "Connection to the Authentication Server is lost.",
          });
          removeOverlay();
        }
      }
    };
  } catch (e) {}
}

/*
 * This function initialize the Ajax Autocomplete control.
 * Source is the control based on its value the request would be made.
 * Dest is the control on which suggestions would be listed.
 */
function initialize(source) {
  sourceControl = document.getElementById(source);
  destControl = document.createElement("DIV");
  setStyle(destControl);
  document.body.appendChild(destControl);
  clearSuggestList();
  if (sourceControl.addEventListener) {
    sourceControl.addEventListener("blur", clearSuggestList, false);
  } else {
    sourceControl.attachEvent("onblur", clearSuggestList);
  }
}
function dyn_init(source, dest) {
  sourceControl = source;
  destControl = dest;
  setStyle(destControl);
  clearSuggestList();
  if (sourceControl.addEventListener) {
    sourceControl.addEventListener("blur", clearSuggestList, false);
  } else {
    sourceControl.attachEvent("onblur", clearSuggestList);
  }
}
function setStyle(dest) {
  dest.style.backgroundColor = "#FFFFFF";
  dest.style.textAlign = "left";
  dest.style.border = "1px";
  dest.style.borderStyle = "solid";
  dest.style.borderColor = "#000000";
  dest.style.display = "none";
  dest.style.position = "absolute";
  dest.style.zIndex = "1";
  dest.style.top =
    getElementHeight(sourceControl) + getElementTop(sourceControl) + "px";
  dest.style.left = getElementLeft(sourceControl) + "px";
  dest.style.width = "300px";
}

function makeAjaxRequest(
  method,
  queryString,
  url,
  event,
  requestHandlerMethod
) {
  var keynum;
  if (window.event) {
    keynum = event.keyCode;
  } else if (event.which) {
    keynum = event.which;
  }
  if (keynum == 9) {
    sourceControl.blur();
    return true;
  }
  if (keynum != 40 && keynum != 38 && keynum != 13 && keynum != 27) {
    if (sourceControl.value == "") {
      clearSuggestList();
    } else {
      var req = getAjaxObject();
      var fieldValue = sourceControl.value;
      req.onreadystatechange = getReadyStateHandler(req, requestHandlerMethod);
      req.open(method, url, true);
      req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      req.send(queryString);
    }
  }
}

function isNavigation(event) {
  var keynum;
  if (window.event) {
    keynum = event.keyCode;
  } else if (event.which) {
    keynum = event.which;
  }
  if (keynum != 40 && keynum != 38 && keynum != 13 && keynum != 9) {
    return true;
  }
  return false;
}
function addItemToList(index, itemList, setIndex) {
  var elementId;
  var alignment = "left";
  suggestList = itemList;
  selectIndex = setIndex;
  var division = Math.ceil(100 / suggestList.length);
  var suggest =
    '<table onmouseover="javascript:suggestOver(' + index + ', this);" ';
  suggest += 'onmouseout="javascript:suggestOut();" ';
  suggest +=
    'onclick="javascript:setSourceValue(' + index + ", this.innerHTML); ";
  suggest +=
    'javascript:clearSuggestList();" class="suggest_link" width="100%"><tr>';
  for (i = 0; i < suggestList.length; i++) {
    if (i == selectIndex) {
      elementId = index;
      alignment = "left";
    } else {
      elementId = suggestList[i] + index;
      alignment = "right";
    }
    suggest +=
      '<td id="ele' +
      elementId +
      '" align="' +
      alignment +
      '" width="' +
      division +
      '%"  style="font-size:12px">' +
      suggestList[i] +
      "</td>";
  }
  suggest += "</tr></table>";
  destControl.innerHTML += suggest;
}
function getElementTop(element) {
  var targetTop = 0;
  if (element.offsetParent) {
    while (element.offsetParent) {
      targetTop += element.offsetTop;
      element = element.offsetParent;
    }
  } else if (element.y) {
    targetTop += element.y;
  }
  return targetTop;
}

function getElementLeft(element) {
  var targetLeft = 0;
  if (element.offsetParent) {
    while (element.offsetParent) {
      targetLeft += element.offsetLeft;
      element = element.offsetParent;
    }
  } else if (element.x) {
    targetLeft += element.x;
  }
  return targetLeft;
}

function getElementHeight(element) {
  var targetHeight = 0;
  if (element.offsetParent) {
    targetHeight += element.offsetHeight;
  }
  return targetHeight;
}

function getElementWidth(element) {
  var targetWidth = 0;
  if (element.offsetParent) {
    targetWidth += element.offsetWidth;
  }
  return targetWidth;
}

function clearSuggestList() {
  destControl.innerHTML = "";
  hideList();
}

function hideList() {
  destControl.style.display = "none";
}

function showList() {
  destControl.style.display = "";
}

function getCursor() {
  if (destControl.innerHTML.length == 0) {
    return -1;
  }
  var parent = destControl;
  for (var i = 0; i < parent.childNodes.length; i++) {
    if (parent.childNodes[i].className == "suggest_link_over") {
      return i;
    }
  }
  return parent.childNodes.length;
}

function handleArrowKeys(event) {
  var keynum;
  var cursor;
  var parent;
  if (window.event) {
    keynum = event.keyCode;
  } else if (event.which) {
    keynum = event.which;
  }
  if (keynum == 13 || keynum == 9 || keynum == 27) {
    clearSuggestList();
    return false;
  } else {
    if (sourceControl.value != "" && (keynum == 40 || keynum == 38)) {
      cursor = getCursor();
      parent = destControl;
      if (keynum == 40) {
        if (cursor == parent.childNodes.length) {
          suggestOver(0, parent.childNodes[0]);
        } else if (cursor < parent.childNodes.length - 1) {
          suggestOut();
          suggestOver(cursor + 1, parent.childNodes[cursor + 1]);
        }
      } else {
        if (cursor > 0) {
          suggestOut();
          suggestOver(cursor - 1, parent.childNodes[cursor - 1]);
        }
      }
    }
  }
  return true;
}

function suggestOver(index, div_value) {
  div_value.className = "suggest_link_over";
  setSourceValue(index);
}

function suggestOut() {
  var parent = destControl;
  for (i = 0; i < parent.childNodes.length; i++) {
    parent.childNodes[i].className = "suggest_link";
  }
}

function setSourceValue(index) {
  var selectedVal = document.getElementById("ele" + index);
  sourceControl.value = selectedVal.innerHTML;
}

/*.........These functions are for SXP Portal.................................................*/
function makeAjaxRequest2(method, queryString, url, requestHandlerMethod) {
  var req = getAjaxObject();
  req.onreadystatechange = getReadyStateHandler2(req, requestHandlerMethod);
  req.open(method, url, true);
  req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  req.send(queryString);
}

function getReadyStateHandler2(req, responseXmlHandler) {
  try {
    // Return an anonymous function that listens to the XMLHttpRequest instance
    return function () {
      // If the request is completed successfully.
      if (req.readyState == 4) {
        // Check whether we have received a successful response from the server
        if (req.status == 200) {
          // Pass the XML payload of the response to the handler function.
          responseXmlHandler(req.response);
        } else {
          // An HTTP problem has occurred
          consol.log("Status code - " + req.status);
        }
      }
    };
  } catch (e) {
    consol.error("Issue in getReadyStateHandler2 function - " + e);
  }
}
/*............................................................................................*/
