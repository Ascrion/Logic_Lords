// signup-page.js
function validateForm() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if (password !== confirmPassword) {
    alert('Passwords do not match. Please try again.');
    return false;
  }

  if (password.length < 6) {
    alert('Password must be at least 6 characters long.');
    return false;
  }

  return true;
}
