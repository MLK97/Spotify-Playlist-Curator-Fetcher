<template>
  <form class="search" method="POST">
        <input autocapitalize="none" autocorrect="off" :placeholder="placeholderValue" v-model="searchValue" type="search" class="search_text">
        <button class="search_button" v-on:click="search(searchValue)">Search</button>   
  </form>
</template>

<script>
export default {
  name: 'Search',
  props: {
    placeholderValue: String,
  },
  data() {
    return {
      searchValue: "" 
    }
  },
  methods: {
    search: function () {
      var SpotifyWebApi = require('spotify-web-api-node');
      var spotifyApi = new SpotifyWebApi();

    spotifyApi.getAlbum('5U4W9E5WsYb2jUQWePT8Xm').then(
      function(data) {
        alert('Album information', data.body);
      }, 
      function(err) {
        alert(err);
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
$black: #191414;
$green: #1db954;
$gray: #2D2424;

@import url('https://fonts.googleapis.com/css2?family=Signika:wght@300;500&display=swap');

form {
    width: 90%;
    background-color: $black;
    border-bottom: 1px solid white;
    padding-bottom: 10px;
    display: inline-block;

    &:focus {
        outline: none;
    }
}

.search_text {
    border: none;
    width: 88%;
    background-color: $black;
    color: white;
    height: 40px;
    border-radius: 3px;
    transition: 0.3s;
    
    &:focus {
        outline: none; 
        background-color: $gray;
    }
}


.search_button {
    background-color: $green;
    border-radius: 25px;
    color: white;
    border: none;
    padding: 0 20px;
    letter-spacing: 0.1em;
    text-align: center;
    height: 40px;
    width: 10%;
}
</style>
