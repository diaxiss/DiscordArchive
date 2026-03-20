<script setup lang="ts">
import { computed } from 'vue';
import type { Attachment } from '../interfaces';
import { audio_extentions, image_extentions, video_extentions } from '../constants';


const props = defineProps<{
    attachment: Attachment
}>()

const emits = defineEmits<{
    (e: 'zoom', url: string): void
}>()

const fileExtention = computed(() => {
    return props.attachment.url.split('.').pop()?.toLowerCase() as string
})

const source = computed(() => {
    return `${import.meta.env.VITE_API_URL}/data/media/${props.attachment.url}`
})

</script>

<template>
    <img
        v-if="image_extentions.includes(fileExtention)"
        loading="lazy"
        :src="source"
        @click="$emit('zoom', props.attachment.url)"/>

    <video
        v-if="video_extentions.includes(fileExtention)"
        controls>
        <source :src="source"/>
    </video>

    <audio
        v-if="audio_extentions.includes(fileExtention)"
        controls>
        <source :src="source"/>
    </audio>
</template>

<style scoped>
img:hover{
    cursor: pointer;
}
</style>