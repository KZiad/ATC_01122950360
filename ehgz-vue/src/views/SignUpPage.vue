<template>
    <div class="log-in-container">
        <div class="fields">
            <div class="input-container">
                <label for="name" class="name-label">Name</label>
                <input v-model="nameInput" type="text" placeholder="John Doe" class="name-input" />
            </div>
            <div class="input-container">
                <label for="email" class="email-label">Email</label>
                <input
                    v-model="email"
                    type="text"
                    placeholder="user@example.com"
                    class="email-input"
                />
            </div>

            <div class="input-container">
                <label for="password1" class="password-label">Password</label>
                <div class="input-eye"><input
                    v-model="password1"
                    :type="showPassword ? 'text' : 'password'"
                    placeholder="****************"
                    class="password-input"
                />
                    <img
                    v-if="!showPassword"
                        src='../assets/eye.png'
                        class="eye-icon"
                        @click="togglePasswordVisibility"
                        />
                    <img
                    v-else
                        src='../assets/eye_closed.png'
                        class="eye-icon"
                        @click="togglePasswordVisibility"
                        />
                </div>
            </div>
            <div class="input-container">
                <label for="password2" class="password-label">Confirm Password</label>
                <input
                    v-model="password2"
                    :type="showPassword ? 'text' : 'password'"
                    placeholder="****************"
                    class="password-input"
                />
                
            </div>
        </div>

        <div class="auth-button" @click="confirmSignUp">
            <div class="auth-button-text">Confirm Sign Up</div>
        </div>
    </div>
</template>
<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const nameInput = ref("");
const email = ref("");
const password1 = ref("");
const password2 = ref("");
const url = process.env.VUE_APP_API_URL;
const showPassword = ref(false);
const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
};
async function confirmSignUp() {
    const response = await fetch(`${url}/api/auth/register/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: nameInput.value,
            email: email.value.toLowerCase(),
            password1: password1.value,
            password2: password2.value,
        }),
    });
    if (response.ok) {
        const data = await response.json();
        console.log(data);
        alert("Sign up successful!");
        router.push("/login");
    } else {
        const errorData = await response.json();
        console.error("Error:", errorData);
        alert("Sign up failed. Please try again.");
    }
}
</script>
<style src="../assets/style.css" scoped></style>