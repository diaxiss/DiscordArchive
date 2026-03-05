<script setup lang="ts">

const props = defineProps({
    image: String
})

const emits = defineEmits<{
    'close': []
}>()

</script>
<template>
    <div
        v-if="props.image"
        class="fullscreen-image-container"
        @click="$emit('close')">
        <img
            class="fullscreen-image"
            :src="`http://localhost:8000/data/media/${$props.image}`"/>
    </div>
</template>

<style scoped>
.fullscreen-image-container{
    display: flex;
    position: fixed;
    top: 0;
    width: 100vw;
    height: 100vh;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    background-color: #000000AA;
}

.fullscreen-image{
    max-width: 90%;
    max-height: 90%;
}
</style>