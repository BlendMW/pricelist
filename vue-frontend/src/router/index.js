import Vue from 'vue';
import Router from 'vue-router';
import DestinationList from '../../../src/components/DestinationList.vue';
import PackageList from '../components/PackageList.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/destination',
      name: 'DestinationList',
      component: DestinationList
    },
    {
      path: '/package',
      name: 'PackageList',
      component: PackageList
    }
  ]
}); 