<script setup lang="ts">
import { computed } from 'vue';
import type { Reaction } from '../interfaces';

const props = defineProps<{
    reaction: Reaction
}>()

const reactionUsers = computed(() => {
    return props.reaction.users.join(' and ')
})

</script>

<template>
    <div class="reaction-details">
        <div class="left">
            <p>{{ props.reaction.emoji }}</p>
        </div>

        <div class="right">
            <p> reacted by {{ reactionUsers }}</p>
        </div>
    </div>
</template>

<style>
.reaction-details{
    position:absolute;
    bottom: 100%;
    display: flex;
    background-color: #131416;
    border-radius: 5px;
    border: 1px solid #242426;
    align-items: center;
    width: fit-content;
    z-index: 9999;
    pointer-events: none;
}

.right > p{
    max-width: 75vw;
    padding: 10px;
}

.left:first-child{
    height: 100%;
    padding: 20px;
}
</style>