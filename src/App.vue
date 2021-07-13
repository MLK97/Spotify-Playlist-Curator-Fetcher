<template>
  <div id="nav">
    <router-link to="/">Authorize</router-link> |
    <router-link to="/search">Search</router-link>
  </div>
  <router-view/>
</template>

<style lang="scss">
$black: #191414;
$green: #1db954;
$gray: #2D2424;

@import url('https://fonts.googleapis.com/css2?family=Signika:wght@300;500&display=swap');

body {
    background-color: $black;
    color: white;
    text-align: center;
    font-family: 'Signika', sans-serif;
}

</style>
