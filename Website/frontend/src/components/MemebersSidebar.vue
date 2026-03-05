<script setup lang="ts">

const props = defineProps<{
    members: any[]
}>()

</script>

<template>
    <div class="members-sidebar">
        <div class="member" v-for="member in members">
            <img 
                class="avatar"
                :src="`http://localhost:8000/data/avatars/${member.image}`"/>
            <p>{{ member.display_name }}</p>
        </div>
    </div>
</template>

<style>

.members-sidebar{
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 10vw;
    min-width: 200px;
    gap: 10px;
    overflow-y: auto;
}

.member{
    display: flex;
    align-items: center;
    padding: 5px;
    border-radius: 10px;
}

.member:hover{
    background-color: #18181B;
    cursor: pointer;
}

.member > p{
    white-space: "none";
    overflow-x: hidden;
    text-overflow: ellipsis;
}

.avatar{
    height: 30px;
}
</style>