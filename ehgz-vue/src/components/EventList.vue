<template>
    <div class="event-list-container">
        <div class="event-card-group">
            <EventCard
                v-for="event in events"
                :key="event.id"
                :event-id="event.id"
                :event-name="event.name"
                :event-price="event.price"
                :event-date="event.date"
                :event-venue="event.venue"
                :event-image-url="event.image"
                :booked="event.booked"
                :category="event.category.name"
            />
        </div>
    </div>
    <div class="pagination" v-if="events.next !== null && events.previous !== null">
        <div class="pagination-back">&lt;</div>
        <div class="pagination-number pagination-selected" >1</div>
        <div class="pagination-number" v-for="page in paginationNumbers.items" :key="page" @click="fetchEvents(page)">{{page}}</div>
        <div class="pagination-next">&gt;</div>
    </div>
</template>
<script setup>
import EventCard from "./EventCard.vue";
import { ref, onMounted, reactive } from "vue";
import axios from "axios";

const events = ref([]);
const paginationDetails = ref({
    next: null,
    previous: null,
    count: 0,
});
const paginationNumbers = reactive({
    items:[]
});

async function populatePagination() {
    const totalPages = Math.ceil(paginationDetails.value.count / 3);
    for (let i = 1; i < totalPages + 1; i++) {
        paginationNumbers.items[i-1] = i
        
    }
    console.log(paginationNumbers.value)
}
async function fetchEvents(page) {
    try {
        const url = process.env.VUE_APP_API_URL;
        const response = await axios.get(url + `/api/events?page_size=3&?page=${page}`); // Replace with your API endpoint
        events.value = response.data.results;
        paginationDetails.value.next = response.data.next;
        paginationDetails.value.previous = response.data.previous;
        paginationDetails.value.count = response.data.count;


    } catch (error) {
        console.error("Error fetching events:", error);
    }
}
onMounted(() => {
    fetchEvents(1);
    populatePagination();
});
</script>

<style src="../assets/style.css" scoped></style>
