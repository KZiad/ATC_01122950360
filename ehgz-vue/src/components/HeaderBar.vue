<template>
    <div class="header">
        <router-link to="/">
            <img
                loading="lazy"
                class="logo-2"
                src="../assets/logo.png"
                alt="Logo"
            />
        </router-link>

        <div v-if="isAuthenticated" class="header-button" @click="logout">
            <div @click="logout()" class="header-button-text">Log Out</div>
        </div>
        <div v-else class="buttons">
            <div class="header-button">
                <router-link to="/sign-in">
                    <div class="header-button-text">Log In</div>
                </router-link>
            </div>
            <div class="header-button">
                <router-link to="/sign-up">
                    <div class="header-button-text">Sign Up</div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { inject, onMounted } from "vue";
import axios from "axios";
const isAuthenticated = inject("isAuthenticated");
async function verifyToken() {
    const apiUrl = process.env.VUE_APP_API_URL;

    try {
        const response = await axios.get(`${apiUrl}/api/auth/token/verify/`);
        if (response.status === 200) {
            console.log("Logged in!");
            isAuthenticated.value = true;
        }
    } catch (error) {
        console.error("Token verification failed:", error);
        isAuthenticated.value = false;
        // Attempt to refresh the token
        try {
            const refreshResponse = await axios.post(
                `${apiUrl}/api/auth/token/refresh/`
            );
            if (refreshResponse.status === 200) {
                console.log("Token refreshed!");
                isAuthenticated.value = true;
            }
        } catch (refreshError) {
            console.error("Token refresh failed:", refreshError);
            isAuthenticated.value = false;
        }
    }
}

async function logout() {
    const apiUrl = process.env.VUE_APP_API_URL;
    try {
        await axios.post(`${apiUrl}/api/auth/logout/`).then(
            () => {
                console.log("Logged out!");
                isAuthenticated.value = false;
                document.cookie = "ehgz-access-token=; Max-Age=0"; // Clear the token cookie
            },
            { withCredentials: true }
        );
    } catch (error) {
        console.error("Logout failed:", error);
    }
}
onMounted(() => {
    verifyToken();
});
</script>

<style src="../assets/style.css" scoped></style>
