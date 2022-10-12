let myAns = {};
let QuestionNo = 0;
let data = [
  {
    correctAnswer: "Five Gold Rings",
    incorrectAnswers: [
      "Five Lords a Leaping",
      "Five Drummers Drumming",
      "Five Gold Rings",
      "Five Calling Birds",
    ],
    question:
      "According to the Christmas song what did my true love give to me on the fifth day of Christmas?",
  },
  {
    correctAnswer: "Bonsai",
    incorrectAnswers: ["Ornamental Shrubbery", "Decorage", "Topiary", "Bonsai"],
    question:
      "What is the name given to the art of miniaturising trees and maintaining their small size?",
  },
  {
    correctAnswer: "Washington DC",
    incorrectAnswers: ["Washington DC", "New York City", "Brussels", "Geneva"],
    question: "Where is Capitol Hill?",
  },
  {
    correctAnswer: "Gold",
    incorrectAnswers: ["Invisible", "Gold", "Dead", "Water"],
    question: 'What does the "touch of Midas" turn everything?',
  },
  {
    correctAnswer: "Apple",
    incorrectAnswers: ["Blackberry", "Microsoft", "Google", "Apple"],
    question:
      "Which computer company was set up by Steven Jobs and Stephen Wozniak?",
  },
  {
    correctAnswer: "Bravo",
    incorrectAnswers: ["Boot", "Bravo", "Ball", "Baby"],
    question:
      "What word is used in the NATO Phonetic Alphabet for the letter B?",
  },
  {
    correctAnswer: "Robots",
    incorrectAnswers: ["Robots", "Aliens", "Gods", "Wizards"],
    question: "Transformers are ___________ in disguise. ",
  },
  {
    correctAnswer: "Apple",
    incorrectAnswers: ["Microsoft", "Apple", "Google", "Linux"],
    question: "Who Make Macintosh Computers?",
  },
  {
    correctAnswer: "5 Gold Rings",
    incorrectAnswers: [
      "5 Drummers Drumming",
      "5 Gold Rings",
      "5 Swans a Swimming",
      "5 Lords a Leaping",
    ],
    question:
      'What Did My True Love Give To Me On The "Fifth" Day Of Christmas"?',
  },
  {
    correctAnswer: "Echo",
    incorrectAnswers: ["Echo", "Elton", "Elbow", "Enable"],
    question:
      "What word is used in the NATO Phonetic Alphabet for the letter E?",
  },
];

const next = () => {
  storeAns();
  if (QuestionNo < data.length-1) {
    ++QuestionNo;
    displayQuestion();
    console.log(QuestionNo);
  }
  if(QuestionNo==9){
    document.querySelector(".btn").style.display="none"
  }
};
const storeAns = () => {
  let radioBtn = document.getElementsByClassName("radioBtn");
  for (let i in radioBtn) {
    if (radioBtn[i].checked) {
      myAns = { ...myAns, [QuestionNo]: i };
      break;
    }
  }
  console.warn(myAns);
};

const displayQuestion = () => {
  console.log(data[QuestionNo]);
  document.querySelector(".que").innerHTML = `Q${QuestionNo + 1}. ${
    data[QuestionNo].question
  }`;
  let ans = data[QuestionNo]["incorrectAnswers"];
  let options = document.getElementsByClassName("option");
  let radioBtn = document.getElementsByClassName("radioBtn");

  for (let i in radioBtn) {
    options[i].innerHTML = data[QuestionNo].incorrectAnswers[i];
    radioBtn[i].checked = false;
  }

  console.log(ans);
};

const cal = () => {
  storeAns();
  let score = 0;
  for (let i = 0; i < data.length; i++) {
    if (i in myAns) {
      if (data[i].correctAnswer == data[i].incorrectAnswers[myAns[i]]) {
        score++;
      }
    }
  }
  let display=document.querySelector(".score")
  display.style.display="block"
  display.innerHTML=`Your Score is ${score} out of ${data.length}`
  document.querySelector(".container").style.display="none";
};
displayQuestion();