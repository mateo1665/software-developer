spelerslijst = ['Modric','zidane','ronaldo b','ronaldo','suker','ibrahimovic','ronaldinho','messi','neymar','lewandowski']
spelerslijst = shuffle(spelerslijst);
function shuffle(array) {
    let currentindex = array.length, randomindex;
    
    while(currentindex != 0) {

        randomindex = math.floor(math.random() * currentindex);
        currentindex--;

        [array[currentindex], array[randomindex]] = [array[randomindex], array[currentindex]];
    }


    return array;
}