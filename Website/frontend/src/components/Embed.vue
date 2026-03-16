<script setup lang="ts">

const props = defineProps<{
    embed: any
}>()

const emits = defineEmits<{
  (e: 'zoom', url: string): void
}>()

function enableAutoplay(event: Event){
  const el = event.currentTarget as HTMLVideoElement
  el.play()
}

function disableAutoplay(event: Event){
  const el = event.currentTarget as HTMLVideoElement
  el.pause()
}
</script>


<template>

    <video 
        v-if="!props.embed.url.includes('youtube.com')"
        loop muted autoplay playsinline
        preload="none"
        @loadstart="disableAutoplay"
        @mouseenter="enableAutoplay"
        @mouseleave="disableAutoplay"
        @click="$emit('zoom', props.embed.url)">
        <source :src="props.embed.url"/>
    </video>
    <iframe
        v-if="props.embed.url.includes('youtube.com')"
        class="yt-embed-iframe"
        :src="props.embed.url"
        frameborder="0"
        allow="autoplay; fullscreen"
        scrolling="no"
        loading="lazy">
    </iframe>

</template>