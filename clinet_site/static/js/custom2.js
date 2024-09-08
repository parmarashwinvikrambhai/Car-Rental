const form = document.getElementById("form");
const cardHolderName = document.getElementById("cardholdername");
const cardNumber = document.getElementById("cardnumber");

const ValidateValues = {
    cardholderName: false,
    cardholderNumber: false,
};



// submit the form when all details are correct
// form.addEventListener("submit", (e) => {
//   e.preventDefault();
//   if ( ValidateValues.cardholderName == true && ValidateValues.cardholderNumber == true)
//     {
//       const formObjectData = $(this).serializeArray();
//       const formData = {}

//       formObjectData.forEach( e => {
//         formData[e.name] = e.value
//       });

//       console.log(formData);
      
//     //   $.ajax({
//     //     type: "POST",
//     //     url: "/client/user_signup",
//     //     data: ValidateValues,
//     //     success: function (response) {
//     //       console.log("FormData: ", data);
//     //       alert("Registration Successfull!!!");
//     //     },
//     //     error: function(response){
//     //       alert("Something went wrong.");
//     //     }
//     //   });
//     } else {
//       console.log("Form is not Validateed");
//     }
// });


function checkCardHolderName(){

    const cardHolderNameValue = cardHolderName.value.trim();

    if(cardHolderNameValue === ""){
        setErrorFor(cardHolderName, "Card Holder Name cannot be blank");
    } else if (cardHolderNameValue.length < 20){
        setErrorFor(cardHolderName, "Card Holder Name should not be less than 20");
    } else {
        ValidateValues.cardholderName = true;
        setSuccessFor(cardHolderName);
    }
}

function checkCardNumber(){
    const cardNumberValue = cardNumber.value.trim();

    if(cardNumberValue === ""){
        setErrorFor(cardNumber, "Card Number cannot be blank");
    } else if (cardNumberValue.length < 16){
        setErrorFor(cardNumber, "Card Number should not be less than 16");
    } else {
        ValidateValues.cardholderNumber = true;
        setSuccessFor(cardNumber);
    }
}


function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");
    formControl.className = "sign__group error";
    small.innerText = message;
}
  
function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = "sign__group success";
}