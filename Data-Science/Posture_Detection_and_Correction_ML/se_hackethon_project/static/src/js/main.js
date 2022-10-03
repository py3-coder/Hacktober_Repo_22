'use strict';

let timeThreshold = 300; // time in ms
let startAlgo = false;
let lastClosedTime,continuous = false;
let body = document.querySelector('body');
let message;
let x1=0;
let x2=0;
let x3=0;
let x4=0;
var let1 = document.getElementById("l1");
var let2 = document.getElementById("l2");
var let3 = document.getElementById("l3");
var let4 = document.getElementById("l4");


function main() {
	JEEFACETRANSFERAPI.init({
		canvasId: 'canvas',
		NNCpath: 'static/assets/model/',
		callbackReady: function(errCode) {
			if (errCode) {
				console.log('ERROR - cannot init JEEFACETRANSFERAPI. errCode =', errCode);
				errorCallback(errCode);
				return;
			}
			console.log('INFO : JEEFACETRANSFERAPI is ready !!!');
			successCallback();
		} //end callbackReady()
	});
} //end main()

function successCallback() {
	nextFrame();
	document.getElementById('full-page-loader').style.display = 'none';
	body = document.querySelector('body');
	message = document.querySelector('#message');
}

function errorCallback(errorCode) {

}

function nextFrame() {
	if (!startAlgo) {
		return;
	}
	let deltaTime = Date.now() - lastClosedTime;
	if (deltaTime > timeThreshold && continuous) {
		start_alarm();
		// console.log("Alarm Called");
		body.style.background = '#f00';
	} else {
		stop_alarm();
		body.style.background = '#fff';
	}

	if (JEEFACETRANSFERAPI.is_detected()) {
		let rotation = JEEFACETRANSFERAPI.get_rotationStabilized();
		let isHeadPostureOk = isHeadPostureOK(rotation);
		let positionScaleZ = JEEFACETRANSFERAPI.get_positionScale()[2];
		let screenDistanceOK = isScreenDistanceOK(positionScaleZ);

		if (!isHeadPostureOk[0] || !isHeadPostureOk[1] || !isHeadPostureOk[2] || !screenDistanceOK) {
			if (lastClosedTime === undefined || !continuous) lastClosedTime = Date.now(); // Now is the new time
			continuous = true;
			if (message) {
				let messageContent = '';
				if (!screenDistanceOK) {
					x1++;
					var b = '<p>Getting too close to the Screen!!!</p>';
					messageContent += b;
					console.log(x1);
					let1.value = x1;
				}
				if (!isHeadPostureOk[0]) {
					x2++;
					var c = '<p>Head is either too up or too down.</p>';
					messageContent += c;
					console.log(x2);
					let2.value = x2;
				}
				if (!isHeadPostureOk[1]) {
					x3++;
					var d = '<p>Head is turned too much.</p>';
					messageContent += d;
					console.log(x3);
					let3.value = x3;
				}
				if (!isHeadPostureOk[2]) {
					x4++;
					var e = '<p>Head is bend towards shoulders.</p>';
					messageContent += e;
					console.log(x4);
					let4.value = x4;
				}
				message.innerHTML = messageContent;
			}
		} else {
			if (message) {
				message.innerHTML = '';
			}
			continuous = false;
		}
		console.log('Detected and Face Recpognition On');
	} else {
		console.log('Face Not detected');
	}
	requestAnimationFrame(nextFrame);
}

function start() {
	init_sound();
	startAlgo = true;
	nextFrame();
	document.getElementById('warnings').style.display = 'none';
}

// function graph() {
// 	console.log(x1);
// 	console.log(x2);
// 	console.log(x3);
// 	console.log(x4);
// 	let1.value = x1;
// 	let2.value = x2;
// 	let3.value = x3;
// 	let4.value = x4;
// }
