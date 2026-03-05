<script setup lang="ts">
import { useRouter } from 'vue-router';


const router = useRouter()

const props = defineProps<{
    channels: any[],
    server_id: string
}>()

</script>

<template>
    <div class="channels-sidebar">
        <div 
            v-for="channel in channels"
            class="channel-container"
            @click="router.push(`/server/${props.server_id}/${channel.id}`)"
        >
            <div class="name-container">
                <p class="channel-icon">{{ channel.type === 'text' ? "#" : ''}}</p>
                <p class="channel-name">{{ channel.name }}</p>
            </div>
        </div>
    </div>
</template>

<style>

span{
    padding: 0;
    margin: 0;

    overflow: hidden;
    font-size: 20px
}

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
    border-radius: 5px;
    padding: 10px;
}

.channel-container:hover{
    background-color: #121213;
}

.name-container{
    display: flex;
    gap: 10px;
    width: 100%;
    align-items: center;
}

.channel-icon{
    font-size: 20px;
    color: white;
}

.channel-name{
    height: 100%;
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    color: #7A7B83

}

</style>