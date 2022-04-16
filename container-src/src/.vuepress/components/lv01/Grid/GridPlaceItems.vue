<template lang="">
    <div class="layout" :style="addStyle">
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>

        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>

        <div class="box"></div>
    </div>
</template>
<script>
export default {
    props:[
        'gridTemplateColumns',
        'columnGap',
        'rowGap',
        'placeItems',
      
    ],
    computed:{
        addStyle(){
            return{
                '--grid-template-columns':this.gridTemplateColumns,
                '--column-gap':this.columnGap,
                '--row-gap':this.rowGap,
                '--place-items':this.placeItems,
            
            }
        }
    }
    
}
</script>
<style scoped>
.layout{
    height: 50vh;
    background-color: gray;
    display: grid;

    grid-template-columns: var(--grid-template-columns);

    column-gap:var(--column-gap) ; 
    row-gap: var(--row-gap);

   
    place-items: var(--place-items);
}
.box{
   
    width: 100px;
    height: 100px;
    background-color: yellow;
}
</style>

