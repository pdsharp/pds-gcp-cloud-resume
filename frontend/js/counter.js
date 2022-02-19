const getCount = () => {
  fetch("https://us-west1-pds-cloud-resume.cloudfunctions.net/counter")
  .then(response => response.text())
  .then(response => document.getElementById('counter').innerText = response)
}
getCount();