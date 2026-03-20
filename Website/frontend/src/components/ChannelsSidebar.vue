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

<style lang="css" scoped src="../styles/ChannelsSidebar.css"/>