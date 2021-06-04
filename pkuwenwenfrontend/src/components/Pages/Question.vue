<template>
<div>
  <div id = 'logoimg'>
  <img alt="Vue logo" src="./logo.png" height="106" width="256">
  </div>
   <!--
    <div class="common-layout">
      <el-container class="Question">
        <el-aside class="aside" width="200px">  提问者 </el-aside>
        <el-container>
          <el-header class="header">{{ curQuestion.title }}</el-header>
          <el-main class="main">{{ curQuestion.content }}</el-main>

        </el-container>
      </el-container>
    </div>
    -->

    <div class="common-layout">
        <div class = 'title'>
            <h4>{{curQuestion.title}}</h4>
        </div>
        <div class = 'content'>
            <p>{{curQuestion.content}}</p>
        </div>
    </div>

    <el-table
    :data="AnswerList"
    style="width: 100%"
    >
    <el-table-column
      fixed
      prop="content"
      label="回复内容"
      width="1000"
      >
      <template #default="scope">
      <div class="talk-box">
        <p>
          <span class="reply">{{ scope.row.content }}</span>
        </p>
      </div>
      <!-- 暂时disable了赞踩的功能，因为现在的实现会导致一个人可以点很多次赞……修改起来比较麻烦
      <div id = 'footer'>
          <el-button type="primary" plain @click="likeThisAnswer(scope.row.id)"><i class="el-icon-circle-check el-icon--left"></i>{{scope.row.proNum}}赞</el-button>
          <el-button type="danger" plain @click="dislikeThisAnswer((scope.row.id))"><i class="el-icon-circle-close el-icon--left"></i>{{scope.row.conNum}}踩</el-button>
      </div>
      -->
      </template>
    </el-table-column>
    </el-table>


    <el-container class="lower-part">
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">

        <el-form-item label="添加回复">
          <el-input type="textarea" :rows="10" 
            placeholder="输入回复"
            v-model="replyContent"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="addReply">回复</el-button>
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
      // 显示当前问题
      curQuestion: {
          title:'',
          content:'',
      },
      // 加载当前问题下的回复列表
      AnswerList: Array(), 
      // 添加回复
      replyContent: '',
    }
  },
  mounted(){
    var post_request = new FormData()
    post_request.append('question_id', this.$route.params.id)
    this.$http
    .request({
      url: this.$url + '/getAnswerList',
      method: 'post',
      data: post_request,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    .then((response) =>{
      //console.log('get return data')
      console.log(response)    
      this.AnswerList = response.data.answerlist
      this.curQuestion.title = response.data.question.title
      this.curQuestion.content = response.data.question.content
    })
  },

  methods: {
    addReply(){
        var post_request = new FormData()
        post_request.append('reply_content', this.replyContent)
        post_request.append('replyer', localStorage.getItem('ms_username'))
        post_request.append('qid', this.$route.params.id)
        this.$http
          .request({
            url: this.$url + '/addReply',
            method: 'post',
            data: post_request,
            headers: {'Content-Type': 'multipart/form-data'},
          })
          .then((response) => {
            console.log(response)
            if(response.data.retCode === 0){
              alert('回复成功！')
              location.reload() // 刷新页面
            }else{
              alert('error!回复失败！')
            }
          })
          .catch((response) => {
              console.log(response)
          })
    }
    /*
    暂时不启用赞踩功能
    因为如果想限制一个用户对一个问题只能点赞一次需要对点赞记录uid（我目前的想法）但是这就比较麻烦
    还有赞踩互斥关系感觉也挺麻烦的
    函数留在这里，如果什么时候有空我再来完善功能（by Tortoise）
    
    likeThisAnswer(aid){
        var post_request = new FormData()
        post_request.append('answer_id',aid)
        this.$http
        .request({
        url: this.$url + '/likeAnswer',
        method: 'post',
        data: post_request,
        headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) =>{
        //console.log('get return data')
        console.log(response)  
        })
    },
    dislikeThisAnswer(aid){
        var post_request = new FormData()
        post_request.append('answer_id',aid)
        this.$http
        .request({
        url: this.$url + '/likeAnswer',
        method: 'post',
        data: post_request,
        headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) =>{
        //console.log('get return data')
        console.log(response)  
        })
    },
    */
   
  },
}

</script>

<style>
.header{
  background-color: #f6f7f8;
  color: rgb(202, 187, 187);
  text-align: left;
  line-height: 60px;
}

.aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.main {
  background-color: #E9EEF3;
  color: #333;
  text-align: left;
  line-height: 160px;
}

.Question {
  margin-bottom: 40px;
}

.Answer {
  margin-top: auto;
}
.lower-part{
  margin-top: 30px;
}
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

.form-box{
  width: 700px;
}

.title{
    text-align: left;
}
</style>

