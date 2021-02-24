let date = new Date()

let hour = date.getHours()


if (hour < 11) {
    document.write("Good Morning!")
} else if ( hour <18){
    document.write("Good Day!")
}  else {
    document.write("Good Afternoon!")
}