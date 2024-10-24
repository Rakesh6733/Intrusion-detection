const form = document.querySelector('.contact-form');
const firstNameInput = form.querySelector('#firstNameInput');
const lastNameInput = form.querySelector('#lastNameInput');
const emailInput = form.querySelector('#emailInput');
const messageInput = form.querySelector('#messageInput');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // validate form fields
  const errors = [];

  if (firstNameInput.value.trim() === '') {
    errors.push('First name is required');
  }

  if (lastNameInput.value.trim() === '') {
    errors.push('Last name is required');
  }

  if (emailInput.value.trim() === '') {
    errors.push('Email is required');
  } else if (!isValidEmail(emailInput.value)) {
    errors.push('Email is not valid');
  }

  if (messageInput.value.trim() === '') {
    errors.push('Message is required');
  }

  if (errors.length > 0) {
    alert(errors.join('\n'));
    return;
  }

  // submit form
  alert('Form submitted successfully');
});

function isValidEmail(email) {
  const emailRegex = /^\S+@\S+\.\S+$/;
  return emailRegex.test(email);
}
