<template lang="">
    <div class="layout">
        <div>
            <p>display: flex;</p>
        <label for="flex-direction">flex-direction:</label>
        <input id="flex-direction"  class="input-box" type="text" v-model="flexDirection">;
        <br>
        <label for="justify-content">justify-content</label>
        <input id="justify-content" class="input-box" type="text" v-model="justifyContent" >;


        <br>
            <label for="align-items">align-items</label>
        <input id="align-items" class="input-box" type="text" v-model="alignItems" >;


        <br>
            <label for="gap">gap</label>
        <input id="gap" class="input-box" type="text" v-model="gap" >;

        </div>
       
        <flex :flexDirection="flexDirection" :justifyContent="justifyContent" :alignItems="alignItems" :gap="gap"  />
    </div>
</template>
<script>
export default {
    data(){
        return{
        flexDirection:"row",
        justifyContent:"center",
        alignItems:"center",
        gap:"0"
        }
    },
    components:{
        "flex": ()=>import("./Flex.vue")
    }
}
</script>
