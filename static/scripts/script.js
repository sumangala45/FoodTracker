function initAutocomplete() {
        // Create the autocomplete object, restricting the search to geographical
        // location types.
        autocomplete = new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
            {types: ['geocode']});

        // When the user selects an address from the dropdown, populate the address
        // fields in the form.
        autocomplete.addListener('place_changed', fillInAddress);
}

function fillInAddress() {
    // Get the place details from the autocomplete object.
    var place = autocomplete.getPlace();

    for (var component in componentForm) {
      document.getElementById(component).value = '';
      document.getElementById(component).disabled = false;
    }

    // Get each component of the address from the place details
    // and fill the corresponding field on the form.
    for (var i = 0; i < place.address_components.length; i++) {
      var addressType = place.address_components[i].types[0];
      if (componentForm[addressType]) {
        var val = place.address_components[i][componentForm[addressType]];
        document.getElementById(addressType).value = val;
      }
    }
  }

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
      if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function (position) {
              var geolocation = {
                  lat: position.coords.latitude,
                  lng: position.coords.longitude
              };
              var circle = new google.maps.Circle({
                  center: geolocation,
                  radius: position.coords.accuracy
              });
              autocomplete.setBounds(circle.getBounds());
          });
      }
  }
      

function reset(){
    var name = document.getElementById("name");
    var mailid = document.getElementById("mailid");
    var userid = document.getElementById("userid");
    var pwd = document.getElementById("pwd");
    var rpwd = document.getElementById("rpwd");
    var contact = document.getElementById("contact");
    var desp = document.getElementById("desp");
    var autocomplete = document.getElementById("autocomplete");
    name.value = "";
    mailid.value = "";
    userid.value = "";
    pwd.value = "";
    rpwd.value = "";
    contact.value = "";
    desp.value = "";
    autocomplete.value = "";

}

function register_to_db(){
    var name = document.getElementById("name");
    var mailid = document.getElementById("mailid");
    var userid = document.getElementById("userid");
    var pwd = document.getElementById("pwd");
    var rpwd = document.getElementById("rpwd");
    var contact = document.getElementById("contact");
    var desp = document.getElementById("desp");
    var autocomplete = document.getElementById("autocomplete");

}

// function submit(){
//     var location = document.getElementById("location");
//     var user = document.getElementById("userid");
//     var pwd = document.getElementById("pwd");
//     var location = document.getElementById("location")
//     var location_label = document.getElementById("location_label")
//     location_label.setValue(location.value)
//
//
//     if(user.value == 'sumangala' )
//     {
//         if(pwd.value == 'yelamma45') {
//             window.alert("You are loggen in successfully !!" + user.value);
//             window.open("http://www.google.co.in")
//         }
//         else
//             window.alert("Incorrect Password" + user.value);
//     }
//     else{
//         window.alert("Incorrect UserID" + user.value);
//     }
//
//
// }