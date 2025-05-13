// filepath: c:\Users\ziadk\Desktop\Areeb Challenge\Ehgz\ehgz-vue\src\router\index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import SignInPage from '../views/SignInPage.vue';
import SignUpPage from '../views/SignUpPage.vue';
import EventDetailsPage from '../views/EventDetailsPage.vue';
import EditEvent from '@/views/EditEvent.vue';
import AddEvent from '@/views/AddEvent.vue';

const routes = [
    { path: '/', component: HomePage, name: 'Home' },
    { path: '/sign-in', component: SignInPage, name: 'SignIn' },
    { path: '/sign-up', component: SignUpPage, name: 'SignUp' },
    { path: "/details/:id", component: EventDetailsPage, name: "EventDetails" },
    {path: "/details/:id/edit", component: EditEvent, name: "EventEdit"},
    {path:"/addevent",component: AddEvent,name:"AddEvent"},
    {path:"/:pathMatch(.*)*", redirect: "/"},
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;