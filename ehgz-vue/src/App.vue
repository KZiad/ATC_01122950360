<template>
    <div id="app" class="page">
        <HeaderBar ref="HeaderBar"/>
        <router-view ref="Router" />
    </div>
</template>

<script>
import HeaderBar from "./components/HeaderBar.vue";
import { ref, provide } from "vue";
export default {
    name: "App",
    components: {
        HeaderBar,
    },
    setup() {
        const isAuthenticated = ref(false);
        const isAdmin = ref(false);
        provide("isAuthenticated", isAuthenticated);
        provide("isAdmin", isAdmin);
    },
};
</script>

<style src="./assets/style.css" scoped></style>
