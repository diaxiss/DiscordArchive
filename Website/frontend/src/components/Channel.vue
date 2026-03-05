<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import FullscreenImage from '../components/FullscreenImage.vue';

const props = defineProps<{
  channel: String
}>()


const messages = ref<any[]>([]);
const fullscreenImage = ref<string>('');

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

function enableAutoplay(event: MouseEvent){
  const el = event.currentTarget as HTMLVideoElement
  el.play()
}

function disableAutoplay(event: MouseEvent){
  const el = event.currentTarget as HTMLVideoElement
  el.pause()
}


onMounted(async() => {
  messages.value = (await axios.get(`http://localhost:8000/channel/${props.channel}`)).data.messages
  console.log(messages.value)
})

</script>

<template>

  <FullscreenImage
    :image="fullscreenImage"
    @close="fullscreenImage = ''"
  />

  <ol
    class="messages-container" 
    :class="{'no-scroll': fullscreenImage}">

    <li v-for="message in messages" :key="message.id" class="message">

      <div class="left">
        <img 
          :src="`http://localhost:8000/data/avatars/${message.author.avatar_url}`"
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
            <video
              v-if="!embed.url.includes('youtube.com')"
              loop autoplay muted playsinline
              preload="none"
              @mouseenter="enableAutoplay"
              @mouseleave="disableAutoplay">
                <source :src="embed.url"/>
            </video>
            <iframe
                v-else
                class="yt-embed-iframe"
                :src="embed.url"
                frameborder="0"
                allow="autoplay; fullscreen"
                scrolling="no"
                loading="lazy">
            </iframe>  
          </div>

          <div v-for="attachment in message['attachments']">

            <img
              v-if="['png', 'jpg', 'jpeg', 'gif', 'apng', 'gifv', 'webm'].includes(attachment.url.split('.').pop().toLowerCase())"
              loading="lazy"
              :src="`http://localhost:8000/data/media/${attachment.url}`"
              @click="fullscreenImage = attachment.url"/>

            <video
              v-if="['mp4'].includes(attachment.url.split('.').pop().toLowerCase())"
              controls>
              <source :src="attachment.url"/>
            </video>

            <audio
              v-if="['ogg', 'mp3', 'wav'].includes(attachment.url.split('.').pop().toLowerCase())"
              controls>
              <source :src="attachment.url"/>
            </audio>

          </div>

        </div>
      </div>
    
    </li>
  </ol>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

*{
  margin: 0px;
  padding: 0px;
  color: #E4E4E6;
  font-family: "Roboto", sans-serif;
}

body, html, #app{
  height: 100%;
}

body{
  background-color: #070709;
  overflow: hidden;
}

.messages-container{
  height: 100%;
  width: 100%;
  overflow-y: scroll;
}

.messages-container.no-scroll{
  overflow: hidden;
}

.message{
  display: flex;
  width: 90%;
  border-radius: 0 5px 5px 0;
  word-wrap: break-word;
  overflow-wrap: anywhere;
  gap: 1rem;
  margin-bottom: 2rem;
}

.message:hover{
  background-color: #18181B;
}

.author{
  display:flex;
  align-items:start;
  gap: 1rem;
}

.name-date-container{
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
}

.name-date-container > *{
  margin: 0;
}

.sent-date{
  color: #767780;
}

.message-content{
  color: #DCDCDF
}

.yt-embed-iframe{
    min-width: 500px;
    max-width: 600px;
    aspect-ratio: 16/9;
}

iframe{
  border-radius: 10px;
}

video{
  max-height: 300px;
  border-radius: 10px;
}

audio{
  max-height: 100px;
  border-radius: 10px;
}

img{
  max-height: 400px;
  max-width: 400px;
  border-radius: 10px;
}

</style>