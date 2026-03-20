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

<style lang="css" scoped src="../styles/ServerSideBar.css"/>