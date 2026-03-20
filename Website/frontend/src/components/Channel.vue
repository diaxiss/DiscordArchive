<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import FullscreenImage from '../components/FullscreenImage.vue';
import Attachment from './Attachment.vue';
import Embed from './Embed.vue';

import type { Message } from '../interfaces';
import Reactions from './Reactions.vue';
import { api_url } from '../constants';

const props = defineProps<{
  channel: String
}>()

const messages = ref<Message[]>([]);
const fullscreenImage = ref<string>('');

const offset = ref<number>(0);
const loading = ref<boolean>(false);
const allLoaded = ref<boolean>(false);
const container = ref<HTMLElement | null>(null)

function formatDate(date: Date){
  let string = date.toLocaleString('en-GB', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  })
  return string
}

function checkScrollEnd(){
  if(!container.value){
    return
  }

  if(-container.value?.scrollTop + container.value?.clientHeight >= container.value?.scrollHeight - 2){
    loadMoreMessages()
  }
}

async function loadMoreMessages(){
  if (loading.value || allLoaded.value){
    return
  }
  offset.value += 20
  loading.value = true
  const newMessages = (await axios.get(`${api_url}/channel/${props.channel}?offset=${offset.value}`)).data.messages
  if (newMessages.length === 0){
    allLoaded.value = true
  }
  messages.value.push(...newMessages)
  loading.value = false

}


function setFullscreenImage(url: string){
  fullscreenImage.value = url
}


onMounted(async() => {
  messages.value = (await axios.get(`${api_url}/channel/${props.channel}`)).data.messages
})

</script>

<template>

  <FullscreenImage
    :source="fullscreenImage"
    @close="fullscreenImage = ''"
  />

  <ol
    class="messages-container"
    ref="container"
    :class="{'no-scroll': fullscreenImage}"
    @scrollend="checkScrollEnd">

    <li v-for="message in messages" :key="message.id" class="message">

      <div class="left">
        <img 
          :src="`${api_url}/data/avatars/${message.author.avatar_url}`"
          style="height: 50px; width: 50px; border-radius: 50px;"/>
      </div>
      
      <div class="right">

        <div class="author">
          <h3>{{ message.author.nickname }}</h3>
          <p class="sent-date">{{ formatDate(new Date(message.created_at)) }}</p>
        </div>

        <div>
          <pre class="message-content">{{ message.content }}</pre>

          <div v-for="embed in message.embeds">
            <Embed
              :embed="embed"
              @zoom="setFullscreenImage"
            />  
          </div>

          <div v-for="attachment in message['attachments']">

            <Attachment
              :attachment="attachment"
              @zoom="setFullscreenImage"
              />

          </div>

          <Reactions
            v-if="message.reactions.length > 0"
            :reactions="message.reactions"
          />

        </div>
      </div>
    
    </li>
  </ol>
</template>

<style lang="css" scoped src="../styles/Channel.css"/>