<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="./logo.png" height="106" width="256">
  </div>
  <div id = 'text'>
  <p> {{SchoolName}} </p>
  <p> {{CourseName}} </p>
  </div>
  <el-container class="higher-part">
    <el-table
    :data="QuestionList"
    style="width: 100%"
    >

    <el-table-column
      fixed
      prop="course_name"
      label="问题标题"
      width="800">
      <template #default="scope">
        <span class="message-title" @click="openQuestion(scope.row.id)">{{scope.row.title}}</span>
      </template>
    </el-table-column>
    
    </el-table>
  </el-container>

  <el-container class="lower-part">
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="问题标题">
          <el-input 
            placeholder="输入问题标题，限制40字以内"
            v-model="inputdata.title"></el-input>
        </el-form-item>

        <el-form-item label="问题描述">
          <el-input type="textarea" :rows="10" 
            placeholder="输入问题描述，限制1000字以内（语言尽量简洁即可）"
            v-model="inputdata.content"></el-input>
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
      CourseName: this.$route.params.course,
      SchoolName: this.$route.params.school,
      inputdata: {
        title: '',
        content:'',
      },
      QuestionList: Array(),
    /*
      form: {
        title: '默认标题',
        date1: '',
        date2: '',
        desc: '这里应该有高赞回复的内容\n而且这个输入框是可以随着内容数量的变化改变大小的\n这个部分应该从属于每一个Question各自的字段' +
            '，但是我只是搞了排版所以让他们在这里共享了\n实际上应该在上面的read和unread的每一项里面存相应的字段\n这个可以架子搭完再微调,' +
            '\n日后还可以上传图片，不过数据库那边不好办，一个比较简单的方法是在服务器上保存图片文件，然后把文件名存到数据库里，' +
            '每次查完数据库得到图片名，再用python文件操作打开文件，比较繁琐咱们先不做了吧',
      },
    */
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('coursename', this.$route.params.course)
    this.$http
    .request({
      url: this.$url + '/getQuestionIndex',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)    
      this.QuestionList = response.data.questionlist
    })
  },

  methods: {
    openQuestion (question_id) {
       console.log(`dash: ${question_id}`);
       this.$router.push({
         path: '/Question/' + question_id.toString(),
       })
    },

    submitQuestion(){
      var post_request = new FormData()
      post_request.append('coursename', this.$route.params.course)
      post_request.append('publisher', localStorage.getItem('ms_username'))
      post_request.append('title', this.inputdata.title)
      post_request.append('content', this.inputdata.content)
      this.$http
          .request({
            url: this.$url + '/addQuestion',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.addQuestion.retCode === 0){
              alert('提交问题成功！')
              location.reload() // 刷新页面
            }else{
              alert('error!提交问题失败！')
            }
          })
          .catch((response) => {
              console.log(response)
          })
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

