<template lang="">
    <div class="layout">
        <div>
              <label for="">margin:</label>
        <input type="text" class="input-box" v-model="marginString">;
        </div>
        <div>
              <label for="">padding:</label>
        <input type="text" class="input-box" v-model="paddingString">;
        </div>
        <br>
      
        <box :marginString="marginString" :paddingString="paddingString" />
    </div>
</template>
<script>

export default {
    data(){
        return{
            marginString:"0",
            paddingString:"0"
        }
    },
    components:{
        'box':()=>import('./MarginPaddingBox.vue')
    }
}
</script>
<style scoped>
.layout{
    margin-bottom: 2rem;
    /* height: 30vh;
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    align-items: center; */
}
.input-box{
    width: 30%;
    text-align: center;
    border: 1px solid #ccc;
    height: 1rem;
    border-radius: .1rem;
}
</style>