<template>
    <div class="log-in-container">
        <div class="fields">
            <div class="input-container">
                <label for="email" class="email-label">Email</label>
                <input
                    :value="email_input"
                    @input="onInputEmail"
                    type="text"
                    placeholder="user@example.com"
                    class="email-input"
                />
            </div>

            <div class="input-container">
                <label for="password" class="password-label">Password</label>
                <input
                    @input="onInputPass"
                    :value="password_input"
                    @keyup.enter="login"
                    type="password"
                    placeholder="****************"
                    class="password-input"
                />
            </div>
        </div>
        <div class="auth-buttons">
            <div @click="login" class="auth-button">
                <div class="auth-button-text">Log In</div>
            </div>
            <div class="auth-button-or">or</div>
            <router-link to="/sign-up" class="auth-button-signup">
                <div class="auth-button-text">Sign Up</div>
            </router-link>
        </div>
    </div>
</template>
<script setup>
import { ref, inject } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const email_input = ref("");
const password_input = ref("");
const isAuthenticated = inject("isAuthenticated");
const isAdmin = inject("isAdmin");
async function checkAdmin() {
  const apiUrl = process.env.VUE_APP_API_URL;
  try {
    const response = await axios.get(`${apiUrl}/api/auth/token/verify/`);
    if (response.status === 200) {
      isAdmin.value = response.data.isadmin;

    }
  } catch (error) {
    isAdmin.value = false;
    console.error("Failed to fetch user data:", error);
  }
}


function onInputEmail(event) {
  email_input.value = event.target.value;
}
function onInputPass(event) {
  password_input.value = event.target.value;
}
async function login() {
  const apiUrl = process.env.VUE_APP_API_URL;
  const data = {
    email: email_input.value,
    password: password_input.value,
  };
  try {
    const response = await axios.post(`${apiUrl}/api/auth/login/`, data);
    if (response.status === 200) {
      console.log("Logged in!");
      isAuthenticated.value = true;
      await checkAdmin();
      if (isAdmin.value) {
        router.push("/admin");
      } else {
        router.push("/");
      }
    }
  } catch (error) {
    isAuthenticated.value = false;
    isAdmin.value = false;
    alert("Invalid email or password.");
    console.error("Login failed:", error);
  }


}
</script>
<style src="../assets/style.css" scoped></style>
