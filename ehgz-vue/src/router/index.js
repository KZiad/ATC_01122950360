// filepath: c:\Users\ziadk\Desktop\Areeb Challenge\Ehgz\ehgz-vue\src\router\index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import LoginPage from '../views/LoginPage.vue';
import SignUpPage from '../views/SignUpPage.vue';
import EventDetailsPage from '../views/EventDetailsPage.vue';
import EditEvent from '@/views/EditEvent.vue';
import AddEvent from '@/views/AddEvent.vue';
import CongratulationsPage from '@/views/CongratulationsPage.vue';
import BookingDetails from '@/views/BookingDetails.vue';
import AdminPanel from '@/views/AdminPanel.vue';

const routes = [
    { path: '/', component: HomePage, name: 'Home' },
    { path: '/login', component: LoginPage, name: 'Login' },
    { path: '/sign-up', component: SignUpPage, name: 'SignUp' },
    { path: "/details/:id", component: EventDetailsPage, name: "EventDetails" },
    {path: "/details/:id/edit", component: EditEvent, name: "EventEdit"},
    {path: "/details/:id/congratulations", component: CongratulationsPage, name: "CongratulationsPage"},
    {path: "/details/:id/booking", component: BookingDetails, name: "BookingDetails"},
    {path:"/admin",component: AdminPanel,name:"AdminPanel"},

    {path:"/addevent",component: AddEvent,name:"AddEvent"},
    {path:"/:pathMatch(.*)*", redirect: "/"},
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;