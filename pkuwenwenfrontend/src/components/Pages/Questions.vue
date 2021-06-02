<template>
  <h1>This is the Questions view</h1>
  <div class="">
    <div class="container">
      <el-tabs v-model="message">
        <el-tab-pane :label="`全部问题(${unread.length})`" name="first">
          <el-table :data="unread" :show-header="false" style="width: 100%">
            <el-table-column>
              <template #default="scope">
                <span class="message-title"><router-link to="/Questions/IWantToUseVarHere">{{scope.row.title}}</router-link></span>
              </template>
            </el-table-column>
            <el-table-column prop="content" width="180"></el-table-column>
            <el-table-column width="540">
              <el-form-item label="文本框">
                <el-input title="高赞回复" type="textarea" autosize rows="5" v-model="form.desc"></el-input>
              </el-form-item>
            </el-table-column>
            <el-table-column prop="stars" width="180"></el-table-column>
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
                  <span class="message-title">{{scope.row.title}}</span>
                </template>
              </el-table-column>
              <el-table-column prop="content" width="180"></el-table-column>
              <el-table-column width="540">
                <el-form-item label="文本框">
                  <el-input title="高赞回复" type="textarea" autosize rows="5" v-model="form.desc"></el-input>
                </el-form-item>
              </el-table-column>
              <el-table-column prop="stars" width="180"></el-table-column>
              <el-table-column prop="date" width="180"></el-table-column>
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
        title: 'Question1',
        content: "描述1",
        stars: "233",
        link: 'q1',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: 'Question2',
        content: "描述2",
        stars: "61",
        link: 'q2',
      }],
      read: [{
        date: '更新于 2021-04-19 20:00:00',
        title: 'Question3',
        content: "描述3",
        stars: "618",
        link: 'q3',
      },{
        date: '更新于 2021-04-19 20:00:00',
        title: 'Question4',
        content: "描述4",
        stars: "604",
        link: 'q4',
      }],
      form: {
        desc: '这里应该有高赞回复的内容\n而且这个输入框是可以随着内容数量的变化改变大小的',
      }
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
</style>

