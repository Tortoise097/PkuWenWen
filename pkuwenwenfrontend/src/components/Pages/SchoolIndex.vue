<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="./logo.png" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> School Index </p>
  </div>
  <div class="">
    <el-table
    :data="SchoolList"
    style="width: 30%"
    >
    <el-table-column
      fixed
      prop="school_name"
      label="全部院系"
      width="250">
      <template #default="scope">
        <span class="message-title" @click="openSchool(scope.row.school_name)">{{scope.row.school_name}}</span>
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
      message: 'first',
      showHeader: false,
      SchoolList: Array()
    }
  },
  mounted(){
    this.$http
    .request({
      url: this.$url + '/getSchoolIndex',
      method: 'get',
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)    
      this.SchoolList = response.data.schoollist
    })
  },
  methods: {
    openSchool (schoolname) {
       console.log(`dash: ${schoolname}`);
       this.$router.push({
         path: '/'+ schoolname + '/CourseIndex',
       })
    },
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
/*
#logoimg {
  text-align: left;
}
#text {
  text-align: right;
}
*/
</style>

