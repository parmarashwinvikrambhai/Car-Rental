
const form = document.getElementById("form");
const userdl = document.getElementById("userDL");
const fname = document.getElementById("fullname");
const lname = document.getElementById("lastname");
const email = document.getElementById("email");
const password = document.getElementById("password");
const address = document.getElementById("address");
const phone = document.getElementById("phoneno");
const file = document.getElementById("dlimage");

const ValidateValues = {
  userDL: false, 
  userFirstName: false, 
  userLastName: false, 
  userEmail: false, 
  userPassword: false, 
  userAddress: false, 
  userPhone: false, 
  userDLFile: false,
};



// validate the Driving Licence Number
function checkUserDL() {
	const userDLValue = userdl.value.trim();
	if (userDLValue === "") {
	  setErrorFor(userdl, "Driving Licence cannot be blank");
	} else if (userDLValue.length < 15) {
	  setErrorFor(userdl, "Driving Licence should not be less than 15");
	} else {
    ValidateValues.userDL = true;
	  setSuccessFor(userdl);
	}
}


// validate the FirstName
function checkFirstName() {
    const userFirstNameValue = fname.value.trim();
    if (userFirstNameValue === "") {
      setErrorFor(fname, "FirstName cannot be blank");
    } else if (userFirstNameValue.length < 3) {
      setErrorFor(fname, "FirstName should not be less than 3");
    } else {
      ValidateValues.userFirstName = true;
      setSuccessFor(fname);
    }
}


// validate the LastName
function checkLastName() {
    const userLastNameValue = lname.value.trim();
    if (userLastNameValue === "") {
      setErrorFor(lname, "FirstName cannot be blank");
    } else if (userLastNameValue.length < 4) {
      setErrorFor(lname, "FirstName should not be less than 3");
    } else {
      ValidateValues.userLastName = true;
      setSuccessFor(lname);
    }
}



// validate the Email
function checkUserEmail() {
    const emailValue = email.value.trim();
    if (emailValue === "") {
      setErrorFor(email, "Email cannot be blank");
    } else if (!isEmail(emailValue)) {
      setErrorFor(email, "Not a valid email");
    } else {
      ValidateValues.userEmail = true;
      setSuccessFor(email);
    }
}


// validate the Password
function checkUserPassword() {
    const passwordValue = password.value.trim();
    if (passwordValue === "") {
      setErrorFor(password, "Password cannot be blank");
    } else if (passwordValue.length < 8 || passwordValue.length > 12) {
      setErrorFor(password, "Password should be between 8 to 12 characters");
    } else {
      ValidateValues.userPassword = true;
      setSuccessFor(password);
    }
}


// validate the Address
function checkAddress(){
    const addressValue = address.value.trim();
    if(addressValue === ""){
        setErrorFor(address, "Address cannot be blank");
    } else {
      ValidateValues.userAddress = true;
      setSuccessFor(address);
    }
}

// validate the Phone
function checkPhone(){
    const phoneValue = phone.value.trim();
    if(phoneValue === ""){
        setErrorFor(phone, "Phone cannot be blank");
    } else if((phoneValue.length < 10)){
        setErrorFor(phone, "Phone number should be of 10 digits");
    } else {
      ValidateValues.userPhone = true;
        setSuccessFor(phone);
    }
}

// validate the Driving Licence Image
function checkImageType() {
    console.log("Check Image Type called..");
    if (/\.(jpe?g|png|gif)$/i.test(file.files[0].name) === false) {
      setErrorFor(file, "Please Select Image");
    } else {
      ValidateValues.userDLFile = true;
      setSuccessFor(file);
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


function isEmail(email) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    email
  );
}

// function validPassword(passwordValue, password)
//   var re = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
//   return re.test(password);
// }



let dateInput1 = document.getElementById("pickupdate");
dateInput1.min = new Date().toISOString().slice(0,new Date().toISOString().lastIndexOf(":"));

