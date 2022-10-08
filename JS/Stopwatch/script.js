//get all the required elements
let sec=ms=min=hr='0'+0;
let started=false; //keeps track of whether timer is running or not
const start = document.getElementById('start-btn');
const stop = document.getElementById('stop-btn');
const reset = document.getElementById('reset-btn');

start.addEventListener('click',startFunc);
//on click function for start
 function startFunc(e){
    //managing the css
    start.classList.add('active');
    start.classList.remove('hover');
    e.preventDefault();
    //if not already running , start the timer
    if(!started){
        stop.classList.remove('active');
        stop.classList.add('hover');
        started=true;
    startTimer = setInterval(()=>{
        ms++;
        ms = ms<10?'0'+ms:ms;
    
        if(ms==100){
            sec++;
            ms=0;
            sec = sec<10?'0'+sec:sec;
        }
        if(sec==60){
            min++;
            sec=0;
            min = min<10?'0'+min:min;
        }
        if(min==60){
            hr++;
            min=0;
            hr = hr<10?'0'+hr:hr;
        }
    
        setTimer();
        },1);
        }
    
    }

// on click function for stop btn
stop.addEventListener('click',function(e){
    //managing css
    start.classList.remove('active');
    start.classList.add('hover');
    e.preventDefault();
    //if timer is presently running
    if(started){
        stop.classList.add('active');
        stop.classList.remove('hover');
        clearInterval(startTimer);
        started=false;
    }
    
    

})

reset.addEventListener('click',function(){
    //reset the whole timer
    start.classList.remove('active');
    start.classList.add('hover');
    stop.classList.remove('active');
    stop.classList.add('hover');
    clearInterval(startTimer);
    sec=ms=min=hr='0'+0;
    started=false;
    setTimer();
})

//display the variable values to page
function setTimer(){
    document.getElementById('hours').innerText = hr;
    document.getElementById('min').innerText = min;
    document.getElementById('sec').innerText = sec;
    document.getElementById('ms').innerText = ms;
}

