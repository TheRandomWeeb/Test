console.log('Answer more than 69420 and type "You are welcum" to unlock the good ending')
function confirmPay(){
    return confirm(`Are you sure you want to pay SnailPi $${money}?`);
}


alert("SnailPi: WelCUM to CUMLAND");
let money = prompt("SnailPI: Tickets are $69420", "<Enter Money Here>");
if (money == 69420){
    var answer = confirmPay();
    if (answer == true){
        alert("Bruh");
    }
    else{
        prompt("SnailPi: BITCH YOU TRYNA SCAM ME?");
        alert("*SnailPi pulls out his quarter-incher*");
        alert("SnailPi: MEGA CUMBLAST");
    }
}
else if (money < 69420){
    function death(){
        prompt("SnailPi: BITCH YOU TRYNA SCAM ME?");
        alert("*SnailPi pulls out knife*");
        alert("*SnailPi shoves it up your ass*");
    }
    var answer = confirmPay();
    if (answer == true){
        death();
    }
    else{
        death();
    }
}
else if (money > 69420){
    function death(){
        alert("*SnailPi pulls out a gun*");
        alert(`SnailPi shoots you ${money - 69420} times`);
    }
    function next(){
        let secret = prompt(`SnailPi: Thank you for the $${money - 69420} tip`);
        if (secret == "You are welcum"){
            alert('You have unlocked the good ending');
            alert('SnailPi: SIKE');
            death();
        }
        else{
            death();
        }
    }
    var answer = confirmPay();
    if (answer==true){
        next();
    }
    else{
        prompt("SnailPi: BITCH YOU TRYNA SCAM ME?");
        alert("*SnailPi enters his car*");
        alert("*SnailPi runs you over*");
    }
}
else{
    prompt("SnailPi: THAT AINT NO MONEY BITCH");
    alert("*SnailPi grabs you by the neck*");
    alert("*SnailPi grabs you and yeets you into the road*");
    alert("*SnailPi gets in his car*");
    alert("*SnailPi runs you over*");
}