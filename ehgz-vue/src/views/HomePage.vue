<template>
<div class="events-addevent">
            <div class="events">Events</div>

        </div>

    <EventList />
</template>
<script setup>
import EventList from "../components/EventList.vue";
import { inject } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
const isAdmin = inject("isAdmin");
if (isAdmin.value) {
    console.log("admin");
    router.push("/admin/");
}
</script>
<style src="../assets/style.css" scoped></style>
