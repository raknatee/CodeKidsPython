<template lang="">
    <div class="layout">

        <div>
        <label for="colorString">background-color:</label>
        
        <input type="text" id="colorString" class="input-box" v-model="colorString">;
        </div>
        
        <box :colorString="colorString"/>
    </div>
</template>
<script>

export default {
    data(){
        return{
            colorString:"#FFC43380"
        }
    },
    components:{
        'box':()=>import('./BoxColor.vue')
    }
}
</script>
<style scoped>
.layout{
    height: 30vh;
    display: flex;
    justify-content: space-around;
    flex-direction: column;
   
}
.input-box{
    width: 30%;
    text-align: center;
    border: 1px solid #ccc;
    height: 1rem;
    border-radius: .1rem;
}
</style>