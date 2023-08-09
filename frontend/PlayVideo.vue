<template>
  <div>
    <video ref="videoPlayer" controls @timeupdate="updateSubtitle">
      <track v-for="(subtitle, index) in subtitles" :key="index" :src="subtitle.src" :default="index === 0" />
    </video>
  </div>
</template>

<script>
export default {
  props: ['subtitles'],
  methods: {
    updateSubtitle(event) {
      const videoTime = this.$refs.videoPlayer.currentTime;
      // Implement logic to update subtitle based on video time
    },
  },
};
</script>
