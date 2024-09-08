const phoneNumber = document.getElementById("userPhone");
const upiMode = document.getElementById("upimethod");



const ValidateCancelBookingValues = {
    validatePhone: false,
    validatePayment: false,
};

// const cancelForm = document.getElementById("Cancelform");
// cancelForm.addEventListener("submit", (form)=>{
//     form.preventDefault();

//     if(ValidateCancelBookingValues.validatePhone === true && ValidateCancelBookingValues.validatePayment){
//         const formObjectData = $(this).serializeArray();
//               const formData = {}
        
//               formObjectData.forEach( e => {
//                 formData[e.name] = e.value
//               });
        
//               console.log(formData);
              
//     }
// });



function validatePhone(){
    const phoneNumberValue = phoneNumber.value.trim();

    if(phoneNumberValue === ""){
        setErrorFor(phoneNumber, "Phone Number cannot be blank.")
    } else if(phoneNumberValue.length < 10 || phoneNumberValue.length > 10){
        setErrorFor(phoneNumber, "Phone number should be of 10 digits.")
    } else {
        ValidateCancelBookingValues.validatePhone = true;
        setSuccessFor(phoneNumber);
    }
}

function checkUPI(){
    const upimethodValue = upiMode.value.trim();
    console.log(upimethodValue);

    if(upimethodValue === ""){
        setErrorFor(upiMode, "Please Select UPI Option.");
        
    } else {
        ValidateCancelBookingValues.validatePayment = true;
        setSuccessFor(upiMode);
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

