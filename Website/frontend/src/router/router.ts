import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import Server from "../pages/Server.vue";

const routes = [
    {path: '/', component: Home},
    {path: '/server/:server_id/:channel_id', component: Server},
    {path: '/channels/@me/',
        component: Home,
        children:[
            {path: ':channel_id', component: Home}
        ]
    }
]

export const router = createRouter({
    history: createWebHistory(),
    routes: routes
})