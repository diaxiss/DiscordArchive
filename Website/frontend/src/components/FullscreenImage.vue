<script setup lang="ts">
import { computed, ref } from 'vue';
import { api_url, image_extentions } from '../constants';


const props = defineProps<{
    source: string
}>()

const emits = defineEmits<{
    (e: 'close'): void
}>()

const isZoomed = ref<boolean>(false);

const fileExtention = computed(() => {
    return props.source.split('.').pop()?.toLowerCase() as string
})

function toggleZoom(event: any){
    event.stopPropagation()

    // zoom-in
    if (!isZoomed.value){
        event.target.style.transform = "scale(2.0, 2.0)"
        event.target.style.cursor = "zoom-out"
    }
    // reset
    else{
        event.target.style.transform = "scale(1.0, 1.0)"
        event.target.style.cursor = "zoom-in"
    }

    isZoomed.value = !isZoomed.value
}

</script>
<template>
    <div
        v-if="props.source"
        class="fullscreen-image-container"
        @click="$emit('close')">
        <img
            v-if="image_extentions.includes(fileExtention)"
            class="fullscreen-item"
            :src="`${api_url}/data/media/${$props.source}`"
            @click="toggleZoom"/>

        <video
            v-else
            class="fullscreen-item"
            loop muted autoplay playsinline
            @click="toggleZoom">
            <source :src="props.source"
        </video>
    </div>
</template>

<style lang="css" scoped src="../styles/FullscreenImage.css"/>