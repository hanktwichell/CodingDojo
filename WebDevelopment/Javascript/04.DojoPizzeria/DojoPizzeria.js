var toppings = [
    "Pepperoni",
    "Chicken",
    "Bacon",
    "Anchovies",
    "Peppers",
    "Veggies",
    "Mushrooms",
    "Olives",
    "Onions"
];
var crustType = [
    "Thin Crust",
    "Deep Dish",
    "Traditional",
    "Hand Tossed"
];
var sauceType = [
    "Red Sauce",
    "Traditional",
    "No Sauce"
];
var cheeses = [
    "Mozzerella",
    "Cheddar",
    "Feta"
];

function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var order1 = pizzaOven("deep dish", "traditional", ["mozzerella"], ["pepperoni", "sausage"]);
var order2 = pizzaOven("hand tossed", "marinara", ["mozzerella", "feta"], ["mushrooms", "olives", "onions"]);
var order3 = pizzaOven("hand tossed", "red sauce", ["mozzerella"], ["chicken", "bacon"]);
var order4 = pizzaOven("deep dish", "traditional", ["mozzerella", "feta"], ["pepperoni", "sausage", "olives"]);

function randomPizza() {
    var randomZa = {crustType, sauceType, cheeses, toppings};
    randomZa.crustType = crustType[Math.floor(Math.random() * crustType.length)];
    randomZa.sauceType = sauceType[Math.floor(Math.random() * sauceType.length)];
    randomZa.cheeses = [];
    randomZa.toppings = [];
    var chez = cheeses;
    var tops = toppings;
    for (var i=0; i<Math.random() * cheeses.length; i++)
    {
        var index = Math.floor(Math.random() * chez.length);
        randomZa.cheeses[i] = cheeses[index];
        chez.splice(index, 1);
    }
    for (var i=0; i<Math.random() * toppings.length; i++)
    {
        var index = Math.floor(Math.random() * tops.length);
        randomZa.toppings[i] = toppings[index];
        tops.splice(index, 1);
    }
    return randomZa;
}

console.log(randomPizza());
console.log(order1);
console.log(order2);
console.log(order3);
console.log(order4);
