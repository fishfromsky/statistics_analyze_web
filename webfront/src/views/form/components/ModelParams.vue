<template>
    <div class="adjust-container">
      <div v-if="ModelIndex==='1'">
        <params1 @event1="handleChange($event)"></params1>
      </div>
    </div>
</template>

<script>
    import Params1 from './paramsdetail/Params1'
    export default {
        name: "ModelParams",
        data(){
          return{
            val:''
          }
        },
        components:{
          Params1
        },
        props:{
          ModelIndex:{
            type: String,
            required: true
          }
        },
        watch:{
          val:{
            handler(val){
              this.$emit('event1', val)
            }
          }
        },
        mounted() {

        },
        methods:{
          handleChange(val){
            this.val = val;
          }
        }
    }
</script>

<style scoped>

</style>
