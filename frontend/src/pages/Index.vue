<template>
  <q-page-container padding>
    <q-card>
      <q-table
        title="Contatos"
        dense
        :columns="columns"
        :data="tableData"
        row-key="id"
      >
        <q-td
          slot="body-cell-id"
          slot-scope="props"
          :props="props"
        >
          <q-btn
            color="info"
            icon="edit"
            dense
            round
            flat
            @click="edit(props.value)"
          >
            <q-tooltip>
              Editar contato
            </q-tooltip>
          </q-btn>

          <q-btn
            color="negative"
            icon="delete"
            dense
            round
            flat
            @click="alert(props.value)"
          >
            <q-tooltip>
              Excluir contato
            </q-tooltip>
          </q-btn>
        </q-td>
      </q-table>

    </q-card>
    <q-page-sticky
      position="bottom-right"
      :offset="[18, 18]"
    >
      <q-btn
        fab
        icon="add"
        @click="edit(0)"
        color="primary"
      />
    </q-page-sticky>
  </q-page-container>
</template>

<script>
import ComponentContato from '../components/ComponentContato'
export default {
  name: 'PageIndex',
  data () {
    return {
      columns: [
        { name: 'nome', align: 'center', label: 'Nome', field: 'nome' },
        { name: 'idade', label: 'Idade', field: 'idade' },
        { name: 'telefone', label: 'Telefone', field: 'telefone' },
        { name: 'endereco', label: 'Endereço', field: 'endereco' },
        { name: 'id', align: 'right', label: 'Ações', field: 'id' }
      ]
    }
  },
  asyncData: {
    async tableData () {
      const axiosConfig = {
        method: 'get',
        url: '/contatos/',
        headers: {
          Authorization: 'Bearer ' + localStorage.getItem('ACCESS_TOKEN'),
          'Content-Type': 'application/json'
        },
        params: {
          filter: {
            fields: ['id', 'nome', 'idade', 'telefone', 'endereco'],
            order: 'nome'
          }
        }
      }
      const Response = await this.$axios(axiosConfig).then(R => R.data).catch(console.error())
      return Response
    }
  },
  methods: {
    alert (id) {
      this.$q.dialog({
        title: 'Excluir',
        message: 'Tem certeza que quer exclui?',
        ok: 'Confirmar',
        cancel: 'Cancelar'
      }).onOk(() => {
        const axiosConfig = {
          method: 'delete',
          url: `/contatos/${id}`
        }
        this.$axios(axiosConfig).then(() => this.asyncReload('tableData')).catch(console.error())
      })
    },
    edit (id) {
      this.$q.dialog({
        component: ComponentContato,
        parent: this,
        id
      })
        .onOk(() => this.asyncReload('tableData'))
    }
  }
}
</script>
