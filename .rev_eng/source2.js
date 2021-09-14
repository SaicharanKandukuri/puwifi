var liveReqTimeInJS = 180;
var redirectDelayInSec = 0.25;
var LOGGED_IN = "LIVE";
var LOGGED_OUT = "LOGIN";
var CHALLENGE = "CHALLENGE";
var States = {
  SIGNED_IN: "signed_in",
  SIGNED_OUT: "signed_out",
  WAITING: "waiting",
  REJECTED: "rejected",
};
var Live = { ACK: "ack", NACK: "nack", OFF: "live_off", AGAIN: "login_again" };
var Client = { WEB: "0", IOS: "1", ANDROID: "2" };
var RedirectURL = { IOS: "http://ios.cyberoam.com/app/s.html" };
Object.freeze(States);
Object.freeze(Live);
Object.freeze(Client);
Object.freeze(RedirectURL);
var loginstate = null;
var producttype = Client.WEB;
var timer = "";
var finalRedirectUrl = "";
var userAgent = navigator.customUserAgent || navigator.userAgent;
window.onbeforeunload = function () {
  if (
    preserveCaptivePortal != "N" &&
    keepaliverequest === "Y" &&
    getState() === States.SIGNED_IN &&
    !isClientHandheld()
  ) {
    var b =
      "mode=193&username=" +
      encodeURIComponent(document.getElementById("username").value) +
      "&a=" +
      new Date().getTime();
    var a =
      /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
    if (a) {
      sendBeaconForOnce(b, "logout.xml");
    } else {
      makeAjaxRequest("POST", b, "logout.xml", null, false);
    }
  }
};
var ViewRender = (function () {
  function a() {
    var c = document.getElementById("msgDiv");
    var e = document.getElementById("username").value;
    var d = document.getElementById("loginbtn");
    switch (this.state) {
      case States.SIGNED_IN:
        c.style.color = "green";
        c.innerHTML = this.message.replace(/{username}/g, e);
        d.value = logoutBtnCaption;
        break;
      case States.REJECTED:
        renderMessage(this.message, "red");
        d.value = loginBtnCaption;
        break;
      case States.SIGNED_OUT:
        c.innerHTML = "";
        renderMessage(this.message, "green");
        d.value = loginBtnCaption;
        break;
      default:
        break;
    }
  }
  function b() {
    var d = document.getElementById("signin-caption");
    var h = document.getElementById("credentials");
    var c = document.getElementById("loggedin-message");
    var g = document.getElementById("statusmessage");
    var e = document.getElementById("loginbutton");
    var f = document.getElementById("registerlink").children[0];
    removeSpinner();
    switch (this.state) {
      case States.SIGNED_IN:
        g.className = "unshown";
        h.className = "loggedin";
        c.className = "loggedin";
        e.innerText = logoutBtnCaption;
        f.style.display = "none";
        var i = document.getElementById("username").value;
        renderLoginMessage(this.message, i);
        break;
      case States.REJECTED:
        d.innerText = title;
        renderMessage(this.message, "red");
        h.className = "loggedout shake";
        e.innerText = loginBtnCaption;
        setTimeout(function () {
          if (h.className === "loggedout shake") {
            h.className = "loggedout";
          }
        }, 500);
        break;
      case States.SIGNED_OUT:
        h.className = "loggedout";
        c.className = "loggedout";
        d.innerText = title;
        e.innerText = loginBtnCaption;
        f.style.display = guestUserRes === 1 ? "block" : "none";
        renderMessage(this.message, "green");
        document.title = title;
        document.getElementById("password").value = "";
        break;
      case States.WAITING:
        g.className = "unshown";
        h.className = "loggedin";
        c.className = "loggedin";
        d.innerText = signingIn;
        e.innerText = loginBtnCaption;
        renderSpinner();
        break;
      default:
        break;
    }
  }
  return {
    init: function (d, c) {
      this.state = d;
      this.message = typeof c == "undefined" ? "" : c;
      this.render = enablefullcustomization === "1" ? a : b;
      return this;
    },
  };
})();
function submitRequest() {
  var c;
  var a = getState();
  if (a != States.SIGNED_IN && validateLogin()) {
    var b = replaceAll(document.getElementById("username").value, "'", "''");
    c =
      "mode=191&username=" +
      encodeURIComponent(b) +
      "&password=" +
      encodeURIComponent(document.getElementById("password").value) +
      "&a=" +
      new Date().getTime() +
      "&producttype=" +
      producttype;
    if (loginstate) {
      c += "&state=" + loginstate;
    }
    ViewRender.init(States.WAITING).render();
    makeAjaxRequest("POST", c, "login.xml", loginResponseHandler);
  } else {
    if (a === States.SIGNED_IN) {
      c =
        "mode=193&username=" +
        encodeURIComponent(document.getElementById("username").value) +
        "&a=" +
        new Date().getTime() +
        "&producttype=" +
        producttype;
      makeAjaxRequest("POST", c, "logout.xml", logoutResponseHandler);
    }
  }
}
function validateLogin() {
  var b = false;
  var a = "";
  if (
    document.getElementById("username").value.replace(/ /g, "").length === 0
  ) {
    a = enterUsername;
    document.getElementById("username").focus();
  } else {
    if (document.getElementById("password").value.length === 0) {
      a = enterPassword;
      document.getElementById("password").focus();
    } else {
      b = true;
    }
  }
  renderMessage(a, "red");
  return b;
}
function initializeField(d, b, a) {
  var c = document.getElementById(d);
  if (c && b && typeof a === "string") {
    c.setAttribute(b, a);
    c[b] = a;
  }
}
function setup() {
  document.title = title;
  if (
    navigator.userAgent.match(/iPhone/i) ||
    navigator.userAgent.match(/iPad/i)
  ) {
    producttype = Client.IOS;
  } else {
    if (navigator.userAgent.match(/android/i)) {
      producttype = Client.ANDROID;
    }
  }
  if (enablefullcustomization === "1") {
    renderLoginBox();
  }
  var d = document.getElementById("logo");
  if (d) {
    var f = d.children[0];
    if (f) {
      var c = f.getAttribute("href");
      if (c.indexOf("http") === -1) {
        f.setAttribute("href", "http://" + c);
      }
    }
  }
  var b = location.host.substring(0, location.host.lastIndexOf(":"));
  var e =
    "https://" +
    b +
    ":" +
    userportalport +
    "/userportal/webpages/myaccount/login.jsp";
  var a = document.getElementById("myaccountcaption");
  a.setAttribute("href", e);
  a.setAttribute("target", "_blank");
  initializeField("username", "placeholder", usernameCaption);
  initializeField("password", "placeholder", passwordCaption);
  initializeField("registercaption", "text", registerCaption);
  initializeField("myaccountcaption", "text", myaccountCaption);
  initializeField("loginbutton", "innerText", loginBtnCaption);
  initializeField("signin-caption", "innerText", title);
  initializeField("donotclosepage", "innerText", doNotClosePage);
  initializeField("willbesignedout", "innerText", willBeSignedOut);
  setListeners();
}
function setListeners() {
  addOnclick(document.getElementById("registerlink"), function () {
    var a =
      document.URL.split("8090")[0] +
      "8090/webconsole/webpages/guestportal/GuestUserEdit.jsp";
    a = a.replace(/^http:\/\//i, "https://");
    openRegisterWindow(a);
  });
  addOnclick(document.getElementById("logo"), function () {
    var a = document.getElementById("logo").children[0];
    if (a) {
      window.open(a.getAttribute("href"));
    }
  });
  document.addEventListener("keydown", function (a) {
    switch (a.keyCode) {
      case 13:
        if (enablefullcustomization === "0") {
          document.getElementById("loginbutton").parentNode.click();
          a.preventDefault();
        }
        break;
      case 116:
        a.preventDefault();
        break;
    }
  });
}
function openRegisterWindow(d) {
  var a = (window.screen.width - 750) / 2;
  var e = (window.screen.height - 500) / 2;
  var b =
    "status=yes, height=450,width=650,resizable=no,left=" +
    a +
    ",top=" +
    e +
    ",screenX=" +
    a +
    ",screenY=" +
    e +
    ",scrollbars=no";
  var c =
    typeof window.opener != "undefined" &&
    navigator.userAgent.indexOf("MSIE") != -1
      ? window.opener.open(d, "registerLink", b)
      : window.open(d, "registerLink", b);
  c.focus();
}
function getState() {
  return enablefullcustomization === "1" ? getStateCustom() : getStateDefault();
}
function getStateCustom() {
  var b = "";
  var a = document.getElementById("msgDiv");
  if (a.innerHTML.length === 0) {
    b = States.SIGNED_OUT;
  } else {
    if (a.style.color === "red") {
      b = States.REJECTED;
    } else {
      b = States.SIGNED_IN;
    }
  }
  return b;
}
function getStateDefault() {
  var a = "";
  if (document.getElementById("statusmessage").className.indexOf("red") != -1) {
    a = States.REJECTED;
  } else {
    if (
      document.getElementById("credentials").className.indexOf("loggedout") !=
      -1
    ) {
      a = States.SIGNED_OUT;
    } else {
      if (document.getElementById("spinner-view").style.display === "block") {
        a = States.WAITING;
      } else {
        a = States.SIGNED_IN;
      }
    }
  }
  return a;
}
function getTagValue(c, a) {
  var b = c.getElementsByTagName(a);
  return b && b.length > 0 ? b[0].firstChild.nodeValue : undefined;
}
function isClientAndroid() {
  return producttype === Client.ANDROID;
}
function isClientIOS() {
  return (
    producttype === Client.IOS &&
    userAgent.match(/mozilla/i) &&
    userAgent.match(/applewebkit/i) &&
    userAgent.match(/mobile/i) &&
    !userAgent.match(/safari/i)
  );
}
function isClientHandheld() {
  return isClientAndroid() || isClientIOS();
}
function loginResponseHandler(d) {
  var c = "";
  var b = d.documentElement;
  var a = getTagValue(b, "status");
  loginstate = a == CHALLENGE ? getTagValue(b, "state") : null;
  if (a === LOGGED_IN) {
    if (isClientIOS()) {
      handleIOSRedirect();
    } else {
      if (displayWebpage === "1") {
        if (isClientAndroid()) {
          handleAndroidRedirect();
        } else {
          handleBrowserRedirect();
        }
      }
    }
    c = States.SIGNED_IN;
  } else {
    if (a === LOGGED_OUT) {
      c = States.REJECTED;
    }
  }
  ViewRender.init(c, getTagValue(b, "message")).render();
  setTimeForLiveRequest(liveReqTimeInJS);
}
function logoutResponseHandler(c) {
  var b = c.documentElement;
  var a = getTagValue(b, "status");
  if (a === LOGGED_OUT) {
    clearTimeout(timer);
    ViewRender.init(States.SIGNED_OUT, getTagValue(b, "message")).render();
  }
}
function getRedirectUrl() {
  if (location.href.indexOf("u=") != -1) {
    return location.href.substring(location.href.indexOf("u=") + 2);
  }
  if (redirectTo) {
    if (redirectTo.indexOf("http") === -1) {
      redirectTo = "http://" + redirectTo;
    }
    return redirectTo;
  }
  return "";
}
function redirectToFinalUrl() {
  location.href = finalRedirectUrl;
}
function handleIOSRedirect() {
  finalRedirectUrl = RedirectURL.IOS;
  redirectToFinalUrl();
}
function handleAndroidRedirect() {
  finalRedirectUrl = getRedirectUrl();
  redirectToFinalUrl();
}
function handleBrowserRedirect() {
  finalRedirectUrl = getRedirectUrl();
  setTimeout(function () {
    if (preserveCaptivePortal === "Y") {
      window.open(finalRedirectUrl);
    } else {
      redirectToFinalUrl();
    }
  }, redirectDelayInSec * 1000);
}
function renderLoginMessage(c, d) {
  var a = document.getElementById("signin-caption");
  var b = c.replace(/{username}/g, d);
  a.innerText = b;
  document.title = b;
}
function renderMessage(c, a) {
  var b = document.getElementById("statusmessage");
  if (enablefullcustomization === "1") {
    b.style.color = a;
    b.style.marginTop = "10px";
  } else {
    b.className = a;
  }
  b.innerHTML = c;
}
function renderSpinner() {
  document.getElementById("loggedin-view").style.display = "none";
  document.getElementById("spinner-view").style.display = "block";
}
function removeSpinner() {
  document.getElementById("loggedin-view").style.display = "block";
  document.getElementById("spinner-view").style.display = "none";
}
function getQueryString(a) {
  return Object.keys(a)
    .map(function (b) {
      return b + "=" + a[b];
    })
    .join("&");
}
function sendLiveRequest() {
  var a = {
    mode: "192",
    username: encodeURIComponent(document.getElementById("username").value),
    a: new Date().getTime(),
    producttype: producttype,
  };
  invokeAjaxURL("live?" + getQueryString(a), "get");
}
function setTimeForLiveRequest(a) {
  clearTimeout(timer);
  if (a != -1) {
    timer = setTimeout(sendLiveRequest, a * 1000);
  }
}
function parseXML(c) {
  if (!c) {
    setTimeForLiveRequest(liveReqTimeInJS);
    return;
  }
  var a = c.documentElement;
  var d = "";
  try {
    d = getTagValue(a, "ack");
    if (d == Live.ACK) {
      setTimeForLiveRequest(liveReqTimeInJS);
    } else {
      if (d == Live.NACK || d == Live.AGAIN) {
        clearTimeout(timer);
        ViewRender.init(States.SIGNED_OUT).render();
      } else {
        if (d == Live.OFF) {
        }
      }
    }
  } catch (b) {}
}
function renderLoginBox() {
  var d = createElement("div", { id: "msgDiv" }, []);
  var c = createElement("div", { id: "credentials", style: "margin:15px;" }, [
    createElement("input", {
      id: "username",
      placeholder: usernameCaption,
      type: "text",
    }),
    createElement("input", {
      id: "password",
      placeholder: passwordCaption,
      type: "password",
    }),
    createElement("input", {
      id: "loginbtn",
      type: "button",
      value: loginBtnCaption,
      onclick: "submitRequest()",
    }),
    createElement("div", { class: "statusmessagerow" }, [
      createElement("div", { id: "statusmessage", class: "unshown" }),
    ]),
  ]);
  var b = createElement("ul", { id: "links" }, [
    createElement("li", { id: "userportallink" }, [
      createElement(
        "a",
        {
          id: "myaccountcaption",
          style: "display:" + (myAccountLink === "1" ? "block;" : "none;"),
          href: "#",
        },
        myaccountCaption
      ),
    ]),
    createElement("li", { id: "registerlink" }, [
      createElement(
        "a",
        {
          id: "registercaption",
          style: "display:" + (guestUserRes === "1" ? "block;" : "none;"),
          href: "#",
        },
        registerCaption
      ),
    ]),
  ]);
  var a = document.getElementById("__loginbox");
  a.appendChild(d);
  a.appendChild(c);
  a.appendChild(b);
}
function createElement(a, b, d) {
  var c = document.createElement(a);
  Object.keys(b).forEach(function (e) {
    c.setAttribute(e, b[e]);
  });
  if (typeof d === "string") {
    c.appendChild(document.createTextNode(d));
  } else {
    if (Array.isArray(d)) {
      d.forEach(function (e) {
        c.appendChild(e);
      });
    }
  }
  return c;
}
function addOnclick(a, b) {
  if (a) {
    a.onclick = b;
  }
}
function replaceAll(c, d, b) {
  var a = 0;
  while ((a = c.indexOf(d, a)) > -1) {
    c = c.substring(0, a) + b + c.substring(a + 1);
    a = a + b.length;
  }
  return c;
}
function sendBeaconForOnce(d, b) {
  try {
    var a = new Blob([d], { type: "application/x-www-form-urlencoded" });
    navigator.sendBeacon(b, a);
    intentionalBlockingWait(650);
  } catch (c) {
    ViewRender.init(States.SIGNED_IN).render();
  }
}
function intentionalBlockingWait(c) {
  var b = new Date().getTime();
  var a = null;
  while (true) {
    a = new Date().getTime();
    if (a - b >= c) {
      return;
    }
  }
}
function makeAjaxRequest(i, h, a, g, b) {
  function f() {
    ViewRender.init(
      a === "logout.xml" ? States.SIGNED_IN : States.SIGNED_OUT
    ).render();
  }
  var c = getAjaxObject();
  c.addEventListener("error", f);
  if (g) {
    c.onreadystatechange = getReadyStateHandler(c, g);
  }
  try {
    c.open(i, a, typeof b === "undefined" ? true : b);
    c.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    c.send(h);
  } catch (d) {
    f();
  }
}
function removeOverlay() {}
