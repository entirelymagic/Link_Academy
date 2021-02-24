var money = 5;
var chocolates = 0;
var chocolatePrice =1;


while (money > chocolatePrice) {
    chocolates++;
    money -= chocolatePrice;
}

document.write("I have " + chocolates + "chocolates");