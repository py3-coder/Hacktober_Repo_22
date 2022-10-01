const max = (a, b) => (a > b ? a : b);
const min = (a, b) => (a < b ? a : b);

let mainImage = "./image.jpg";
let bgImage = "./bg.jpg";
let size = 500;

let container = document.querySelector(".container");
let cover = document.querySelector(".cover");
let imageDiv = document.querySelector(".image");
let img = document.querySelector("img");

container.style.backgroundImage = `url(${bgImage})`;
img.setAttribute("src", mainImage);

size = min(window.innerHeight, window.innerWidth) - 50;
container.style.height = `${size}px`;
container.style.width = `${size}px`;
cover.style.height = `${size}px`;
cover.style.width = `${size}px`;
imageDiv.style.height = `${size}px`;
imageDiv.style.width = `${size}px`;

const newImg = new Image();
newImg.src = mainImage;
newImg.onload = () => {
	let w = newImg.naturalWidth;
	let h = newImg.naturalHeight;
	if (w > h) {
		img.style.width = "100%";
		img.style.height = "auto";
	} else {
		img.style.height = "100%";
		img.style.width = "auto";
	}
};
