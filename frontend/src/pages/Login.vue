<template>
  <q-page class="flex flex-center">
    <q-card class="q-pa-lg">
      <q-form
        @submit="onSubmit"
        @reset="onReset"
        class="q-gutter-md"
      >
        <div class="flex flex-center">
          <q-icon
            name="contacts"
            class="text-primary"
            size="xl"
          />
        </div>
        <q-input
          outlined
          v-model="Form.username"
          label="username"
        />

        <q-input
          outlined
          v-model="Form.password"
          label="pass"
          type="password"
        />

        <q-card-actions align="between">
          <q-btn
            label="Reset"
            type="reset"
            color="primary"
            flat
            class="q-ml-sm"
          />
          <q-btn
            label="Login"
            type="submit"
            color="primary"
          />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-page>
</template>

<script>
import { required } from 'vuelidate/lib/validators'
export default {
  name: 'PageLogin',
  data () {
    return {
      Form: {
        username: '',
        password: null
      }
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
    async onSubmit () {
      this.$v.Form.username.$touch()
      this.$v.Form.password.$touch()
      const axiosConfig = {
        method: 'post',
        url: '/token/',
        data: JSON.parse(JSON.stringify(this.Form))
      }
      const Response = await this.$axios(axiosConfig).then(R => R.data).catch(R => undefined)

      if (Response === undefined) {
        return this.$q.notify({
          message: 'Algo certo está errado',
          color: 'negative'
        })
      }
      localStorage.setItem('ACCESS_TOKEN', Response.access)
      this.$acl.change('authenticated')
      this.$router.push('/index')
    },
    onReset () {
      this.Form.username = null
      this.Form.password = null
    }
  }
}
</script>
