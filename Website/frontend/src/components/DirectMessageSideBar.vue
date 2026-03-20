<script setup lang="ts">
import { useRouter } from 'vue-router';
import { api_url } from '../constants';

const router = useRouter()
const props = defineProps<{
    dms: any[]
}>()


</script>

<template>
    <div class="dm-sidebar">
        <div
            class="dm"
            v-for="dm in dms"
            @click="router.push(`/channels/@me/${dm.id}`)">
            <img class="user-image" :src="`${api_url}/data/avatars/${dm.image}`"/>
            <p>{{dm.name}}</p>
        </div>
    </div>
</template>

<style lang="css" scoped src="../styles/DirectMessageSideBar.css"/>