// set the minimuum and maximum date
function restrictDate(){
  
  let dateInput1 = document.getElementById("pickupdate");
  
  if(dateInput1.value != ""){
    document.getElementById("dropdate").value = "";
    document.getElementById("dropdate").removeAttribute("disabled");
  } else {
    document.getElementById("dropdate").setAttribute("disabled", "");
  }

  var date = dateInput1.value.toString().slice(0,10);
  // console.log("date: ", date);

  const time = dateInput1.value.toString().slice(11);
  // console.log("time: ", time);

  var convertedTime12 = moment(time, 'HH:mm').format('hh:mm:ss');
  // console.log(convertedTime12);

  var convertedTime24 = moment(time, "HH:mm").format('HH:mm:ss');
  // console.log(convertedTime24);

  const dateTime = moment(`${date} ${convertedTime24}`, 'YYYY-MM-DD HH:mm:ss').format();
  // console.log("datetime: ", dateTime);  

  // console.log("DateObject Conversion: ", new Date(dateTime));

  setMinDateInSecondCalendar(date);  
}


function setMinDateInSecondCalendar(date){
  var dummydate = date;
  var date2 = new Date(date);
  var maxtoday2 = new Date(date2.getTime() + 24 * 60 * 60 * 1000);
  var fakemaxtoday2 = maxtoday2;
  // console.log("mindate in Date2 calendar: ", maxtoday2);
  var maxdate = String(maxtoday2.getDate()).padStart(2, "0");
  var maxmonth = String(maxtoday2.getMonth() + 1).padStart(2, "0");
  var maxyear = maxtoday2.getFullYear();

  maxtoday2 = maxyear + "-" + maxmonth + "-" + maxdate;
  // console.log("mindate in EndDateTime Calendar: ", maxtoday2);
  
  let dateInput2 = document.getElementById("dropdate");
  dateInput2.min = new Date(maxtoday2).toISOString().slice(0,new Date(maxtoday2).toISOString().lastIndexOf(":"));

  
  setMaxDateInSecondCalendar(maxtoday2);  
}


function setMaxDateInSecondCalendar(maxtoday2){
  
  // below code will add the number of days into the current date
  Date.prototype.addDays = function (days) {
    let date = new Date(maxtoday2);
    // console.log("todayinfunction", date);
    date.setDate(date.getDate() + days);
    return date;
  };
 
  // creating maximum date and passing number of days we want to add
  let date3 = new Date(maxtoday2);

  var yyyy = date3.getFullYear();
  var mm = String(date3.getMonth() + 1).padStart(2, "0");
  var dd = String(date3.getDate()).padStart(2, "0");
  const max_date = new Date(date3.addDays(daysInMonth(yyyy, mm)));
  // console.log("add days: " + date3.addDays(daysInMonth(yyyy, mm)));

  // get the date, month and year for maximum date
  var mdd = String(max_date.getDate()).padStart(2, "0");
  var mmm = String(max_date.getMonth() + 1).padStart(2, "0");
  var myyyy = max_date.getFullYear();

  // constructing maximum date to string
  var mymaxdate = myyyy + "-" + mmm + "-" + mdd;
  // console.log("final maxdate in 2nd cal.: " + mymaxdate);
  
  
   let dateInput3 = document.getElementById("dropdate");
  dateInput3.max = new Date(mymaxdate).toISOString().slice(0,new Date(mymaxdate).toISOString().lastIndexOf(":"));
}

function daysInMonth(year, month) {
  // console.log("daydiff: ", new Date(year, month, 0).getDate());
  return new Date(year, month, 0).getDate();
}

// function CheckInput(){
//   if (confirm("Are you sure ?") === false){
//     location.href = '/http://127.0.0.1:8080/client/booked_car/';
   
//   }
// }
const form2 = document.getElementById("form");
form2.addEventListener("submit", (e)=>{
  e.preventDefault();

  data = {
    "pickup_date": document.getElementById("pdate").value,
    "drop_date": document.getElementById("ddate").value,
    "pickup_location": document.getElementById("plocation").value,
    "drop_location": document.getElementById("dlocation").value,
    "total": document.getElementById("ptotal").value,
    "car_id": document.getElementById("carid").value,
  }

  let car_id = data["car_id"];
  if( confirm("Are you sure?") === true){
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8080/client/booking_car/",
      data: data,
      success: function(response){
        console.log("FormData: ", data);
        location.href = '/client/booked_car/';
        
      },
      error:function(response){
        alert("something went wrong.")
      }
    });
  }
})


