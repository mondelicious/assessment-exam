<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'home' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Cars</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-12">
              <div class="input-group mb-12">
                <div class="input-group-prepend">
                  <label class="input-group-text" for="inputGroupSelect01">Options</label>
                </div>
                <select class="custom-select" id="inputGroupSelect01" v-model="newCar.color">
                  <option v-for="color in colors" :key="color.id">{{ color.name }}</option>
                </select>
              </div>
            </div>
            <div class="form-group col-md-12">
              <label for="inputEmail4">Name</label>
              <input type="text" class="form-control" v-model="newCar.name" />
            </div>
          </div>
          <button type="submit" class="btn btn-success">Add</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "CarsAdd",

  data() {
    return {
      saving: false,
      success: false,
      colors: {},
      currentItem: {},
      newCar: {
        name: null,
        color: null
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/cars/";
      let method = "POST";
      apiService(endpoint, method, this.newCar)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "car.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    },
    getListColors() {
      this.loading = true;
      let endpoint = `/api/v1/colors/`;
      apiService(endpoint)
        .then(data => {
          this.colors = data;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  created() {
    this.getListColors();
  }
};
</script>