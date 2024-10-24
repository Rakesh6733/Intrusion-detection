const form = document.querySelector('.jobform');
const jobname = document.querySelector('input[name="jobname"]');
const desc = document.querySelector('input[name="desc"]');
const jobtype = document.querySelector('input[name="Type"]');
const duration = document.querySelector('input[name="duration"]');
const salary = document.querySelector('input[name="salary"]');
const link = document.querySelector('input[name="link"]');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (jobname.value === '' || desc.value === '' || jobtype.value === '' || duration.value === '' || salary.value === '' || link.value === '') {
    alert('Please fill in all fields.');
  } else if (!isValidUrl(link.value)) {
    alert('Please enter a valid URL.');
  } else {
    form.submit();
  }
});

function isValidUrl(url) {
  try {
    new URL(url);
    return true;
  } catch (error) {
    return false;
  }
}
