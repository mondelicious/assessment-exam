<template>
  <div class="home">
    <car-table />
  </div>
</template>

<script>
// @ is an alias to /src
import CarTable from "@/components/Cars/CarTable.vue";

export default {
  name: "home",
  components: {
    CarTable
  }
};
</script>
