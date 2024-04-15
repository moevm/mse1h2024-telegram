import "@/assets/main.css"

import { createApp } from "vue"
import { createPinia } from "pinia"

import App from "./App.vue"
import router from "./router"

import "vuetify/styles"
import "material-design-icons-iconfont/dist/material-design-icons.css"
import { createVuetify } from "vuetify"
import { aliases, mdi } from "vuetify/iconsets/mdi-svg"
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

const vuetify = createVuetify({
  components,
  directives,
  icons: {
<<<<<<< HEAD
    defaultSet: "mdi",
=======
    defaultSet: 'mdi',
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a
    aliases,
    sets: {
      mdi,
    },
  },
})

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.use(createPinia())

app.mount("#app")