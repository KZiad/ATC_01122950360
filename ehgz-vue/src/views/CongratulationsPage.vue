<template>
    <div class="title"><router-link :to="`/details/${eventDetails.id}`" class="back-button-back">&lt;</router-link> Congratulations! Your ticket was booked!</div>
    <div style="display: flex; width: 100%; justify-content: center;"><div class="booking-details">
        <div class="booking-details-image">
            <img :src="eventDetails.image" alt="Event Image" />
        </div>
        <div class="details-text booking-details-text">
            <div class="details-top">
                <div class="event-card-category">{{ eventDetails.category.name }}</div>
                <div class="event-details-name">{{ eventDetails.name }}</div>
                <div class="event-details-date">{{ eventDetails.date }}</div>
                <div class="event-details-venue">{{ eventDetails.venue }}</div>

            </div>

        </div>
    </div></div>
</template>

<script setup>
import { reactive,ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
const router = useRoute();
const eventId = ref(router.params.id); // Use the event ID from the route params

const url = process.env.VUE_APP_API_URL;
const eventDetails = reactive({
    id:0,
    name: "",
    date: "",
    venue: "",
    description: "",
    image: "",
    price: "0.00", // Default price
    booked: false,
    category: "",
    tags: [],
});
async function fetchEventDetails () {
    try {
        const response = await axios.get(url + `/api/events/${eventId.value}`); // Replace with your API endpoint

        // Format the date
        const formattedDate = new Intl.DateTimeFormat("en-GB", {
            weekday: "long", // Full weekday name (e.g., Tuesday)
            day: "2-digit",  // Two-digit day (e.g., 25)
            month: "long",   // Full month name (e.g., October)
            year: "numeric", // Full year (e.g., 2025)
            hour: "2-digit", // Two-digit hour (e.g., 12)
            minute: "2-digit", // Two-digit minute (e.g., 30)
            hour12: true, // 12-hour format
        }).format(new Date(response.data.date));
        eventDetails.id = response.data.id;
        eventDetails.name = response.data.name;        
        eventDetails.date = formattedDate;
        eventDetails.venue = response.data.venue;
        eventDetails.price = response.data.price;
        eventDetails.description = response.data.description;
        eventDetails.image = response.data.image;
        eventDetails.booked = response.data.booked;
        eventDetails.tags = response.data.tags;
        eventDetails.category = response.data.category;
    } catch (error) {
        console.error("Error fetching event details:", error);
    }
}
onMounted(() => {
    fetchEventDetails();
});
</script>
