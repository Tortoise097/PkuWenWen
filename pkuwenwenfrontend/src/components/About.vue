<template>
<div>
    <div id="navbar">
        <router-link to="/">Home</router-link> |
        <router-link to="/About">About</router-link> |
        <router-link to="/SignIn">Sign In</router-link> |
        <router-link to="/SignUp">Sign Up</router-link>
    </div>
    <div>
        <img alt="Vue logo" src="../assets/logo.png">
    </div>
    <div>
        <h1>
            this is the About Page of PkuWenWen
        </h1>
        <el-button type="primary" @click="ClickThis()">测试此按钮</el-button>
      <el-table
          :data="tableData"
          style="width: 100%">
        <el-table-column type="expand">
          <template #default="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="问题名称">
                <span>{{ props.row.name }}</span>
              </el-form-item>
              <el-form-item label="所属院系">
                <span>{{ props.row.school }}</span>
              </el-form-item>
              <el-form-item label="问题 ID">
                <span>{{ props.row.id }}</span>
              </el-form-item>
              <el-form-item label="院系 ID">
                <span>{{ props.row.schoolId }}</span>
              </el-form-item>
              <el-form-item label="问题分类">
                <span>{{ props.row.category }}</span>
              </el-form-item>
              <el-form-item label="问题描述">
                <span>{{ props.row.desc }}</span>
              </el-form-item>
              <el-form-item label="热度">
                <span>{{ props.row.rate }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column
            label="问题 ID"
            prop="id">
        </el-table-column>
        <el-table-column
            label="问题名称"
            prop="name">
        </el-table-column>
        <el-table-column
            label="问题描述"
            prop="desc">
        </el-table-column>
        <el-table-column
            label="热度"
            prop="rate">
        </el-table-column>
        <el-table-column
            align="right">
          <template #header>
            <el-input
                v-model="search"
                size="mini"
                placeholder="输入关键字搜索"/>
          </template>
        </el-table-column>
      </el-table>
    </div>
</div>
</template>

<script>
export default{
    data() {
      return {
        tableData: [{
          id: '12987122',
          name: '这里是问题名',
          category: '数学题（问题类别）',
          desc: '以及简介',
          school: '这里是院系名',
          schoolId: '10333',
          rate: 12
        }, {
          id: '12987122',
          name: '这里是问题名',
          category: '数学题（问题类别）',
          desc: '以及简介',
          school: '这里是院系名',
          schoolId: '10333',
          rate: 12
        }, {
          id: '12987122',
          name: '这里是问题名',
          category: '数学题（问题类别）',
          desc: '以及简介',
          school: '这里是院系名',
          schoolId: '10333',
          rate: 12
        }, {
          id: '12987122',
          name: '这里是问题名',
          category: '数学题（问题类别）',
          desc: '以及简介',
          school: '这里是院系名',
          schoolId: '10333',
          rate: 12
        }],
        search: '',
      }
    },
    methods: {
        ClickThis(){
            alert("you click this!");
        },
    },
};

</script>

<style>
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>
