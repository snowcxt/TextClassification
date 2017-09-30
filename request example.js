var data = `Does anyone know what the domestic content is of any of these:
Geo Prizm, Eagle Talon, Ford Probe?

All are made in the US, but I have been told they contain mostly
foreign parts.  Please follow up directly to me, I'll post the
findings to the net if there is interest.`;

var xhr = new XMLHttpRequest();

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "http://localhost:8000/predict/");

xhr.send(data);