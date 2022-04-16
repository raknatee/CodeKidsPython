<template>
  <div>
    <h3 style="color: #6d32a8">parent</h3>
    <h3 style="color: #009921">child</h3>
    <div class="parent">
      <div class="child ch1">width: 100%</div>
      <div class="child ch2">width: 50%</div>
      <div class="child ch3">width: 110%</div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
.parent {
  border: 0.5rem solid #6d32a8;
  height: 30rem;
  border-radius: 0.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.child {
  text-align: center;
  background-color: #009921;
  color: whitesmoke;
  font-size: 2rem;
}
.ch1 {
  width: 100%;
}
.ch2 {
  width: 50%;
}
.ch3 {
  width: 110%;
}
</style>