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
        <div
          v-if="id > 0"
          class="text-h6"
        >
          Editar Contato
        </div>
        <div
          v-else
          class="text-h6"
        >
          Novo Contato
        </div>
      </q-card-section>

      <q-card-section>
        <q-input
          v-model="Form.nome"
          class="q-pb-md"
          label="Nome completo"
          outlined
          :error="$v.Form.nome.$error"
          dense
        />

        <q-input
          v-model="Form.idade"
          class="q-pb-md"
          label="Idade"
          outlined
          dense
        />

        <q-input
          v-model="Form.telefone"
          class="q-pb-md"
          label="Telefone"
          autofocus
          outlined
          dense
          :error="$v.Form.telefone.$error"
        />

        <q-input
          v-model="Form.endereco"
          class="q-pb-md"
          label="Endereço"
          autofocus
          outlined
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
          ref="salvar"
          label="Salvar"
          color="primary"
          flat
          @click="save"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>

</template>

<script>
import { required } from 'vuelidate/lib/validators'
const factoryForm = JSON.stringify({
  nome: '',
  idade: '',
  telefone: '',
  endereco: '',
  id: null
})

export default {
  name: 'ComponentContato',
  props: {
    id: {
      type: Number,
      default: () => null
    }
  },
  data () {
    return {}
  },
  validations: {
    Form: {
      nome: {
        required
      },
      telefone: {
        required
      }
    }
  },
  asyncData: {
    FormDefault: JSON.parse(factoryForm),
    async Form () {
      if (!this.id) {
        return JSON.parse(factoryForm)
      }

      const axiosConfig = {
        method: 'get',
        url: `/contatos/${this.id}`
      }

      const Response = await this.$axios(axiosConfig)
        .then(R => R.data)
        .catch(this.AxiosCatch)
      return Response
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

    async save () {
      this.$v.Form.telefone.$touch()
      this.$v.Form.nome.$touch()
      if (this.id === 0) {
        const axiosConfig = {
          method: 'post',
          url: '/contatos/',
          data: JSON.parse(JSON.stringify(this.Form))
          // headers: { Authorization: 'Bearer ' + token }
        }
        await this.$axios(axiosConfig).catch(console.error())
      } else {
        const axiosConfig = {
          method: 'put',
          url: `/contatos/${this.id}/`,
          data: JSON.parse(JSON.stringify(this.Form))
        }
        await this.$axios(axiosConfig).catch(console.error())
      }
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
