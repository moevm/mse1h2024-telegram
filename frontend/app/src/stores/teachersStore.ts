import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from '@/config/defaultAxios'
import type TeacherItem from '@/entities/TeacherEntity'
import TeacherCreator from '@/models/TeacherModel'

export const useTeachersStore = defineStore('teachers', () => {
  const teachers = ref(new TeacherCreator())

  const getTeachers = async () => {
    axios.get('/teachers').then((response) => {
      response.data.forEach((teacher: TeacherItem) => {
        teachers.value.addTeacher(teacher)
      })
    })
  }

  const putTeacher = async (teacher: TeacherItem) => {
    axios.post('/teachers', teacher).then((response) => {
      teacher._id = response.data._id
      teachers.value.addTeacher(teacher)
    })
  }

  return {
    teachers,
    getTeachers,
    putTeacher
  }
})
