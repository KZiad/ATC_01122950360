<template>
    <div class="title"><router-link to="/" class="back-button-back">&lt;</router-link>Event Details</div>
    <div class="details">
        <div class="details-text">
            <div class="details-top">
                <div class="event-card-category">{{ eventDetails.category.name }}</div>
                <div class="event-details-name">{{ eventDetails.name }}</div>
                <div class="event-details-date">{{ eventDetails.date }}</div>
                <div class="event-details-venue">{{ eventDetails.venue }}</div>
                <div class="tags">
                    
                    <div class="tag-card" v-for="tag in eventDetails.tags" :key="tag"> #{{ tag.name }}</div>
    
                </div>
            </div>
            <div class="description">
                {{ eventDetails.description }}
            </div>
        </div>
        <div class="image-book-button">
            <img class="event-details-image" :src="eventDetails.image" />
            <div class="details-button-price">
                <div @click="confirmBooking" class="book-button book-button-back">
                    <div class="book-button-text" v-if="!eventDetails.booked">Book Now</div>
                    <div class="book-button-text" v-else>Booking Details</div>
                </div>
                <div class="price" v-if="eventDetails.price != '0.00'">{{(eventDetails.price).split(".")[0]}} EGP</div>
            </div>
        </div>
    </div>

</template>
<style src="../assets/style.css" scoped></style>
<script setup>
import { ref, onMounted, reactive } from "vue";
import axios from "axios";

// get the event id from the url query params
import { useRoute } from "vue-router";
const router = useRoute();
const eventId = ref(router.params.id); // Use the event ID from the route params
const eventDetails = reactive({
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
const url = process.env.VUE_APP_API_URL;
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
async function confirmBooking(){
    try {
        await axios.post(url + `/api/book/${eventId.value}`)
        router.push(`/details/${eventId.value}/congratulations`);
    } catch(error){
        if (error.response.status === 400 && error.response.data.message === "You have already booked this event.") {
            console.error("Event already booked");
            router.push(`/details/${eventId.value}/booking-details`);
        }
        else {
            console.error("Error fetching booking event:", error);
        }
    }
}
onMounted(() => {
    fetchEventDetails();
});
</script>
