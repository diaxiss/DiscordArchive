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

<style lang="css">

.reactions-container{
    position: relative;
    display: flex;
    align-items: center;
    gap: 5px;
}

.reaction-container{
    display: flex;
    align-items: center;
    background-color: #27272B;
    color: #9D9EA5;
    padding: 3px 6px;
    border-radius: 5px;
    border: 1px solid rgba(0,0,0,0);
    font-size: 14px;
    gap: 5px;
}

.reaction-container > p{
    color: #9D9EA5
}

.reaction-container:hover{
    background-color: #303034;
    border: 1px solid #3F3F45;
    cursor: pointer;
}

.reaction-container:hover > p{
    color: #E4E4E6;
}

.hidden{
    display: none;
}
</style>