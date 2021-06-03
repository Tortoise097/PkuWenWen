<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="./logo.png" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> {{SchoolName}} </p>
  </div>
  <div class="">
    <el-table
    :data="CourseList"
    style="width: 50%"
    >
    <el-table-column
      fixed
      prop="course_id"
      label="课程号"
      width="250">
    </el-table-column>

    <el-table-column
      fixed
      prop="course_name"
      label="课程名"
      width="250">
      <template #default="scope">
        <span class="message-title" @click="openCourse(scope.row.course_name)">{{scope.row.course_name}}</span>
      </template>
    </el-table-column>
    
    </el-table>
  </div>
</div>
</template>

<script>
export default {
  name: 'tabs',
  data() {
    return {
      SchoolName: this.$route.params.school,
      message: 'first',
      showHeader: false,
      CourseList: Array(),
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('schoolname', this.$route.params.school)
    this.$http
    .request({
      url: this.$url + '/getCourseIndex',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)    
      this.CourseList = response.data.courselist
    })
  },

  methods: {
    openCourse (coursename) {
       console.log(`dash: ${coursename}`);
       this.$router.push({
         path: '/' + this.$route.params.school + '/' + coursename + '/CourseIndex',
       })
    }
  },
}

</script>

<style>
.message-title{
  cursor: pointer;
}
.handle-row{
  margin-top: 30px;
}
</style>

