import { createRouter, createWebHistory } from 'vue-router'
import RouteForm from '../views/RouteForm.vue'
import dashboard from '../views/dashboard.vue'
import aboutus from '../views/aboutus.vue'
import Route from '../views/routes.vue'
import NearbyBuses from '../views/NearbyBuses.vue'

const router = createRouter({
    history:createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path:'/',
            name:RouteForm,
            component:RouteForm
        },
        {
            path:'/routes',
            name:Route,
            component:Route
        },
        {
            path:'/dashboard',
            name:'dashboard',
            component:dashboard,
          },
          {
            path:'/aboutus',
            name:'aboutus',
            component:aboutus,
          },
          {
            path:"/near",
            name:NearbyBuses,
            component:NearbyBuses
          }
    ]
})

export default router