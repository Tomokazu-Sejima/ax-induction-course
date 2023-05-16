document.addEventListener('DOMContentLoaded', function () {
  // Initialize with an empty search
  searchEmployees();

  document
    .getElementById('search-btn')
    .addEventListener('click', function (event) {
      var employeeId = document.getElementById('userId').value;
      var userName = document.getElementById('userName').value;
      var department = document.getElementById('department').value;

      searchEmployees(employeeId, userName, department);
    });
});

function searchEmployees(employeeId = '', userName = '', department = '') {
  var url = new URL('http://localhost:8000/user/');

  var params = {
    employee_id: employeeId,
    user_name: userName,
    department: department,
  };

  url.search = new URLSearchParams(params).toString();

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      var tableBody = document
        .getElementById('results')
        .getElementsByTagName('tbody')[0];
      tableBody.innerHTML = '';

      data.forEach((employee) => {
        var row = document.createElement('tr');

        var idCell = document.createElement('td');
        idCell.textContent = employee.user_id;
        row.appendChild(idCell);

        var nameCell = document.createElement('td');
        nameCell.textContent = employee.user_name;
        row.appendChild(nameCell);

        var departmentCell = document.createElement('td');
        departmentCell.textContent = employee.department;
        row.appendChild(departmentCell);

        tableBody.appendChild(row);
      });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
