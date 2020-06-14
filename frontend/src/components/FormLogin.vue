<template>
  <q-dialog
    ref="dialog"
    @hide="$emit('hide')"
  >
    <q-card
      class="q-dialog-plugin"
      style="width: 600px; max-width: 80vw;"
    >
      <q-card-section>
        <div>
          Login
        </div>
      </q-card-section>

      <q-card-section>
        <q-input
          v-model="Form.username"
          class="q-pb-md"
          label="Username"
          outlined
          :error="$v.Form.username.$error"
          dense
        />

        <q-input
          v-model="Form.password"
          class="q-pb-md"
          label="Password"
          outlined
          :error="$v.Form.password.$error"
          dense
        />
      </q-card-section>

      <q-card-actions align="between">
        <q-btn
          ref="cancelar"
          label="Cancelar"
          color="primary"
          flat
          @click="hide"
        />

        <q-btn
          label="Login"
          color="primary"
          flat
          @click="login"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { required } from 'vuelidate/lib/validators'
export default {
  name: 'FormLogin',
  props: {
    Form: {
      type: Object
    }
  },
  data () {
    return {
    }
  },
  validations: {
    Form: {
      username: {
        required
      },
      password: {
        required
      }
    }
  },
  methods: {
    // following method is REQUIRED
    // (don't change its name --> "show")
    show () {
      this.$refs.dialog.show()
    },

    // following method is REQUIRED
    // (don't change its name --> "hide")
    hide () {
      this.$refs.dialog.hide()
    },

    onDialogHide () {
      // required to be emitted
      // when QDialog emits "hide" event
      this.$emit('hide')
    },
    async login () {
      this.$v.Form.username.$touch()
      this.$v.Form.password.$touch()
      const axiosConfig = {
        method: 'post',
        url: '/token/',
        data: JSON.parse(JSON.stringify(this.Form))
      }
      const Response = await this.$axios(axiosConfig).then(R => R.data).catch(console.error())

      localStorage.setItem('ACCESS_TOKEN', Response.access)

      this.asyncReload()
      this.$emit('ok')
      this.hide()
    },

    onCancelClick () {
      // we just need to hide dialog
      this.hide()
    }
  }
}
</script>
