import Vue from 'vue';
import App from './App.vue';

Vue.config.productionTip = false;
Vue.filter('value', (input: number) => {
  if (Number.isNaN(input)) {
    return '-';
  }
  return `R$ ${input.toFixed(2)}`;
});

Vue.filter('cpf', (value: string) => {
  return value.replace(/^(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
});

Vue.filter('to_date', (dateOtr: string) => {
  if (!dateOtr) {
    return '';
  }

  const locale = 'en-us';
  const dateObj = new Date(Date.parse(dateOtr));
  const monthName = dateObj.toLocaleString(locale, { month: 'short' });
  return `${dateObj.getDate()} ${monthName} ${dateObj.getFullYear()}`;
});

new Vue({
  render: (h) => h(App),
}).$mount('#app');
