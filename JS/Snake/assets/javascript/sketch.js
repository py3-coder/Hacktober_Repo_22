let end = document.getElementById("end");
let welcome = document.getElementById("welcome");
let restart = document.getElementById("restart");
let snake;
let res = 20;   //resolution
let food;
let w;
let h;

function setup() {
    createCanvas(400, 400);
    w = floor(width / res);
    h = floor(height / res);
    frameRate(5);
    snake = new Snake();
    foodLocation();
}

function foodLocation() {
    let x = floor(random(w));
    let y = floor(random(h));
    food = createVector(x, y);
}

function keyPressed() {
    if (keyCode === LEFT_ARROW)
        snake.setDir(-1, 0);
    else if (keyCode === RIGHT_ARROW)
        snake.setDir(1, 0);
    else if (keyCode === DOWN_ARROW)
        snake.setDir(0, 1);
    else if (keyCode === UP_ARROW)
        snake.setDir(0, -1);
}

function draw() {
    scale(res);
    background(220);
    if (snake.eat(food))
        foodLocation();
    snake.update();
    snake.show();

    if (snake.endGame()) {
        welcome.style.display = "none";
        end.innerHTML += `<h1>The game has ended!</h1>`;
        restart.style.display = "block";
        background(255, 0, 0);
        noLoop();
    }

    noStroke();
    fill(0, 255, 0);
    rect(food.x, food.y, 1, 1);
} 