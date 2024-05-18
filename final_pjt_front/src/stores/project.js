import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProjectStore = defineStore('project', () => {
  // 은행
  const banks = ["우리은행","한국스탠다드차타드은행","대구은행","부산은행","광주은행","제주은행","전북은행","경남은행","중소기업은행","한국산업은행","국민은행","신한은행","농협은행주식회사","하나은행","주식회사 케이뱅크","수협은행","주식회사 카카오뱅크","토스뱅크 주식회사"];
  // TopRateCard
  const topRateDeposit = ref(null)
  const topRateSaving = ref(null)
  const getTRDeposit = function () {
    axios({
      method: 'get',
      url:'http://127.0.0.1:8000/products/deposit-products/top_rate/',
    }).then((res) => {
      topRateDeposit.value=res.data
    })
  }
  const getTRSaving = function () {
    axios({
      method: 'get',
      url:'http://127.0.0.1:8000/products/saving-products/top_rate/',
    }).then((res) => {
      topRateSaving.value=res.data
    })}



    //ProductList
    // 예금상품
    const productListD = ref([])
    const productListDR = ref([])
    const productListDRC = ref([])
    const productListDRT = ref([])
    const pagenumD=ref(0)
    const getProductListD= function () {
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/products/deposit-products/',
      }).then((res) => {
        if(productListD.value.length==0){
        productListD.value=res.data
        productListDR.value=productListD.value.map((product) => {
          const result={
            productname:product.deposit_product.fin_prdt_nm,
            bankname:product.deposit_product.kor_co_nm,
            fin_prdt_cd:product.deposit_product.fin_prdt_cd
          }
          product.options.forEach(el => {
            if(el.save_trm%6==0){
              result[el.save_trm]=el.intr_rate
            }
          });
          return result
        })
        for(let i=0;i<productListDR.value.length;i=i+10){
          productListDRT.value.push(productListDR.value.slice(i,i+10))
        }}
        productListDRC.value=productListDR.value
      })}

      // 적금상품
      const productListS = ref([])
      const productListSR = ref([])
      const productListSRC = ref([])
      const productListSRT = ref([])
      const pagenumS=ref(0)
      const getProductListS= function () {
        axios({
          method: 'get',
          url:'http://127.0.0.1:8000/products/saving-products/',
        }).then((res) => {
          if(productListS.value.length==0){
          productListS.value=res.data
          productListSR.value=productListS.value.map((product) => {
            const result={
              productname:product.saving_product.fin_prdt_nm,
              bankname:product.saving_product.kor_co_nm,
              fin_prdt_cd:product.saving_product.fin_prdt_cd
            }
            product.options.forEach(el => {
              if(el.save_trm%6==0){
                result[el.save_trm]=el.intr_rate
              }
            });
            return result
          })
          for(let i=0;i<productListDR.value.length;i=i+10){
            productListSRT.value.push(productListSR.value.slice(i,i+10))
          }}
          productListSRC.value=productListSR.value
        })}

    
  return {
    banks,
    topRateDeposit, getTRDeposit, topRateSaving, getTRSaving ,
    productListD, getProductListD,productListDR,productListDRT,pagenumD,productListDRC,
    productListS, getProductListS,productListSR,productListSRT,pagenumS,productListSRC
  }
})
