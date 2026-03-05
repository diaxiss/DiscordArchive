<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

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
                :src = "`http://localhost:8000/data/guild_icons/0.png`"
                @click="router.push('/channels/@me')"/>
        </div>
        <div v-for="server in servers" :key="server.id">
            <img 
                class="server-image" 
                :src="`http://localhost:8000/data/guild_icons/${server.image}`"
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

.server-image{
    height: 50px;
    border-radius: 30px;
    padding: 10px;
}
</style>