<template>
    <div class="booking-details-container">
        <div class="booking-details-text">
            <div class="booking-details-name">{{eventDetails.name}}</div>
            <div class="booking-details-date">{{eventDetails.date}}</div>
            <div class="booking-details-venue">{{eventDetails.date}}</div>
            <div class="booking-details-price">{{eventDetails.price.split(".")[0]}} EGP</div>
            <router-link to="/details/{{eventDetails.id}}" class="booking-details-back-button" ></router-link>
        </div>
        <div class="booking-details-image">
            <img :src="eventDetails.image" alt="Event Image" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
const router = useRoute();
const eventId = ref(router.params.id); // Use the event ID from the route params
const eventDetails = ref({
    name: "",
    date: "",
    venue: "",
    description: "",
    image: "",
    price: "0.00", // Default price
});
const url = process.env.VUE_APP_API_URL;
const successfulBooking = ref(false);
async function fetchEventDetails() {
    try {
        const response = await axios.get(url + `/api/events/${eventId.value}`); // Replace with your API endpoint
        eventDetails.value = response.data;

        // Format the date
        const formattedDate = new Intl.DateTimeFormat("en-GB", {
            weekday: "long", // Full weekday name (e.g., Tuesday)
            day: "2-digit", // Two-digit day (e.g., 25)
            month: "long", // Full month name (e.g., October)
            year: "numeric", // Full year (e.g., 2025)
            hour: "2-digit", // Two-digit hour (e.g., 12)
            minute: "2-digit", // Two-digit minute (e.g., 30)
            hour12: true, // 12-hour format
        }).format(new Date(eventDetails.value.date));
        if (eventDetails.value.booked) {
            successfulBooking.value = true;
        } else {
            successfulBooking.value = false;
            router.push(`/details/${eventId.value}`);
        }
        eventDetails.value.date = formattedDate;
    } catch (error) {
        console.error("Error fetching event details:", error);
    }
}
onMounted(() => {
    fetchEventDetails();
});
</script>
