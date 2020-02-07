import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CarEditor from "../components/Cars/CarEditor.vue";
import CarAdd from "../components/Cars/CarAdd.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/cars/:id",
    name: "car.edit",
    component: CarEditor,
    props: true
  },
  {
    path: "/car/add/",
    name: "car.add",
    component: CarAdd
  },
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL, - commented out for proper url
  routes
});

export default router;
