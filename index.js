function validatePassword(password){
    const minLength = 8;
    const hasUppercase = /[A-Z]/.test(password);
    const haslowercase = /[a-z]/.test(password);
    const hasnumber = /\d/.test(password);
    const haSspecialchar = /[!@#$%&*]/.test(password);
     

    if (!hasUppercase){
        return "password must contain at least one uppercase letter.";
    }
    if (!haslowercase) {
        return "password must conatain at least one lowercase letter.";
    }
    if (!hasnumber) {
        return "password must conatain at least one number.";
   }
    if (!haSspecialchar) {
        return "password must conatain at least one special character.";
    }
    return "password is valid.";
}

//use process.argv to get command line arguments
const args = process.argv;
console.log(args);
const password = args[2];
console.log(validatePassword(password));
