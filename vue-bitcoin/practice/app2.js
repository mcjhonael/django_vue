Vue.component("heade", {
  template: `
   <header>
    <nav>
      <ul>
        <li><a href="">Home</a></li>
        <li><a href="">About</a></li>
        <li><a href="">Contact</a></li>
      </ul>
    </nav>
   </header>
  `,
});

Vue.component("seccion1", {
  template: `
    <section>
      <h2>Mi primera section de noticias</h2>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad nemo sit repellendus nobis beatae corporis dolorum perspiciatis nihil id tempora minima vero non, libero, quidem odio ipsa officia, et necessitatibus.</p>
      <a href="" type="button"> Ver mas ....</a>
    </section>
    `,
});

Vue.component('seccion2', {
  template:`
    <section>
      <h2>Mi segunda secion de noticias</h2>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur temporibus reiciendis laboriosam quaerat earum tenetur reprehenderit aperiam? Sequi commodi unde, natus amet, eos suscipit totam ad repellendus harum architecto perspiciatis.</p>
      <a href="" type="button">Ver mas ...</a>
    </section>
  `
})

Vue.component("foote", {
  template: `
  <footer>
    <p>Todos los derechos reservador por jhonael</p>
  </footer>
  `
})



const app = new Vue({
  el: "#app",
  data() {
    return {
      saludo: "Bienvenido",
      nombre: "jhonatan",
    };
  },
});
