<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="./logo.png" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> CourseName </p>
  </div>
  <el-container class="higher-part">
    <div class="container">
      <el-tabs v-model="message">
        <el-tab-pane :label="`全部问题(${unread.length})`" name="first">
          <el-table :data="unread" :show-header="false" style="width: 100%">
            <el-table-column>
              <template #default="scope">
                <span class="message-title" @click="openQuestion(scope.row.title)">{{scope.row.title}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="content" width="180"></el-table-column>
            <el-table-column width="540">
              <el-form>
                <el-form-item label="文本框">
                  <el-input title="高赞回复" type="textarea" autosize rows="5" v-model="form.desc"></el-input>
                </el-form-item>
              </el-form>
            </el-table-column>
            <el-table-column prop="stars" width="180"></el-table-column>
            <el-table-column prop="date" width="180"></el-table-column>
            <el-table-column width="120">
              <template #default="scope">
                <el-button size="small" @click="handleRead(scope.$index)">关注</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>

      </el-tabs>
    </div>
  </el-container>

  <el-container class="lower-part">
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="问题标题">
          <el-input v-model="form.title"></el-input>
        </el-form-item>

        <el-form-item label="问题描述">
          <el-input type="textarea" :rows="10" v-model="form.desc"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitQuestion">提问</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-container>
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
        title: 'Question1',
        content: "描述1",
        stars: 233,
        link: 'q1',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: 'Question2',
        content: "描述2",
        stars: 61,
        link: 'q2',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: 'Question3',
        content: "描述3",
        stars: 618,
        link: 'q3',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: 'Question4',
        content: "描述4",
        stars: 604,
        link: 'q4',
      }],
      read: [],
      //read: JSON.parse(this.$route.params.questions.toString()),
      form: {
        title: '默认标题',
        date1: '',
        date2: '',
        desc: '这里应该有高赞回复的内容\n而且这个输入框是可以随着内容数量的变化改变大小的\n这个部分应该从属于每一个Question各自的字段' +
            '，但是我只是搞了排版所以让他们在这里共享了\n实际上应该在上面的read和unread的每一项里面存相应的字段\n这个可以架子搭完再微调,' +
            '\n日后还可以上传图片，不过数据库那边不好办，一个比较简单的方法是在服务器上保存图片文件，然后把文件名存到数据库里，' +
            '每次查完数据库得到图片名，再用python文件操作打开文件，比较繁琐咱们先不做了吧',
      },
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
    submitQuestion(){
      var post_request = new FormData()
      post_request.append('title', this.form.title)
      post_request.append('date1', this.form.date1)
      post_request.append('date2', this.form.date2)
      post_request.append('detail', this.form.desc)
      let _this = this
      const tmpform = {
        date: '0000-00-00',
        title: '',
        content: "",
        stars: 0,
        link: 'lkabababa',
      }
      this.$http
          .request({
            url: this.$url + '/submitQuestion',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 1){
              alert('submit question success')
              tmpform.title = response.data.title
              tmpform.content = response.data.detail
              //把新问题挂到unread列表里
              _this.unread = _this.unread.concat(tmpform)
            }else{
              _this.$message({
                message: "submitQuestion() failed",
                type: 'warning',
              })
              return false
            }
          })
          .catch((response) => {
            console.log(response)
          })
    },
    openQuestion(question) {
      // console.log(`dash: ${Course.id}`);
      // this.$router.push({
      //   name: 'Questions',
      //   params: {url:Course.link,id:Course.id}
      // })
      var post_request = new FormData()
      post_request.append('question', question)
      let _this = this
      this.$http
          .request({
            url: this.$url + '/openQuestion',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 1){
              alert('get questions success')
              const curQuestion = response.data.curQuestion
              const curAnswer = response.data.curAnswer
              this.$router.push({name: 'ViewAnswer', params: {curQuestion: curQuestion, curAnswer: curAnswer}})
            }else{
              _this.$message({
                message: "openQuestion() failed",
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
    }
  }
}

</script>

<style>
.higher-part{
  margin-bottom: 30px;

}
.lower-part{
  margin-top: auto;
}
.message-title{
  cursor: pointer;
}
.handle-row{
  margin-top: 30px;
}

.form-box{
  width: 700px;
}

</style>

