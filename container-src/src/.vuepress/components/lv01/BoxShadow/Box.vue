<template>
    <div class="box" :style="`box-shadow: ${boxShadowString} ;`">
        
    </div>
</template>
<script>
export default {
    props:["boxShadowString"]
}
</script>
<style scoped>
.box{
    background-color: yellow;
    width: 20vw;
    height: 20vh;
}
</style>