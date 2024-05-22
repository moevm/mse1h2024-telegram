<script setup lang="ts">
import { ref, type Ref } from 'vue'
import axios from '@/config/defaultAxios'
import { useRouter, type Router } from 'vue-router'
import useVuelidate, { type Validation } from '@vuelidate/core'
import { helpers, required } from '@vuelidate/validators'
import type { Rules } from '@/interfaces/ValidationRulesType'

type AuthResponse = {
  data: {
    access_token: string
    token_type: string
  }
}

type AuthRequest = {
  username: string
  password: string
}

const emit = defineEmits<{
  (event: 'close-dialog'): void
}>()

const router: Router = useRouter()
const password: Ref<string> = ref('')
const errorMessage: Ref<string> = ref('')

const setUpToken = (token: string, tokenType: string): void => {
  localStorage.setItem('token', token)
  localStorage.setItem('type', tokenType)
}

const rules: Rules = {
  password: {
    required: helpers.withMessage('Пароль не может быть пустым', required)
  }
}
const state: any = { password }

const v$: Ref<Validation<Rules, any>> = useVuelidate(rules, state)

const confirm = async (): Promise<void> => {
  const resultValidation: boolean = await v$.value.$validate()
  if (!resultValidation) {
    errorMessage.value = v$.value.password.$errors[0].$message
    return
  }
  const body: AuthRequest = {
    username: 'admin',
    password: password.value
  }
  axios
    .post('/auth/login', body, {
      headers: { 'content-type': 'application/x-www-form-urlencoded' }
    })
    .then((response: AuthResponse) => {
      setUpToken(response.data.access_token, response.data.token_type)
      emit('close-dialog')
      router.push('/admin')
    })
    .catch((error) => {
      switch (error.response.status) {
        case 400:
          errorMessage.value = 'Неверный пароль'
          break
        case 422:
          errorMessage.value = 'Ошибка валидации данных'
          break
        default:
          errorMessage.value = 'Ошибка сервера'
      }
    })
}
</script>

<template>
  <v-card height="auto">
    <v-card-title class="card-title">
      <div data-testid="modal-title">Вход в систему</div>
      <v-btn
        class="card-title-close-btn"
        icon="$close"
        variant="text"
        @click="emit('close-dialog')"
      ></v-btn>
    </v-card-title>
    <v-card-text>
      <v-text-field
        data-testid="password-field"
        id="password-field"
        v-model="password"
        :clearable="true"
        label="Пароль"
        :error-messages="errorMessage"
        :required="true"
        @input="errorMessage = ''"
      ></v-text-field>
    </v-card-text>
    <v-card-actions class="card-actions">
      <v-btn
        class="outlined-button"
        id="confirm-button"
        data-testid="confirm-button"
        size="auto"
        variant="outlined"
        @click="confirm"
      >
        Подтвердить
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
.card-actions {
  justify-content: center;
}
#confirm-button {
  color: limegreen;
  padding: 5px 20px;
}
</style>
