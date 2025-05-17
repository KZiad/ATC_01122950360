<script setup>
import { inject, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import EventList from "@/components/EventList.vue";

const router = useRouter();
const isAdmin = inject("isAdmin");
if (!isAdmin.value) {
    router.push("/");
}

const showCategoryModal = ref(false);
const categoryName = ref("");
const loading = ref(false);
const errorMsg = ref("");
const successMsg = ref("");

async function submitCategory() {
    errorMsg.value = "";
    successMsg.value = "";
    if (!categoryName.value.trim()) {
        errorMsg.value = "Category name is required.";
        return;
    }
    loading.value = true;
    try {
        const url = process.env.VUE_APP_API_URL;
        await axios.post(url + "/api/events/category/", { name: categoryName.value });
        successMsg.value = "Category created!";
        categoryName.value = "";
        setTimeout(() => {
            showCategoryModal.value = false;
            successMsg.value = "";
        }, 1000);
    } catch (e) {
        errorMsg.value = "Failed to create category.";
    } finally {
        loading.value = false;
    }
}
</script>

<template>
    <div class="events">Admin Panel</div>
    <div class="admin-buttons">
        <div class="add-event">
            <router-link to="/addevent" class="admin-button admin-button-text" v-if="isAdmin">
                Add Event
            </router-link>
        </div>
        <div class="add-event">
            <div class="admin-button admin-button-text" v-if="isAdmin" @click="showCategoryModal = true">
                Create Category
            </div>
        </div>
    </div>

    <!-- Floating Modal for Create Category -->
    <div v-if="showCategoryModal" class="modal-overlay">
        <div class="modal-content">
            <button class="close-btn" @click="showCategoryModal = false">&times;</button>
            <label for="categoryName">Category Name:</label>
            <input id="categoryName" v-model="categoryName" class="modal-input" />
            <button class="submit-btn" @click="submitCategory" :disabled="loading">
                {{ loading ? "Creating..." : "Submit" }}
            </button>
            <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
            <div v-if="successMsg" class="success-msg">{{ successMsg }}</div>
        </div>
    </div>

    <EventList />
</template>

<style src="../assets/style.css" scoped></style>
<style scoped>
.admin-button {
  background: #794cd1;
  border-radius: 15px;
  width: 100px;
  height: 100%;
  cursor: pointer;
}
.admin-button-text {
  color: #ffffff;
  text-align: center;
  font-family: "Segoe UI", sans-serif;
  font-size: 17px;
  line-height: 150%;
  font-weight: 450;
  top: 50%;
  width:max-content;
  padding: 10px;
  height: 39.4px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
}
.admin-buttons {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  gap:10px;
}

/* Modal styles */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.modal-content {
  background: #fff;
  padding: 30px 24px 24px 24px;
  border-radius: 12px;
  min-width: 320px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.2);
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.close-btn {
  position: absolute;
  top: 8px;
  right: 12px;
  background: none;
  border: none;
  font-size: 22px;
  cursor: pointer;
}
.modal-input {
  padding: 8px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 16px;
}
.submit-btn {
  background: #794cd1;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 16px;
  cursor: pointer;
}
.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
.error-msg {
  font-family: "Segoe UI", sans-serif;
  color: #d32f2f;
  font-size: 14px;
}
.success-msg {
  font-family: "Segoe UI", sans-serif;
  color: #388e3c;
  font-size: 14px;
}
label {
  font-family: "Segoe UI", sans-serif;
}
</style>