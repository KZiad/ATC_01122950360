<template>
    <div class="loading-container">
        <div class="loading-circle"></div>
    </div>
</template>

<style scoped>
.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 200px;
}
.loading-circle {
    border: 6px solid #f3f3f3;
    border-top: 6px solid #794cd1;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    animation: spin 1s linear infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg);}
    100% { transform: rotate(360deg);}
}
</style>