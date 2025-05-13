<template>
        <div class="events-addevent">
            <div class="events">Events</div>
            <div class="add-event">
                <router-link to="/addevent" class="header-button header-button-text">
                    Add Event
                </router-link>
                </div>
        </div>
    <div class="search-bar">
        <input
            placeholder="Search..."
            :value="search_input"
            @input="search_input = $event.target.value"
            class="search-input"
            @keyup.enter="fetchEvents(1,search_input)"
        />
    </div>
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
    <div
        class="pagination"
        v-if="events.next !== null && events.previous !== null"
    >
        <div class="pagination-back" @click="pagination(-1)">&lt;</div>
        <div
            class="pagination-number"
            v-for="page in paginationNumbers.items"
            :key="page"
            :class="{
                'pagination-selected': page === paginationDetails.page,
                'pagination-number': page !== paginationDetails.page,
            }"
            @click="fetchEvents(page)"
        >
            {{ page }}
        </div>
        <div class="pagination-next" @click="pagination(1)">&gt;</div>
    </div>
</template>
<script setup>
import EventCard from "./EventCard.vue";
import { ref, onMounted, reactive, watch } from "vue";
import axios from "axios";

const events = ref([]);
const paginationDetails = reactive({
    next: null,
    previous: null,
    count: -1,
    page: 1,
    page_size: 3,
    totalPages: 0,
});
const paginationNumbers = reactive({
    items: [],
});
const search_input = ref("");

let debounceTimeout = null;

async function populatePagination() {
    const totalPages = Math.ceil(paginationDetails.count / 3);
    paginationDetails.totalPages = totalPages;
    paginationNumbers.items = new Array(totalPages);
    for (let i = 1; i <= totalPages; i++) {
        console.log(`totalPages: ${totalPages}`);
        console.log(`i: ${i}`);
        paginationNumbers.items[i-1] = i;
    }
    console.log(paginationNumbers.items);
}
async function fetchEvents(page=paginationDetails.page,search=search_input.value,page_size=paginationDetails.page_size) {
    try {

        const url = process.env.VUE_APP_API_URL;
        const response = await axios.get(
            url + `/api/events?search=${search}&page_size=${page_size}&page=${page}`
        );
        events.value = [];
        events.value = response.data.results;
        paginationDetails.next = response.data.next;
        paginationDetails.previous = response.data.previous;
        paginationDetails.count = response.data.count;
        paginationDetails.page = page;
        search_input.value = search;
        populatePagination();

    } catch (error) {
        console.error("Error fetching events:", error);
    }
}
// paginationnext
// paginationback
async function pagination(diff=1){
    if (paginationDetails.page + diff > paginationDetails.totalPages) {
        return;
    }
    if (paginationDetails.page + diff < 1) {
        return;
    }
    paginationDetails.page += diff;
    fetchEvents(paginationDetails.page,search_input.value,paginationDetails.page_size);
}
onMounted(() => {
    fetchEvents(1);
});

// Debounce search
watch(search_input, (newVal) => {
    if (debounceTimeout) clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(() => {
        fetchEvents(1, newVal);
    }, 300);
});
</script>

<style src="../assets/style.css" scoped></style>
