<template>
  <div>
    <mymap style="height: 100vh" />
  </div>
</template>

<script>
import mymap from './components/map'

export default {
  name: 'Index',
  components: {
    mymap
  },
  data() {
    return {
    }
  },

  methods: {

  }
}
</script>
<style scoped lang="scss">
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.chart-wrapper {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
</style>
