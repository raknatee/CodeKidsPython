<template lang="">
    <div class="layout" :style="addStyle" >
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
    </div>
</template>
<script>
export default {
    props:['flexDirection','gap','justifyContent','alignItems'],
    computed:{
        addStyle(){
            return {"--flex-direction":this.flexDirection,
                    "--gap":this.gap,
                    "--just-con":this.justifyContent,
                    "--align-items":this.alignItems
            }
        }
    }
}
</script>
<style scoped>
.layout{
    display: flex;
    flex-direction: var(--flex-direction);
    
    background-color: gray;
    height: 50vh;
    gap: var(--gap);
    justify-content: var(--just-con);
    align-items:var(--align-items);
  
}
.box{
   
    width: 100px;
    height: 100px;
    background-color: yellow;
}
</style>