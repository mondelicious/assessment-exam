<template>
  <div class="container">
    <div class="mt-5" v-if="loading">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-else>
      <div class="row">
        <button type="button" class="btn btn-link mt-5 pull-left">
          <router-link :to="{ name: 'home' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ item.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-6">
                <label for="inputEmail4">Name</label>
                <input type="text" class="form-control" disabled v-model="item.name" />
              </div>
              <div class="form-group col-md-6">
                <label for="inputEmail4">Color</label>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <label class="input-group-text" for="inputGroupSelect01">Options</label>
                  </div>
                  <select class="custom-select" id="inputGroupSelect01" v-model="item.color">
                    <option v-for="color in colors" :key="color.id">{{ color.name }}</option>
                  </select>
                </div>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button type="submit" class="btn btn-danger ml-2" @click="deleteExpense">Delete</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "CarEditor",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      item: {},
      colors: {},
      loading: false
    };
  },
  methods: {
    viewCars() {
      this.loading = true;
      let endpoint = `/api/v1/cars/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          this.item = data;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    onSubmit() {
      this.loading = true;
      let endpoint = `/api/v1/cars/${this.id}/`;
      let method = "PUT";
      apiService(endpoint, method, this.item)
        .then(item => {
          this.loading = false;
          this.$router.push({
            name: "car.edit",
            params: { id: item.id }
          });
          this.viewCars();
        })
        .catch(err => {
          console.log(err);
        });
    },
    deleteExpense() {
      let endpoint = `/api/v1/cars/${this.id}/`;
      let method = "DELETE";
      apiService(endpoint, method).then(() => {
        this.$router
          .push({
            name: "home"
          })
          .catch(err => {
            console.log(err);
          });
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
    this.viewCars();
    this.getListColors();
  }
};
</script>