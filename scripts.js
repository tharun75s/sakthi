// Access the form and complaints list
const form = document.getElementById('complaintForm');
const complaintsList = document.getElementById('complaints');

// Event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent page reload

    // Get input values
    const name = document.getElementById('name').value;
    const complaint = document.getElementById('complaint').value;

    // Validate input
    if (name && complaint) {
        // Create a new complaint item
        const complaintItem = document.createElement('li');
        complaintItem.classList.add('complaintItem');

        // Add complaint details
        complaintItem.innerHTML = `<strong>${name}</strong><p>${complaint}</p>`;

        // Append the new complaint to the list
        complaintsList.appendChild(complaintItem);

        // Clear the form
        form.reset();
    } else {
        alert('Please fill in both fields');
    }
});
