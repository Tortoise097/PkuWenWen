<template>
  <h1>This is the CourseIndex view</h1>
  <h1>{{$route.params.courses}}第二</h1>
  <h1>{{$route.params}}第三</h1>
  <h2>{{tmpMessage}}第四</h2>
  <h2>{{paramsFromFormerPage}}第五</h2>
  <el-button @click="handleClick()">handleClick</el-button>
  <el-button @click="handleClick2()">handleClick2</el-button>
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
      paramsFromFormerPage: this.$route.params.courses,
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
      tmpMessage: this.$route.params,
      read: JSON.parse(this.$route.params.courses.toString()),
      //read: this.$route.params.courses,
      readparse: JSON.parse(this.$route.params.courses.toString()),
    }
  },
  methods: {
    handleClick(){
      console.log(this.read)
    },
    handleClick2(){
      console.log(this.readparse)
    },
    handleRead(index) {
      const item = this.unread.splice(index, 1);
      console.log(item);
      this.read = item.concat(this.read);
    },
    handleDel(index) {
      const item = this.read.splice(index, 1);
      this.unread = item.concat(this.unread);
    },
    openCourse(Course) {
      console.log(`dash: ${Course.id}`);
      this.$router.push({
        name: 'Questions',
        params: {url:Course.link,id:Course.id}
      })
    }
  },
  computed: {
    unreadNum(){
      return this.unread.length;
    },
    newCourses(){
      var nc = []
      const courses = this.$route.params['courses']
      alert(courses)
      nc.concat({date: courses['date'], title: courses['title']})
      return nc
    }
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

