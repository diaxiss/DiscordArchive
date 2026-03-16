<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { api_url } from '../constants';

const router = useRouter()

const servers = ref<any[]>([]);

onMounted(async() => {
    servers.value = (await axios.get('http://localhost:8000/servers')).data.servers
    console.log(servers.value)
})
</script>

<template>
    <div class="server-sidebar">
        <div class="direct-messages">
            <img
                class="server-image"
                :src = "`${api_url}/data/guild_icons/0.png`"
                @click="router.push('/channels/@me')"/>
        </div>
        <div v-for="server in servers" :key="server.id"
            class="server-container">
            <img 
                class="server-image" 
                :src="`${api_url}/data/guild_icons/${server.image}`"
                @click="router.push(`/server/${server.id}/${server.first_channel}`)"
            />
        </div>
    </div>
</template>

<style>

.server-sidebar{
    position: sticky;
    top: 0;
    overflow-y: auto;
    background-color: #000000;
    height:100vh;
    min-width: 75px;
}

.server-container{
    display: flex;
    position: relative;
}

.server-image{
    height: 50px;
    border-radius: 30px;
    padding: 10px;
}

.server-image:hover{
    border-radius: 20px;
}

.server-container:hover::before{
    align-self: center;
    position: absolute;
    content: "";
    padding: 10px 2px;
    border-radius: 10px;
    background-color: white;
}

</style>