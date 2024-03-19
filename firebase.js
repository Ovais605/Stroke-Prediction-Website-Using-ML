// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword   } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyB7TAthtYywsJYSKx7UA0e5GVG_ALw9L9U",
    authDomain: "stroke-prediction-system.firebaseapp.com",
    projectId: "stroke-prediction-system",
    storageBucket: "stroke-prediction-system.appspot.com",
    messagingSenderId: "715369107689",
    appId: "1:715369107689:web:6c7c6cd1ddc54c6ad5e078"
};

// Initialize Firebase  
const app = initializeApp(firebaseConfig);

// // Get a reference to the auth service using getAuth
const auth = getAuth();

// Function to handle login
function loginUser(email, password) {
    // const auth = getAuth();
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // Signed up 
        const user = userCredential.user;
        console.log(user);
        // ...
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        // ..
        console.log(error);
      });
}

function getCurrentUser() {
    const user = auth.currentUser;

    if (user) {
        console.log(user);
    } else {
        console.log('o user logged in!');    
    }
}

document.getElementById('getuser').addEventListener('click', () => {
    getCurrentUser();
})

// Listen for the form submission
document.getElementById('login-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission behavior

  const email = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Call the loginUser function with provided email and password
  loginUser(email, password);
});