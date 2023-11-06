Vue.component("CoinDetail", {
  // props: ["changePercent", "img", "name","symbol", "ancho","price","pricesWithDays"],
  props: ['coin'],
  data() {
    return {
      showPrices: false,
      value:0,
    };
  },
  methods: {
    toggleShowPrices() {
      this.showPrices = !this.showPrices;
      // que debe emitir un evento con este $emit le decimos que debe emitir un evento change-color cada vez que se ejecute un metodo como segundo parametro podemos mandar un valor por defecto 
      this.$emit('change-color',this.showPrices ? 'ff99c8':'3d3d3d');
    }
  },
  computed: {
      title() {
      return `${this.coin.name} -  ${this.coin.symbol}`;
    },
    convertedValue() {
      if (!this.value) {
        return 0;
      }
      return this.value / this.coin.price;
    },
  },
  created() { console.log("create hijo")},
  mounted() { console.log("mounted hijo")},

  template: `
  <div>

    <img
      @mouseover="toggleShowPrices"
      @mouseout="toggleShowPrices"
      :src="coin.img"
      :alt="coin.name"
      :width="coin.ancho"
    />
    <h1 :class="coin.changePercent > 0 ? 'green' : 'red' ">
      {{title}}
      <span v-if="coin.changePercent > 0">✌</span>
      <span v-else-if="coin.changePercent < 0">zerou</span>
      <span v-else>😢</span>

      <span v-show="coin.changePercent>0">✌</span>
      <span v-show="coin.changePercent<0">zerou</span>
      <span v-show="coin.changePercent===0">😢</span>
      <span @click="toggleShowPrices"> ver precios {{coin.showPrices ? '🙈' : '🐵' }} </span> 
    </h1>

    <input type="number" v-model="value" />
      <span>{{convertedValue}}</span>

    <slot name="text"></slot>
    <slot name="link"></slot>

      <ul v-show="showPrices">
        <li
          v-for="(dia,i) in coin.pricesWithDays"
          :key="dia.value"
          :class="{orange:dia.value === coin.price , red:dia.value<coin.price , green:dia.value>coin.price}"
          class="upperCase"
        >
          {{i}} {{dia.day}} - {{dia.value}}
        </li>
      </ul>
  </div>
      `,
});
Vue.component("prueba", {
  created() {console.log("create prueba") },
  mounted() {console.log("mounte prueba") },
  template: `
  <div>
  <p>elemnto pruebita nomas</p></div>
  `
})
const app = new Vue({
  el: "#app",
  data() {
    return {
      btc: {
        name: "Bitcoin",
        nombre: "jhonatan maquera",
        symbol: "BTC",
        img: "https://cryptologos.cc/logos/bitcoin-btc-logo.png",
        changePercent: 10,
        ancho: "100px",
        claro: "white",
        price: 8400,
        pricesWithDays: [
          { day: "lunes", value: 8400 },
          { day: "martes", value: 7900 },
          { day: "miercoles", value: 8200 },
          { day: "jueves", value: 9000 },
          { day: "viernes", value: 9400 },
          { day: "sabado", value: 10000 },
          { day: "domingo", value: 10200 },
          
        ],
      },
      color:"f4f4f4",
    };
  },
  created() {
    console.log("created");
  },
  mounted() {
    console.log("mounted");
   },
  methods: {
    updateColor(color) {
      this.color = color || this.color.split("").reverse().join("");
    },
  },
});
