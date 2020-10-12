<template>
    <div>
        <div class="main-box">
            <div class="header">
                <div class="header-text">上海市固废垃圾成分</div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index"
    }
</script>

<style scoped>
    .main-box{
        width: 100%;
        min-height: calc(100vh - 50px);
        background-color: rgb(8, 15, 62);
    }
    .header{
        width: 100%;
        height: 45px;
        padding-top: 10px;
    }
    .header-text{
        color: #fff;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
    }
</style>
