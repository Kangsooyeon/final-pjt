<template>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-12 d-flex flex-column my-3">
        <h2 class="title">게시글 목록</h2>
        

        <div class="filter d-flex ml-auto">
          <div class="my-2 mx-2">
            <select v-model="searchType" class="form-control form-control-sm">
              <option value="" selected>전체게시글▼</option>
              <option value="nickname">닉네임</option>
              <option value="title">제목</option>
              <option v-if="store.isLogin" value="my">내가 쓴글</option>
            </select>
          </div>
          <div class="my-2 mx-2">
            <input type="text" v-model="searchKeyword" placeholder="검색어를 입력하세요" class="form-control form-control-sm">
          </div>

          <button @click="search" class="mx-2 btn btn-primary btn-sm my-2">검색</button>
        </div>
      </div>
    </div>

    <div v-if="store.boardListT.length > 0" class="d-flex flex-column justify-content-between align-items-center prtable">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
            <th scope="col">작성일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="article in store.boardListT[store.pagenumL]" :key="article.id">
            <td @click="goArticle(article)" class="articleTitle">{{ article.title }}</td>
            <td>{{ article.nickname }}</td>
            <td>{{ formatDate(article.created_at) }}
              <span v-if="isNew(article.created_at)" class="text-danger ms-2">New</span>
            </td>
          </tr>
        </tbody>
      </table>
      
      <div class="d-flex flex-column btns">
        <button @click="createArticle" class="btn btn-outline-primary ms-auto me-2 mb-3">게시글 생성</button>
        <nav aria-label="Page navigation example" class="d-flex flex-row justify-content-center align-items-center">
          <ul class="pagination ms-auto me-auto">
            <li class="page-item" :class="{ 'disabled': store.pagenumL === 0 }">
              <span class="page-link" @click="pageDown">Previous</span>
            </li>
            <li class="page-item" v-for="(arr, idx) in store.boardListT" :key="idx" :class="{ 'active': store.pagenumL === idx }">
              <span class="page-link" @click="pageSelector(idx)">{{ idx + 1 }}</span>
            </li>
            <li class="page-item" :class="{ 'disabled': store.pagenumL === store.boardListT.length - 1 }">
              <span class="page-link" @click="pageUp">Next</span>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <div v-else>
      <p>검색 결과가 없습니다.</p>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useProjectStore();
const searchKeyword = ref('');
const searchType = ref('');
const today = new Date();

const pageDown = () => {
  if (store.pagenumL > 0) {
    store.pagenumL--;
  }
};
const pageUp = () => {
  if (store.pagenumL < store.boardListT.length - 1) {
    store.pagenumL++;
  }
};
const pageSelector = (idx) => {
  store.pagenumL = idx;
};

const search = () => {
  if (searchType.value.length > 0 || searchKeyword.value.length==0) {
    store.boardListC = store.boardList.filter(article => {
      if (searchType.value === 'nickname') {
        return article.nickname.includes(searchKeyword.value);
      } else if (searchType.value === 'title') {
        return article.title.includes(searchKeyword.value);
      } else if(searchType.value === 'my'){
        return article.nickname.includes(store.userInfo.nickname);
      }else{
        return true
      }
    });
    store.boardListC.reverse();
    store.boardListT = store.boardListC.reduce((acc, cur, idx) => {
      if (idx % 10 === 0) {
        acc.push([cur]);
      } else {
        acc[acc.length - 1].push(cur);
      }
      return acc;
    }, []);
    store.pagenumL = 0;
  }
};

const createArticle = () => {
  if (store.isLogin) {
    router.push('/article/create');
  } else {
    alert('로그인이 필요합니다.');
    router.push('/login');
  }
};

const goArticle = (article) => {
  router.push({ name: 'articledetail', params: { id: article.id }, data: article });
};

const isNew = (created_at) => {
  const createdDate = new Date(created_at);
  const diffTime = Math.abs(today - createdDate);
  const diffHours = Math.ceil(diffTime / (1000 * 60 * 60));
  return diffHours <= 3;
};

const formatDate = (dateString) => {
  return dateString ? dateString.substr(0, 10) : '';
};

onMounted(() => {
  store.getBoardList();
  store.pagenumL = 0;
});
</script>

<style scoped>
.container {
  width: 950px;
}
.page-link {
  cursor: pointer;
}
.onEffect:hover {
  cursor: pointer;
  color: #007bff;
}
.title {
  font-weight: 600;
}
.field {
  color: #007bff;
}
.titleField {
  width: 350px;
}
.bankField {
  width: 210px;
}
.prtable {
  height: 600px;
}
.btn {
  width: 120px;
}
.articleTitle {
  cursor: pointer;
}
.articleTitle:hover {
  text-decoration: underline;
}
.btns{
  width: 100%;
}
</style>
