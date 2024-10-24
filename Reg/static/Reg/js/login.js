const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  
  if (username === 'example' && password === 'password') {
    alert('Login successful!');
  } else {
    alert('Invalid username or password!');
  }
});
