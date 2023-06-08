const fotos = [
    "braziliaanse_ronaldo.png",
    "messi.png",
    "ronaldo.png",
    "ibrahimovic.png",
    "neymar.png",
    "lewandowski.png",
    "suker.png",
    "zidane.png",
    "modric.png",
    "ronaldinho.png",
];


function shuffle(fotos){
    let currentindex = fotos.length, randomindex;

    while(currentindex != 0) {

        randomindex = Math.floor(Math.random() * currentindex);
        currentindex--;

        [fotos[currentindex], fotos[randomindex]] = [fotos[randomindex], fotos[currentindex]];
    }

    return fotos;
}

var spelerslijst = shuffle(fotos);
div_fotos = document.getElementById("fotos");


for(let i = 0; i < fotos.length; i++) {
    div_fotos.appendChild(fotos);
}