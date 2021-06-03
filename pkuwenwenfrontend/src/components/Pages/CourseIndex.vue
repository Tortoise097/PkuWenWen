<template>
  <h1>This is the CourseIndex view</h1>
  <div class="">
    <div class="container">
      <el-tabs v-model="message">
        <el-tab-pane :label="`全部课程(${unread.length})`" name="first">
          <el-table :data="unread" :show-header="false" style="width: 100%">
            <el-table-column>
              <template #default="scope">
                <span class="message-title" @click="openCourse(scope.row.title)">{{scope.row.title}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="date" width="180"></el-table-column>
            <el-table-column width="120">
              <template #default="scope">
                <el-button size="small" @click="handleRead(scope.$index)">关注</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="handle-row">
            <el-button type="primary">全部关注</el-button>
          </div>
        </el-tab-pane>
        <el-tab-pane :label="`我关注的课程(${read.length})`" name="second">
          <template v-if="message === 'second'">
            <el-table :data="read" :show-header="false" style="width: 100%">
              <el-table-column>
                <template #default="scope">
                  <span class="message-title" @click="openCourse(scope.row.title)">{{scope.row.title}}</span>
                </template>
              </el-table-column>
              <el-table-column prop="date" width="150"></el-table-column>
              <el-table-column width="120">
                <template #default="scope">
                  <el-button type="danger" @click="handleDel(scope.$index)">不再关注</el-button>
                </template>
              </el-table-column>
            </el-table>
            <div class="handle-row">
              <el-button type="danger">删除全部</el-button>
            </div>
          </template>
        </el-tab-pane>
      </el-tabs>
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
      unread: [{
        date: '更新于 2021-04-19 20:00:00',
        title: '软件工程',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: '编译原理',
      }, {
        date: '更新于 2021-04-19 20:00:00',
        title: '计算机系统导论',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: '数学分析III',
      }],
      read: JSON.parse(this.$route.params.courses.toString()),
    }
  },
  methods: {
    handleRead(index) {
      const item = this.unread.splice(index, 1);
      console.log(item);
      this.read = item.concat(this.read);
    },
    handleDel(index) {
      const item = this.read.splice(index, 1);
      this.unread = item.concat(this.unread);
    },
    openCourse(course) {
      // console.log(`dash: ${Course.id}`);
      // this.$router.push({
      //   name: 'Questions',
      //   params: {url:Course.link,id:Course.id}
      // })
      var post_request = new FormData()
      post_request.append('course', course)
      let _this = this
      this.$http
          .request({
            url: this.$url + '/openCourse',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 1){
              alert('get questions success')
              const questions = response.data.questions
              this.$router.push({name: 'Questions', params: {questions}})
            }else{
              _this.$message({
                message: "openCourse() failed",
                type: 'warning',
              })
              return false
            }
          })
          .catch((response) => {
            console.log(response)
          })
    }//openCourse() end
  },
  computed: {
    unreadNum(){
      return this.unread.length;
    },
  }
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

