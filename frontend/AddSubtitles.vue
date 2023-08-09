<template>
  <div>
    <textarea v-model="subtitleText" placeholder="Subtitle text"></textarea>
    <input v-model="timestamp" type="number" placeholder="Timestamp (seconds)" />
    <button @click="addSubtitle">Add Subtitle</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      subtitleText: '',
      timestamp: 0,
    };
  },
  methods: {
    async addSubtitle() {
      const subtitleData = {
        text: this.subtitleText,
        timestamp: parseFloat(this.timestamp),
      };

      try {
        await this.$axios.post('/add_subtitle', subtitleData);
        alert('Subtitle added successfully');
      } catch (error) {
        console.error('Error adding subtitle:', error);
      }
    },
  },
};
</script>
