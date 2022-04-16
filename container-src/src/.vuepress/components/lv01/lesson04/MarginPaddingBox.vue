<template lang="">
    <div class="layout" :style="{
        '--margin':marginString,
        '--padding':paddingString
        }
    ">

        <div class="layout-col">
            <div class="box"><div class="box2"></div></div>
            <div class="box"><div class="box2"></div></div>
        </div>
       
        <div class="layout-col">
            <div class="box"><div class="box2"></div></div>
            <div class="box"><div class="box2"></div></div>
        </div>

    </div>
</template>
<script>
export default {
  props: ["marginString", "paddingString"],
};
</script>
<style scoped>
.layout {
  display: flex;
  background-color: gray;
    border-radius: .3rem;

}
.box {
    border-radius: .3rem;
  width: 5rem;
  height: 5rem;
  background-color: #ffc433;
  margin: var(--margin);
  padding: var(--padding);
}
.box .box2 {
    border-radius: inherit;

  background-color: #24AF43;
    width: 2rem;
  height: 2rem;
  margin: 0;
  padding: 0;
}
</style>