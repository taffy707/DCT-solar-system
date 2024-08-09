const bcrypt = require('bcrypt');

const hashpassword = async (password) => {
    const saltRounds = 12;
    const hashedPassword = await bcrypt.hash(password, saltRounds);
    return hashedPassword;
}

const checkTLSVersion = () => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `https://example.com`);
    xhr.onload = function(){
        console.log(`TLS Version:`, xhr.getResponseHeader(`TLS-Version`));
    };
    xhr.send();
}

// Validating Email Address:

const ValidateEmail = (Email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(Email);
}

export default{
    validateEmail
};
