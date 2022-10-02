// let rock = 0;
// let scissor = 1;
// let paper = 2;
let array = ['✊', '✌', '🤚']
let score = 0;
let hand = document.getElementById('hands')
let playerScore = document.getElementById('player-score')
let endGame =  document.getElementById('endGameButton')
// 🤖
const computerChoice = () => {
    const randomChoice = Math.floor(Math.random()*3)
    return randomChoice
}
const playerChoice = (pChoice) => {
    let computer = computerChoice()
    if(pChoice==computer){
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${score}`
        return 

    }
    else if (pChoice==1 && computer==2) {
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${++score}`
        return
    }
    else if (pChoice==1 && computer==0) {
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${--score}`
        return
    }
    else if (pChoice==2 && computer==0) {
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${++score}`
        return
    }
    else if (pChoice==2 && computer==1) {
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${--score}`
        return

    }
    else if (pChoice==0 && computer==1) {
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${++score}`
        return
    }
    else if (pChoice==0 && computer==2) {
        hand.innerHTML = `🧑 : ${array[pChoice]} vs 🤖 : ${array[computer]} `
        playerScore.innerText = `Score : ${--score}`
        return
    }

}
endGame.onclick = () => {
    score = 0
    hand.innerHTML = ''
    playerScore.innerText = ' '
}
