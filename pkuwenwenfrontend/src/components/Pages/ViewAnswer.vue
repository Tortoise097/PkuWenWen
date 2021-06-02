<template>
  <h1>This is the ViewAnswer view</h1>
    <div class="common-layout">

      <el-container class="Question">
        <el-aside class="aside" width="200px">提问者信息</el-aside>
        <el-container>
          <el-header class="header">题目</el-header>
          <el-main class="main">题干详细描述</el-main>
          <el-footer class="footer">点赞投币收藏区</el-footer>
        </el-container>
      </el-container>

      <el-container class="Answer">
        <el-aside class="aside" width="200px">回答者信息</el-aside>
        <el-container>
          <el-header class="header">回答标题</el-header>
          <el-main class="main">回答正文</el-main>
          <el-footer class="footer">点赞投币收藏区</el-footer>
        </el-container>
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
      curQuestion: {
        publisher: '',
        title: '',
        detail: '',
        proNum: 0,
        conNum: 0,
        subscribeNum: 0,
      },
      curAnswer: {
        publisher: '',
        title: '',
        detail: '',
        proNum: 0,
        conNum: 0,
        subscribeNum: 0,
      }
    }
  },
  methods: {
    handleQuestionPro() {
      this.curQuestion.proNum += 1;
      console.log(this.curQuestion.proNum);
    },
    handleQuestionCon() {
      this.curQuestion.conNum += 1;
      console.log(this.curQuestion.conNum);
    },
    handleQuestionSubscribe () {
      this.curQuestion.subscribeNum += 1;
      console.log(this.curQuestion.subscribeNum);
    },
    handleAnswerPro() {
      this.curAnswer.proNum += 1;
      console.log(this.curAnswer.proNum);
    },
    handleQAnswerCon() {
      this.curAnswer.conNum += 1;
      console.log(this.curAnswer.conNum);
    },
    handleAnswerSubscribe () {
      this.curAnswer.subscribeNum += 1;
      console.log(this.curAnswer.subscribeNum);
    },
  },
}

</script>

<style>
.header, .footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
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
  text-align: center;
  line-height: 160px;
}

.Question {
  margin-bottom: 40px;
}

.Answer {
  margin-top: auto;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>

