<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute()

const props = defineProps<{
    channels: any[],
    server_id: string
}>()
</script>

<template>
    <div class="channels-sidebar">
        <RouterLink 
            v-for="channel in channels"
            class="channel-container"
            :to="`/server/${props.server_id}/${channel.id}`"
        >
            <div class="name-container" :class="{selected: route.params.channel_id == channel.id}">
                <p class="channel-icon">{{ channel.type === 'text' ? "#" : ''}}</p>
                <p class="channel-name">{{ channel.name }}</p>
            </div>
        </RouterLink>
    </div>
</template>

<style>

.channels-sidebar{
    display: flex;
    flex-direction: column;
    gap: 5px;
    position: sticky;
    top: 0;
    overflow-y: auto;
    background-color: #000000;
    height:100vh;
    width: 250px;
    max-width: 200px;
}

.channels-sidebar::after{
    padding: 20px;
    border: 4px solid white;
}

.channel-container{
    display: flex;
    align-items: center;
    box-sizing: border-box;
    max-height: 40px;
    width: 100%;
    border-radius: 10px;
    padding: 5px 10px;
    text-decoration: none;
}

.name-container{
    display: flex;
    gap: 10px;
    width: 100%;
    align-items: center;
}

.name-container p{
    color: #7A7B83
}

.channel-icon{
    font-size: 20px;
}

.channel-name{
    height: 100%;
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.router-link-active{
    background-color: #242426;
    color: #E2E2E4;
}

.router-link-active p{
    color: #E2E2E4;
}

.channel-container:hover:not(.router-link-active){
    background-color: #121213;
}

.channel-container:hover:not(.router-link-active) p{
    color: #E4E4E6;
}

</style>