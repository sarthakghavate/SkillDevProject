////document.addEventListener('DOMContentLoaded', () => {
////    const signupBtn = document.getElementById('signup-btn');
////    const loginBtn = document.getElementById('login-btn');
////    const authForm = document.getElementById('auth-form');
////    const submitAuth = document.getElementById('submit-auth');
////    const nameInput = document.getElementById('name');
////
////    signupBtn.addEventListener('click', () => {
////        nameInput.style.display = 'block';
////        authForm.style.display = 'block';
////    });
////
////    loginBtn.addEventListener('click', () => {
////        nameInput.style.display = 'none';
////        authForm.style.display = 'block';
////    });
////
////    submitAuth.addEventListener('click', () => {
////        const name = nameInput.value;
////        const email = document.getElementById('email').value;
////        const password = document.getElementById('password').value;
////        const endpoint = nameInput.style.display === 'block' ? '/signup' : '/login';
////
////        fetch(endpoint, {
////            method: 'POST',
////            headers: { 'Content-Type': 'application/json' },
////            body: JSON.stringify({ name, email, password })
////        })
////        .then(response => response.json())
////        .then(data => alert(data.message || data.error))
////        .catch(err => console.error(err));
////    });
////});
//
//// only hero js
//
////document.addEventListener('DOMContentLoaded', () => {
////    const navLinks = document.querySelectorAll('.nav-links li a');
////
////    navLinks.forEach(link => {
////        link.addEventListener('click', (e) => {
////            e.preventDefault();
////            const targetId = link.getAttribute('href').substring(1);
////            const targetSection = document.getElementById(targetId);
////            targetSection.scrollIntoView({ behavior: 'smooth' });
////        });
////    });
////});
//
//// hero js + register js
//
//document.addEventListener('DOMContentLoaded', () => {
//    // Smooth Scroll for Navigation Links
//    const navLinks = document.querySelectorAll('.nav-links li a');
//
//    navLinks.forEach(link => {
//        link.addEventListener('click', (e) => {
//            e.preventDefault();
//            const targetId = link.getAttribute('href').substring(1);
//            const targetSection = document.getElementById(targetId);
//            targetSection.scrollIntoView({ behavior: 'smooth' });
//        });
//    });
//
//    // Registration Form Submission
//    const registerForm = document.getElementById('register-form');
//
//    if (registerForm) {
//        registerForm.addEventListener('submit', (event) => {
//            event.preventDefault();
//
//            const name = document.getElementById('name').value;
//            const email = document.getElementById('email').value;
//            const password = document.getElementById('password').value;
//            const confirmPassword = document.getElementById('confirm-password').value;
//
//            if (password !== confirmPassword) {
//                alert('Passwords do not match!');
//                return;
//            }
//
//            // Here you can send the form data to the server
//            const userData = { name, email, password };
//
//            fetch('/signup', {
//                method: 'POST',
//                headers: { 'Content-Type': 'application/json' },
//                body: JSON.stringify(userData),
//            })
//            .then(response => response.json())
//            .then(data => {
//                alert(data.message); // Handle response from the server
//                // Redirect user after successful registration or reset the form
//                registerForm.reset(); // Optionally, clear form fields
//            })
//            .catch(err => {
//                console.error('Error:', err);
//                alert('Something went wrong. Please try again.');
//            });
//        });
//    }
//});


// method not found error solving

// main.js (for handling form submission without reloading)
document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            window.location.href = '/login';
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
    });
});
