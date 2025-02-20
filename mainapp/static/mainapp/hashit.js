document.addEventListener('DOMContentLoaded', function() {
    async function hashPassword(password) {
        const encoder = new TextEncoder();
        const data = encoder.encode(password);
        const hashBuffer = await crypto.subtle.digest('SHA-256', data);  
        const hashArray = Array.from(new Uint8Array(hashBuffer));  
        const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');  
        return hashHex;
    }

    document.getElementById('login-form').addEventListener('submit', async function(event) {
        event.preventDefault(); 
        const passwordField = document.getElementById('password');
        const password = passwordField.value;
        const hashedPassword = await hashPassword(password);
        passwordField.value = hashedPassword;
        this.submit();
    });
    document.getElementById('register-form').addEventListener('submit', async function(event) {
        event.preventDefault(); 
        const passwordField = document.getElementById('reg-password');
        const password = passwordField.value;
        const hashedPassword = await hashPassword(password);
        passwordField.value = hashedPassword;
        this.submit();
    });
});
