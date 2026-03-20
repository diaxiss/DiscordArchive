<script setup lang="ts">
import { api_url } from '../constants';


const props = defineProps<{
    members: any[]
}>()

</script>

<template>
    <div class="members-sidebar">
        <div class="member" v-for="member in members">
            <img 
                class="avatar"
                :src="`${api_url}/data/avatars/${member.image}`"/>
            <p>{{ member.display_name }}</p>
        </div>
    </div>
</template>

<style lang="css" scoped src="../styles/MembersSidebar.css"/>