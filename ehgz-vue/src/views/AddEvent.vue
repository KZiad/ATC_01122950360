<template>
    <div class="title">
        <router-link to="/" class="back-button-back">&lt;</router-link>Add Event
    </div>
    <div class="event-inputs-container">
        <div class="event-left-inputs">
            <div class="input-container">
                <label for="event-name-label">Event Name</label>
                <input type="text" id="event-name" v-model="eventName"  />
            </div>
            <div class="input-container">
                <label for="event-date-label">Date</label>
                <input type="date" id="event-date" v-model="eventDate" />
            </div>
            <div class="input-container">
                <label for="event-time-label">Time</label>
                <input type="time" id="event-time" v-model="eventTime"/>
            </div>
            <div class="input-container">
                <label for="event-venue-label">Venue</label>
                <input type="text" id="event-venue" v-model="eventVenue"/>
            </div>
            <div class="input-container">
                <label for="event-price-label">Price (EGP)</label>
                <input type="number" id="event-price" v-model="eventPrice" />
            </div>
            <div class="input-container">
                <label for="event-category-label">Category</label>
                <select id="event-category" v-model="eventCategory">
                    <option value="" disabled selected>Select a category</option>
                    <option v-for="category in categories" :key="category" :value="category.id">{{ category.name }}</option>
                </select>
            </div>
        </div>
        <div class="event-right-inputs">
            <div
                class="image-upload-container"
                @click="triggerFileSelect"
                @dragover.prevent="dragOver = true"
                @dragleave.prevent="dragOver = false"
                @drop.prevent="handleDrop"
                :class="{ dragging: dragOver }"
            >
                <input
                    type="file"
                    ref="fileInput"
                    accept="image/*"
                    hidden
                    @change="handleFileChange"
                />
                <img :src="previewUrl || defaultPlaceholder" alt="Preview" />
            </div>
                <div class="textarea-container">
                        <label for="event-description-label">Description</label>
                        <textarea id="event-description" rows="4" v-model="eventDescription"></textarea>
                </div>
        </div>
    
    </div>
    <div class="tag-submit-container">
        <div class="tag-input-container">
                <label for="event-tags-label">Tags</label>
                <input type="text" id="event-tags" v-model="tags" placeholder="Add tags separated by commas (tag,tag,tag)" />
        </div>
        <div class="submit-button-container" @click="submitEvent">
            Submit
        </div>
    </div>

</template>

<script setup>
import { inject, onMounted, reactive } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const isAdmin = inject("isAdmin");
if (!isAdmin) {
    router.push("/");
}
import { ref } from 'vue';
import axios from "axios";
        
const fileInput = ref(null);
const previewUrl = ref('');
const dragOver = ref(false);

const defaultPlaceholder = require("../assets/upload-placeholder.png");

function triggerFileSelect() {
  fileInput.value.click();
}

function handleFileChange(event) {
  const file = event.target.files[0];
  if (file && file.type.startsWith('image/')) {
    readFile(file);
  }
}

function handleDrop(event) {
  dragOver.value = false;
  const file = event.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) {
    readFile(file);
  }
}

function readFile(file) {
  const reader = new FileReader();
  reader.onload = () => {
    previewUrl.value = reader.result;
  };
  reader.readAsDataURL(file);
}
const eventName = ref('');
const eventDate = ref('');
const eventTime = ref('');
const eventVenue = ref('');
const eventPrice = ref('');
const eventCategory = ref('');
const eventDescription = ref('');
const eventTags = ref([]);
const tags = ref('');
const url = process.env.VUE_APP_API_URL;
const categories = reactive([]);

async function populateCategories() {
    const data = await axios.get(`${url}/api/events/category`);
    for (let i = 0; i < data.data.length; i++) {
        categories.push(data.data[i]);
    }
}
async function cleanTags() {
    const tagsArray = tags.value.split(',');
    for (let i = 0; i < tagsArray.length; i++) {
        tagsArray[i] = tagsArray[i].trim();
    }
    eventTags.value = JSON.stringify(tagsArray);
  
}

async function submitEvent() {
    await cleanTags();
    const formData = new FormData();
    formData.append('name', eventName.value);
    formData.append('date', eventDate.value + 'T' + eventTime.value);
    formData.append('venue', eventVenue.value);
    formData.append('description', eventDescription.value);
    formData.append('price', eventPrice.value);
    formData.append('category', eventCategory.value);
    formData.append('tags', eventTags.value);
    if (fileInput.value.files[0]) {
        formData.append('image', fileInput.value.files[0]);
    }
    
    try {
        const response = await axios.post(`${url}/api/events/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        router.push("/details/" + response.data.id);
    } catch (error) {
        console.error("Error submitting the event:", error);
    }
}

onMounted(() => {
    populateCategories();
});
</script>


<style scoped>
input[type="file"]{
        display: none;
}
.image-upload-container {
  max-width: 500px;
  width: 100%;
  border: 2px dashed #ccc;
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  background-color: #f9f9f9;
  transition: border-color 0.3s;
  aspect-ratio: 517/340;
}

.image-upload-container:hover {
  border-color: #794cd1;
}

.image-upload-container.dragging {
  border-color: #794cd1;
}

.image-upload-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
<style src="../assets/style.css"></style>
