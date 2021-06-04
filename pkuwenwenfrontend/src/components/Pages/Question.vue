<template>
<div>
  <h1>This is the ViewAnswer view</h1>
    <div class="common-layout">

      <el-container class="Question">
        <el-aside class="aside" width="200px">{{ curQuestion['publisher'] }}</el-aside>
        <el-container>
          <el-header class="header">{{ curQuestion['title'] }}</el-header>
          <el-main class="main">{{ curQuestion['detail'] }}</el-main>
          <el-footer class="footer">
            <el-button type="primary" plain @click="handleQuestionPro"><i class="el-icon-circle-check el-icon--left"></i>{{curQuestion.proNum}}赞</el-button>
            <el-button type="danger" plain @click="handleQuestionCon"><i class="el-icon-circle-close el-icon--left"></i>{{curQuestion.conNum}}踩</el-button>
            <el-button type="warning" plain @click="handleQuestionSubscribe()"><i class="el-icon-star-off el-icon--left"></i>{{curQuestion.subscribeNum}}收藏</el-button>
          </el-footer>
        </el-container>
      </el-container>

      <el-container class="Answer">
        <el-aside class="aside" width="200px">{{ curAnswer['publisher'] }}</el-aside>
        <el-container>
          <el-header class="header">{{ curAnswer['title'] }}</el-header>
          <el-main class="main">{{ curAnswer['detail'] }}</el-main>
          <el-footer class="footer">
            <el-button type="primary" plain @click="handleAnswerPro"><i class="el-icon-circle-check el-icon--left"></i>{{curAnswer.proNum}}赞</el-button>
            <el-button type="danger" plain @click="handleAnswerCon"><i class="el-icon-circle-close el-icon--left"></i>{{curAnswer.conNum}}踩</el-button>
            <el-button type="warning" plain @click="handleAnswerSubscribe"><i class="el-icon-star-off el-icon--left"></i>{{curAnswer.subscribeNum}}收藏</el-button>
          </el-footer>
        </el-container>
      </el-container>

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
      curQuestion: 'CurQuestion',//JSON.parse(this.$route.params.curQuestion.toString()),
          // {
          // publisher: '',
          // title: '',
          // detail: '',
          // proNum: 0,
          // conNum: 0,
          // subscribeNum: 0,
          // },
      curAnswer:'CurAnswer', //JSON.parse(this.$route.params.curAnswer.toString()),
          //   {
          //   publisher: '',
          //   title: '',
          //   detail: '',
          //   proNum: 0,
          //   conNum: 0,
          //   subscribeNum: 0,
          // }
    }
  },
  methods: { //TODO： 把这里这些纯前端的methods和后端交互起来， 存到数据库里（暂时不考虑读写锁的问题吧，想想就有坑）
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
    handleAnswerCon() {
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

