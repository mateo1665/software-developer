const fotos = [
    "braziliaanse_ronaldo.png.jpg",
    "messi.png.jpg",
    "ronaldo.png.jpg",
    "ibrahimovic.png.jpg",
    "neymar.png.jpg",
    "lewandowski.png.jpg",
    "suker.png.jpg",
    "zidane.png.jpg",
    "modric.png.jpg",
    "ronaldinho.png.jpg",
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
const div_fotos = document.getElementById("fotos");

for(let i = 0; i < fotos.length; i++) {
    let img = document.createElement("img");
    img.src = fotos[i];
    div_fotos.appendChild(img);
}

for(let i = 0; i < spelerslijst.length; i++) {
    let img = document.createElement("img");
    img.src = spelerslijst[i];
    div_fotos.appendChild(img);
}