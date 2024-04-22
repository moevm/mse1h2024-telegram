import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from '@/config/defaultAxios'
import type TeacherItem from '@/entities/TeacherEntity'
import TeacherCreator from '@/models/TeacherModel'

export const useTeachersStore = defineStore('teachers', () => {
  const teachers = ref(new TeacherCreator())

  const getTeachers = async () => {
    axios.get('/teachers').then((response) => {
      response.data.forEach((teacher: any) => {
        teachers.value.addTeacher(teacher)
      })
    })
  }

  const postTeacher = async (teacher: TeacherItem) => {
    axios.post('/teachers', teacher).then((response) => {
      teacher._id = response.data._id
      teachers.value.addTeacher(teacher)
    })
  }

  const putTeacher = async (teacher: TeacherItem) => {
    axios.put(`/teachers/${teacher._id}`, teacher).then((response) => {
      const changedTeacher: TeacherItem = {
        _id: response.data._id,
        names_list: response.data.names_list,
        telegram_login: response.data.telegram_login
      }
      teachers.value.changeTeacher(changedTeacher)
    })
  }

  const deleteTeacher = async (teacherId: string): Promise<void> => {
    axios.delete(`/teachers/${teacherId}`).then((response) => {
      console.log('deleted')
      const responseTeacherId: string = response.data._id
      teachers.value.removeTeacher(responseTeacherId)
    })
  }

  return {
    teachers,
    getTeachers,
    putTeacher,
    postTeacher,
    deleteTeacher
  }
})
