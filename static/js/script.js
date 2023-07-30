// Alerts

document.addEventListener("DOMContentLoaded", function () {
    let messages = document.getElementById("msg");

    if (messages) {
        setTimeout(function () {
            let alert = new bootstrap.Alert(messages);
            alert.close()
        }, 3000);
    }
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

// Tooltip on like when unauthenticated user
document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (element) {
        return new bootstrap.Tooltip(element);
    });
});