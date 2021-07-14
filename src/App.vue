<template>
    <router-link to="/search" tag="button">
      <button class="searchLink">
        Search
      </button>
    </router-link>
    <router-link to="/auth" tag="button">
      <button class="authLink">
        Authorize
      </button>
    </router-link>
  <router-view/>
</template>

<style lang="scss">
$black: #121212;
$green: #1db954;
$gray: #2D2424;

@import url('https://fonts.googleapis.com/css2?family=Signika:wght@300;500&display=swap');

body {
    background-color: $black;
    color: white;
    text-align: center;
    font-family: 'Signika', sans-serif;
}

.searchLink {
  color: white;
  background-color: $green;
  width: 500px;
  height: 80px;
  border-radius: 500px;
}

.authLink {
  color: white;
  border: 3px $green solid;
  width: 500px;
  height: 80px;
  background-color: $black;
  border-radius: 500px;
}

</style>
