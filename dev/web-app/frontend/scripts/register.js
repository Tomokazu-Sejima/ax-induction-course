// register.js
document.addEventListener('DOMContentLoaded', function () {
  document
    .getElementById('register-form')
    .addEventListener('submit', function (event) {
      event.preventDefault();

      var userId = document.getElementById('userId').value;
      var userName = document.getElementById('userName').value;
      var department = document.getElementById('department').value;

      var data = {
        user_id: userId,
        user_name: userName,
        department: department,
      };

      fetch('http://localhost:8000/user/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then((response) => {
          if (!response.ok) {
            return response.json().then((error) => {
              throw error;
            });
          }
          return response.json();
        })
        .then((data) => {
          alert('User registered successfully.');
        })
        .catch((error) => {
          console.error('Error:', error);
          let errorMessage = '';
          for (let field in error) {
            errorMessage += field + ': ' + error[field] + '\n';
          }
          alert('Error:\n' + errorMessage);
        });
    });
});
