<template lang="">
    <div class="layout">
        <div>
            <p>display: grid;</p>
        <label for="grid-template-columns">grid-template-columns:</label>
        <input id="grid-template-columns"  class="input-box" type="text" v-model="gridTemplateColumns">;
        <br>
        <label for="column-gap">column-gap</label>
        <input id="column-gap" class="input-box" type="text" v-model="columnGap" >;

         <br>
        <label for="column-gap">row-gap</label>
        <input id="column-gap" class="input-box" type="text" v-model="rowGap" >;


        <br>
            <label for="align-items">align-items</label>
        <input id="align-items" class="input-box" type="text" v-model="alignItems" >;

         <br>
            <label for="justify-items">justify-items</label>
        <input id="justify-items" class="input-box" type="text" v-model="justifyItems" >;


     
        </div>
       <br>
        <grid :gridTemplateColumns="gridTemplateColumns"
        :columnGap="columnGap"
        :rowGap="rowGap"
        :alignItems="alignItems"
        :justifyItems="justifyItems"
        
        />
    </div>
</template>
<script>
export default {
    data(){
        return{
        gridTemplateColumns:"1fr 1fr 1fr",
        columnGap:"0",
        rowGap:"0",
        justifyItems:"center",
        alignItems:"center",
    
        }
    },
    components:{
        "grid": ()=>import("./Grid.vue")
    }
}
</script>
