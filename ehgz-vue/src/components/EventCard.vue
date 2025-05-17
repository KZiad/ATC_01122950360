<template>
    <router-link :to="`/details/${eventId}`" class="event-card">
        <router-link class="event-card-image" :to="`/details/${eventId}`"
            ><img
                class="event-card-image"
                :src="eventImageUrl"
                alt="Event Image"
        /></router-link>
        <div class="category-settings" v-if="isAdmin" ><div class="event-card-category"> {{ category }}</div><router-link :to="`/details/${eventId}/edit`"><img class="edit-cog" src="../assets/settings.png" /></router-link></div>
        <div class="category-settings" v-else ><div class="event-card-category"> {{ category }}</div></div>
        <div class="frame-15">
            <div class="event-name-price">
                <div class="event-name">{{ eventName }}</div>
            </div>
            <!-- Replace eventDate with formattedEventDate -->
            <div class="event-date">{{ formattedEventDate }}</div>
            <div class="event-venue">{{ eventVenue }}</div>
        </div>
        <div class="button-price">
            <router-link
                :to="`/details/${eventId}`"
                class="event-button"
                :class="{ 'book-now': !booked, 'booked': booked && isAuthenticated }"
            >
                <div class="event-button-text">
                    {{ isAdmin ? "Manage" : booked && isAuthenticated ? "Booked" : "Book Now" }}
                </div>
            </router-link>

            <div class="event-price">{{ eventPrice.split(".")[0] }} EGP</div>
        </div>
    </router-link>
</template>

<script>
import { inject } from "vue";
export default {
    name: "EventCard",
    props: {
        category:{
            type: String,
            required : true
        },
        eventId: {
            type: Number,
            required: true,
        },
        eventName: {
            type: String,
            required: true,
        },
        eventPrice: {
            type: String,
            required: true,
        },
        eventDate: {
            type: String,
            required: true,
        },
        eventVenue: {
            type: String,
            required: true,
        },
        eventImageUrl: {
            type: String,
            required: true,
        },
        booked: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        formattedEventDate() {
            // Format the date to "Tuesday, 25 October 2025"
            return new Intl.DateTimeFormat("en-GB", {
                weekday: "long", // Full weekday name (e.g., Tuesday)
                day: "2-digit", // Two-digit day (e.g., 25)
                month: "long", // Full month name (e.g., October)
                year: "numeric", // Full year (e.g., 2025)
            }).format(new Date(this.eventDate));
        },
    },
    setup() {
        const isAdmin = inject("isAdmin");
        const isAuthenticated = inject("isAuthenticated");
        return {
            isAdmin,
            isAuthenticated
        };
    },
};
</script>

<style src="../assets/style.css" scoped></style>
