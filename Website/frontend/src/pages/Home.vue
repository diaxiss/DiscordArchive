<script setup lang="ts">

import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import Channel from '../components/Channel.vue';
import DirectMessageSideBar from '../components/DirectMessageSideBar.vue';
import ServerSideBar from '../components/ServerSideBar.vue';

const route = useRoute()
const dms = ref<any[]>([]);

onMounted(async() => {
    dms.value = (await axios.get('http://localhost:8000/dms')).data.dms
})

</script>

<template>
    <div class="page-container">
        <ServerSideBar/>
        <DirectMessageSideBar
            :dms="dms"/>
        <Channel
            v-if="route.params.channel_id"
            :key="route.params.channel_id as string"
            :channel="route.params.channel_id as string"/>
    </div>
</template>

<style lang="css" scoped src="../styles/Home.css"/>