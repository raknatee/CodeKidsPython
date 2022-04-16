<template lang="">
    <div class="layout">
        <div>
        <label for="bs">box-shadow:</label>
        <input id="bs"  class="input-box" type="text" v-model="boxShadowString">;
        </div>
       
        <box :boxShadowString="boxShadowString" />
    </div>
</template>
<script>
export default {
    data(){
        return{
        boxShadowString:"1rem 1rem 1rem 1rem rgba(0, 0, 0, 0.5)"
        }
    },
    components:{
        "box": ()=>import("./Box.vue")
    }
}
</script>
<style scoped>
.layout{
    height: 50vh;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;

}

</style>