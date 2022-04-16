<template lang="" >
    <div class="layout" :style="'--colorString:'+colorString">
        
        <p class="text">A</p>    
    </div>
</template>
<script>
export default {
  props: ["colorString"],
};
</script>
<style scoped>
.layout {
  position: relative;
  width: 100%;
  height: 20vh;
}
.layout::before {
  content: "";
  border-radius: 0.5rem;
  width: 100%;
  height: 5rem;
  background-color: var(--colorString);
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.text {
  z-index: 0;
  position: absolute;
  top: 0;
  left: 50%;
  font-size: 3rem;
  margin: 0;
  transform: translateX(-50%);
}
</style>