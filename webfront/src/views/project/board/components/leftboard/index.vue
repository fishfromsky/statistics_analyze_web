<template>
    <div>
        <column @reload-table="handleReload"></column>
        <datatable :parentmsg="add_id"></datatable>
    </div>
</template>

<script>
import column from './components/column'
import datatable from './components/table'
export default {
    components:{
        column,
        datatable
    },
    data(){
        return{
            add_id: ''
        }
    },
    methods:{
        handleReload:function(val){
            this.add_id = val
        }
    }
}
</script>

<style scoped>

</style>