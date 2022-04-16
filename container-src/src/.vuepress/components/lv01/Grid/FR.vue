<template lang="">
    <div class="layout" :style="addStyle">
        <div class="box box1">
            <p>{{textForBox[0]}}</p>
        </div>
        <div class="box box2">
            <p>{{textForBox[1]}}</p>
        </div>
        <div class="box box3">
            <p>{{textForBox[2]}}</p>
        </div>
    </div>
</template>
<script>
export default {
    props:['gridTemplateColumns','columnGap'],
    computed:{
        addStyle(){
            return {
                '--col':this.gridTemplateColumns,
                '--col-gap':this.columnGap
            }
        },
        textForBox(){
            return this.gridTemplateColumns.split(" ")
        }
    }
}
</script>
<style scoped>
.layout{
    display: grid;
    grid-template-columns: var(--col);
    height: 10vh;
    column-gap: var(--col-gap);
   
}
.box{
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
    font-size: 2rem;
}
.box1{
    background-color: rgb(255, 203, 60);
}
.box2{
    background-color: rgb(33, 153, 18);
}
.box3{
    background-color: rgb(224, 113, 22);
}
</style>