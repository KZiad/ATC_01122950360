<template>
    <div class="log-in-container">
        <div class="fields">
            <div class="input-container">
                <label for="name" class="name-label">Name</label>
                <input v-model="email" type="text" placeholder="John Doe" class="name-input" />
            </div>
            <div class="input-container">
                <label for="email" class="email-label">Email</label>
                <input
                    type="text"
                    placeholder="user@example.com"
                    class="email-input"
                />
            </div>

            <div class="input-container">
                <label for="password" class="password-label">Password</label>
                <input
                    type="password"
                    placeholder="****************"
                    class="password-input"
                />
            </div>
        </div>

        <div class="auth-button" href="./signUp.html">
            <div class="auth-button-text">Confirm Sign Up</div>
        </div>
    </div>
</template>
<script>
export default {
    name: "SignUpPage",
};
</script>
<style src="../assets/style.css" scoped></style>