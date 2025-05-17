<template>
    <div class="title"><router-link to="/" class="back-button-back">&lt;</router-link>Event Details</div>
    <LoadingCircle v-if="!isLoaded" />
    <div v-else class="details">
        <div class="details-text">
            <div class="details-top">
                <div class="event-card-category">{{ eventDetails.category_display }}</div>
                <div class="event-details-name">{{ eventDetails.name }}</div>
                <div class="event-details-date">{{ eventDetails.date }}</div>
                <div class="event-details-venue">{{ eventDetails.venue }}</div>
                <div class="tags">
                    
                    <div class="tag-card" v-for="tag in eventDetails.tags_display" :key="tag"> #{{ tag }}</div>
    
                </div>
            </div>
            <div class="description">
                {{ eventDetails.description }}
            </div>
        </div>
        <div class="image-book-button">
            <img  class="event-details-image" :src="eventDetails.image" />
            <div v-if="!isAdmin" class="details-button-price">
                <div @click="confirmBooking" class="book-button book-button-back">
                    <div class="book-button-text" v-if="!eventDetails.booked||!isAuthenticated">Book Now</div>
                    <div class="book-button-text" v-else>Booking Details</div>
                </div>
                <div class="price" v-if="eventDetails.price != '0.00'">{{(eventDetails.price).split(".")[0]}} EGP</div>
            </div>
            <div v-else class="details-admin-buttons">
                <router-link :to="`/details/${eventId}/edit`" class="admin-edit-button header-button-text">Edit</router-link>
                <div @click="deleteEvent()" class="admin-delete-button header-button-text">Delete</div>
                </div>
        </div>
    </div>

</template>
<style src="../assets/style.css" scoped></style>
<script setup>
import { ref, onMounted, reactive, inject } from "vue";
import LoadingCircle from "@/components/LoadingCircle.vue";
import axios from "axios";

// get the event id from the url query params
import { useRouter } from "vue-router";
import { useRoute } from "vue-router";
const route = useRoute();
const router = useRouter();
const eventId = ref(route.params.id); // Use the event ID from the route params
const eventDetails = reactive({
    name: "",
    date: "",
    venue: "",
    description: "",
    image: "",
    price: "0.00", // Default price
    booked: false,
    category_display: "",
    tags_display: [],
});
const isLoaded = ref(false);
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
        eventDetails.tags_display = response.data.tags_display;
        eventDetails.category_display = response.data.category_display;
    } catch (error) {
        console.error("Error fetching event details:", error);
    }
    finally {
        isLoaded.value = true;
    }
}
const isAuthenticated = inject("isAuthenticated")
const isAdmin = inject("isAdmin")
async function confirmBooking(){
    if (!isAuthenticated.value){
        router.push("/login")
        return
    }
    try {
        await axios.post(url + `/api/book/${eventId.value}`)
        eventDetails.booked = true;
        console.log("Booking successful");
        router.push(`/details/${eventId.value}/congratulations`);
    } catch(error){
        if (error.response.status === 400 && error.response.data.message === "You have already booked this event.") {
            console.error("Event already booked");
            router.push(`/details/${eventId.value}/booking`);    
        }
        else {
            console.error("Error fetching booking event:", error);
        }
    }
}
async function deleteEvent() {
    if (confirm("Are you sure you want to delete this event?")) {
        try {
            await axios.delete(url + `/api/events/${eventId.value}`);
            router.push("/admin/");
        } catch (error) {
            console.error("Error deleting event:", error);
        }
    }
}
onMounted(() => {
    fetchEventDetails();
});
</script>
<style scoped>
.admin-edit-button {
    background-color: #7c7c7c;
    color: #ffffff;
    padding: 10px 20px;
    border-radius: 15px;
    text-decoration: none;
    margin-right: 10px;
    width : 100%;
}
.admin-delete-button {
    background-color: #ba2828;
    color: #ffffff;
    padding: 10px 20px;
    border-radius: 15px;
    text-decoration: none;
    margin-right: 10px;
    width : 100%;
}
.details-admin-buttons{
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-bottom: 20px;
    gap:10px;
    width: 60%;
}
</style>