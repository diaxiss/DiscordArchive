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

<style lang="css" scoped src="../styles/ReactionHoverDetails.css"/>