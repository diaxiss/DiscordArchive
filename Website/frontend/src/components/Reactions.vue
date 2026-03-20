<script setup lang="ts">
import { ref } from 'vue';
import type { Reaction } from '../interfaces';
import ReactionHoverDetails from './ReactionHoverDetails.vue';


const props = defineProps<{
    reactions: Reaction[]
}>()

const hover = ref<boolean>(false);
const focusedReaction = ref<Reaction | null>(null);


console.log(props.reactions)
</script>

<template>
    <div class="reactions-container">
        <div v-for="reaction in props.reactions"
            class="reaction-container"
            @mouseenter="hover=true; focusedReaction = reaction"
            @mouseleave="hover=false; focusedReaction = null"
            >
            <p>{{ reaction.emoji }}</p>
            <p>{{ reaction.users.length }}</p>
        </div>
        <ReactionHoverDetails
            :class="{display: hover}"
            v-if="focusedReaction !== null"
            :reaction="focusedReaction"
        />
    </div>

</template>

<style lang="css" scoped src="../styles/Reactions.css"/>