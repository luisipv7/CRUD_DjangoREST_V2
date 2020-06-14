<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        /> -->

        <q-toolbar-title>
          Agenda QuasarDjango
        </q-toolbar-title>

        <div>
          <q-btn
            v-if="this.$acl.check('isAuthenticated')"
            label="LogOut"
            dense
            flat
            @click="logout"
          />
        </div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import FormLogin from '../components/FormLogin'
export default {
  name: 'MainLayout',
  data () {
    return {
      Form: {
        username: '',
        password: ''
      },
      btnChange: 1
    }
  },
  methods: {
    login (Form) {
      this.$q.dialog({
        component: FormLogin,
        parent: this,
        Form
      }).onOk(() => this.change(0))
    },
    change (val) {
      this.btnChange = val
      this.asyncReload()
    },
    logout () {
      localStorage.removeItem('ACCESS_TOKEN')
      this.$acl.change('unauthenticated')
      this.$router.push('/')
    }
  }
}
</script>
