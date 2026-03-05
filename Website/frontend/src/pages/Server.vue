<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import ServerSideBar from '../components/ServerSideBar.vue';
import ChannelsSidebar from '../components/ChannelsSidebar.vue';
import Channel from '../components/Channel.vue';
import { useRoute } from 'vue-router';
import MemebersSidebar from '../components/MemebersSidebar.vue';

const channels = ref<any[]>([]);
const members = ref<any[]>([]);
const route = useRoute()

async function fetch(){
    channels.value = (await axios.get(`http://localhost:8000/server/${route.params.server_id}`)).data.channels
    members.value = (await axios.get(`http://localhost:8000/server/${route.params.server_id}/members`)).data.members
}

watch(() => route.params.server_id, async() => {
    await fetch()
})

onMounted(async() => {
    await fetch()
})
</script>

<template>
    <div class="page-container">
        <ServerSideBar/>
        <ChannelsSidebar
            v-if="channels.length > 0"
            :key="route.params.server_id as string"
            :channels="channels"
            :server_id="route.params.server_id as string"
        />
        <Channel
            v-if="channels.length > 0"
            :key="route.params.channel_id as string"
            :channel="route.params.channel_id as string"
        />
        <MemebersSidebar
            :key="route.params.server_id as string"
            :members="members"
        />
    </div>
</template>

<style>
</style>