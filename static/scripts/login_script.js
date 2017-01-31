function submit(){
    var location = document.getElementById("location");
    var user = document.getElementById("userid");
    var pwd = document.getElementById("pwd");
    var location = document.getElementById("location")
    var location_label = document.getElementById("location_label")
    location_label.setValue(location.value)


    if(user.value == 'sumangala' )
    {
        if(pwd.value == 'yelamma45') {
            window.alert("You are loggen in successfully !!" + user.value);
            window.open("http://www.google.co.in")
        }
        else
            window.alert("Incorrect Password" + user.value);
    }
    else{
        window.alert("Incorrect UserID" + user.value);
    }


}