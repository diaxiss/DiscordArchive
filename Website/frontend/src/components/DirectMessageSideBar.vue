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

<style>

.dm-sidebar{
    position: sticky;
    top: 0;
    height: 100vh;
    width: 200px;
    overflow: scroll;
    border: 1px solid #1E1E20;
    background-color: #000000;
}

.dm{
    display: flex;
    width: 100%;
    margin: 10px;
    border-radius: 10px;
    align-items: center;
}

.dm:hover{
    background-color: #121213;
}

.dm > p{
    font-size: 14px;
    width: 100%;
    white-space: "none";
    overflow-x: hidden;
    text-overflow: ellipsis;
}

.user-image{
    height: 30px;
    border-radius: 50px;
    padding: 5px;
}
</style>