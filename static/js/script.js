// Alerts

document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close()
    }, 3000);
});

// Delete Images in Edit Form

function showConfirmationModal() {
    const imagesToDelete = document.querySelectorAll('input[data-marked-for-deletion]:checked');

    if (imagesToDelete.length > 0) {
        const modal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        modal.show();
    } else {
        // No images marked submit the form directly
        document.getElementById('edit-report-form').submit();
    }
}

function submitForm() {
    // Change 'confirm-deletion' hidden input boolean
    document.getElementById('confirm-deletion').value = 'true';
    // Submit the form
    document.getElementById('edit-report-form').submit();
}
