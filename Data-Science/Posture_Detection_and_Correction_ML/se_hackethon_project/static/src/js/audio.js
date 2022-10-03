let audioContext, osc, lfo;
var x;

function init_sound() {
	try {
		// window.AudioContext = window.AudioContext || window.webkitAudioContext;
		// audioContext = new AudioContext();
		//
		// var real = new Float32Array([ 0, 0.4, 0.4, 1, 1, 1, 0.3, 0.7, 0.6, 0.5, 0.9, 0.8 ]);
		// var imag = new Float32Array(real.length);
		// var hornTable = audioContext.createPeriodicWave(real, imag);
		//
		// osc = audioContext.createOscillator();
		// osc.type = 'square';
		// osc.setPeriodicWave(hornTable);
		// osc.frequency.value = 100;
		// osc.connect(audioContext.destination);
		// osc.start();
		x = document.getElementById("myAudio");

		// function playAudio() {
		//   x.play();
		// }
		//
		// function pauseAudio() {
		//   x.pause();
		// }
	} catch (e) {
		console.log(e);
		alert('Web Audio API is not supported in this browser');
	}
}

function start_alarm() {
	try {
		// if (osc != undefined) {
		// 	osc.connect(audioContext.destination);
		// }
		if(x!=undefined) {
				x.play();
		}
	} catch (e) {}
}

function stop_alarm() {
	try {
		// if (osc != undefined) {
		// 	osc.disconnect(audioContext.destination);
		// }
		if(x!=undefined) {
				x.pause();
		}
	} catch (e) {}
}
