function check(form) {
    if(form.id.value==""&&form.password.value=="") {
        window.open('target.html')
    } else {
        alert("Error ID or Password")
    }
}