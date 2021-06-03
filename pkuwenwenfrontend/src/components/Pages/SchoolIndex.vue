<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="./logo.png" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> School Index </p>
  </div>
  <div class="">
    <div class="container">
      <el-tabs v-model="message">
        <el-tab-pane :label="`全部院系(${unread.length})`" name="first">
          <el-table :data="unread" :show-header="false" style="width: 100%">
            <el-table-column>
              <template #default="scope">
                <span class="message-title" @click="openSchool(scope.row.title)">{{scope.row.title}}</span>
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
        <el-tab-pane :label="`我关注的院系(${read.length})`" name="second">
          <template v-if="message === 'second'">
            <el-table :data="read" :show-header="false" style="width: 100%">
              <el-table-column>
                <template #default="scope">
                  <span class="message-title" @click="openSchool(scope.row.title)">{{scope.row.title}}</span>
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
        title: '中文系',
        link: 'zhongwen',
        id: 1,
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: '数学科学学院',
        link: 'shuxue',
        id: 2,
      }],
      read: [{
        date: '更新于 2021-04-19 20:00:00',
        title: '信息科学技术学院',
        link: 'xinxi',
        id: 3,
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: '物理学院',
        link: 'wuli',
        id: 4,
      }],
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
    openSchool (school) {
       console.log(`dash: ${school.id}`);
       this.$router.push({
         name: 'CourseIndex',
         params: {url:school.link,id:school.id}
       })
      /*
      var post_request = new FormData()
      post_request.append('school', school)
      let _this = this;
      this.$http
          .request({
            url: this.$url + '/openSchool',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then((response) =>{
            console.log(response)
            // if(response.data.login.retCode == 1){  //这行在最后需要代替下面的 if true
            // eslint-disable-next-line no-constant-condition
            if(response.data.login.retCode == 1){
              alert('get courses success');
              this.$router.push({name: 'CourseIndex', params: {courses: response.data.courses}});
            }
            else {
              _this.$message({
                message: "openSchool()failed",
                type: 'warning',
              });
              return false
            }
          })
          .catch((response) => {
            console.log(response)
          });
      //openSchool end
      */
    },
  },
  computed: {
    unreadNum(){
      return this.unread.length;
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
/*
#logoimg {
  text-align: left;
}
#text {
  text-align: right;
}
*/
</style>

