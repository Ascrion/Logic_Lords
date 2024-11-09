function validateSignIn() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    if (email === "" || password === "") {
      alert("Both fields are required.");
      return false;
    }
  
    if (password.length < 6) {
      alert("Password must be at least 6 characters long.");
      return false;
    }
  
    alert("Sign-in successful!");
    // Add your backend authentication integration here
    return true;
  }
  