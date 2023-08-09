<template>
  <div>
    <input type="file" @change="uploadVideo" />
  </div>
</template>

<script>
export default {
  methods: {
    async uploadVideo(event) {
      const videoFile = event.target.files[0];
      const formData = new FormData();
      formData.append('video', videoFile);

      try {
        await this.$axios.post('/upload_video', formData);
        alert('Video uploaded successfully');
      } catch (error) {
        console.error('Error uploading video:', error);
      }
    },
  },
};
</script>
