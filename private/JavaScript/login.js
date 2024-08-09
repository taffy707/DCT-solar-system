import validate from './security.js';

const email = document.querySelector(`email-login`);
const password = document.querySelector(`password-login`);

const checkLogin = (username, password) => {
    // Replace with actual logic:
    const isCorrect = username === 'correct' && password === 'correct';

    if(isCorrect){
        //Successful Login
        loginAttempts = 0;
        console.log('Login Successful');
        return true;
    }else{
        loginAttempts++;
        if(loginAttempts >= 3){
            // Trigger Password Reset
            console.log('Too many attempts. Password reset required.');
            // Implement Password Reset
            return false;
        }else{
            console.log(`Incorrect email address or password. Attempts Remaining:`, 3 - loginAttempts);
        }
    }
}

const handleLogin = (email, password) => {
    if(!validate.validateEmail(email)){
        // Handle invalid email
    }
}