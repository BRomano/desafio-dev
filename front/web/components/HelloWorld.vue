<template>
  <div class="content-box">
    <h1>{{ msg }}</h1>

    <div class="content-area">
      <h2> Adicione seu arquivo aqui</h2>
      <div class="upload_box">
        <span @click="$refs.file.click()" v-if="!uploadFile"> click here to upload</span>
        <div v-else>
          <span @click="uploadFile=null" class="x-button"> X </span>
          <span> File name: {{ uploadFile.name }} </span>
        </div>

        <input type="file" id="upload" ref="file" @input="changeInputFile" accept="text/plain" style="display: none">
        <button @click="submitCNAB" :disabled="!uploadFile"> Submit </button>
      </div>

      <h2> Lista de Lojas e saldo</h2>

      <div v-if="store" @click="listEntries" class="transaction-store-header">
        <div class="justify-center" style="width: 20%" @click.stop="listEntries">
          <span style="background-color: rgba(89,255,0,0.56); margin: 2px; padding: 2px; font-size: 12px; border-radius: 4px;">
            Voltar
          </span>
        </div>
        <div>
          Loja: {{ store.storeName }}
        </div>
        <div>
          Saldo: {{ totalValue | value }}
        </div>
      </div>

    <!-- STORE or Transaction     -->
      <div :class="{'transaction-grid': store, 'store-grid': !store}">
        <!--   HEADER     -->
        <div class="store-header" v-if="!store">
            <div class="justify-start" style="width: 50%">
              <span>
                Store Name
              </span>
            </div>
            <div class="justify-start" style="width: 30%">
              <span>
                Value
              </span>
            </div>
            <div class="justify-center" style="width: 20%">
              <span>
                Action
              </span>
            </div>
        </div>
        <div class="store-header" v-else>
          <div class="justify-start" style="width: 30%">
              <span>
                Store Owner
              </span>
            </div>
          <div class="justify-start" style="width: 20%">
              <span>
                CPF
              </span>
            </div>
          <div class="justify-center" style="width: 20%">
              <span>
                Date
              </span>
            </div>
          <div class="justify-center" style="width: 15%">
              <span>
                Type
              </span>
            </div>
          <div class="justify-center" style="width: 15%">
              <span style="font-size: 16px">
                Value
              </span>
            </div>
        </div>

        <!--    BODY    -->
        <div v-for="item in stores" :key="item.id" class="store-body-row" :class="{'bg-red': item.value < 0, 'bg-green': item.value > 0}">
          <template v-if="!store">
            <div class="justify-start" style="width: 50%">
              <span>
                # {{ item.id }} - {{ item.storeName }}
              </span>
            </div>
            <div class="justify-start" style="width: 30%">
              <span>
                {{ item.value | value }}
              </span>
            </div>
            <div class="justify-center" style="width: 20%" @click="openStore(item)">
              <span style="background-color: rgba(89,255,0,0.56); margin: 2px; padding: 2px; font-size: 12px; border-radius: 4px;">
                open
              </span>
            </div>
          </template>
          <template v-else>
            <div class="justify-start" style="width: 30%">
              <span>
                # {{ item.id }} - {{ item.storeOwner }}
              </span>
            </div>
            <div class="justify-start" style="width: 20%">
              <span>
                {{ item.cpf | cpf }}
              </span>
            </div>
            <div class="justify-center" style="width: 20%">
              <span>
                {{ item.occurrenceAt | to_date }}
              </span>
            </div>
            <div class="justify-center" style="width: 15%">
              <span style="font-size: 12px">
                {{ item.transactionTypeStr }}
              </span>
            </div>
            <div class="justify-center" style="width: 15%">
              <span style="font-size: 16px">
                {{ item.value | value }}
              </span>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import byCoderService from '@/services/bycoders';
import ResponseData from '@/types/ResponseData';
import Cnab from '@/types/Cnab';

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;

  private uploadFile: null | File = null;

  private message?: string = undefined;

  private stores: Array<Cnab> = [];

  private store?: Cnab;

  get totalValue() {
    const valueSum = this.stores.reduce((sum, item) => sum + item.value, 0);
    return valueSum;
  }

  changeInputFile(e: any) {
    const file = e.target.files || e.dataTransfer.files;

    // eslint-disable-next-line prefer-destructuring
    this.uploadFile = file[0];
    e.currentTarget.value = '';
  }

  submitCNAB(): Promise<any> {
    if (!this.uploadFile) {
      // eslint-disable-next-line prefer-promise-reject-errors
      return Promise.reject(false);
    }

    return byCoderService.upload(this.uploadFile).then(() => {
      this.uploadFile = null;
      this.message = 'Successfully uploaded';
      return this.listEntries();
    });
  }

  listEntries(): Promise<any> {
    return byCoderService.listEntries().then((response: ResponseData) => {
      this.stores = response.data;
      this.store = undefined;
      return true;
    });
  }

  openStore(store: Cnab): Promise<any> {
    this.store = store;
    return byCoderService.listStoreTransactions(this.store.id).then((response: ResponseData) => {
      this.stores = response.data;
      return true;
    });
  }

  mounted() {
    this.listEntries().catch((error) => {
      // console.log(error);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }

  .content-box {
    width: 64rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    &.content-area {
      width: 90% !important;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
  }

  .upload_box {
    width: 100%;
    height: 3rem;
    display: flex;
    justify-content: space-around;
    align-items: center;
    text-align: center;

    border-width: 1px;
    border-style: solid;
    border-color: darkgrey;
    cursor: pointer;

    .x-button {
    border-width: 1px;
    border-style: solid;
    border-color: red;

    &:hover {
      background-color: red;
      border-color: darkgrey;
    }
  }
  }

  .store-grid {
    width: 32rem;
  }

  .transaction-grid {
    width: 48rem;
  }

  .store-header {
    width: 100%;
    height: 28px;
    display: flex;
    justify-content: space-around;
    align-items: center;

    border-width: 0;
    border-bottom-width: 1px;
    border-style: solid;
    border-color: darkgrey;
  }

  .store-body-row {
    width: 100%;
    height: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    //background-color: lightgrey;
    &:nth-child(even) {
      background-color: lightgrey;
    }

    .justify-start {
      display: flex;
      justify-content: flex-start;
    }

    .justify-center {
      display: flex;
      justify-content: center;
    }
  }

  .bg-red {
    background-color: rgba(255, 0, 0, 0.5) !important;
  }
  .bg-green {
    background-color: rgba(144, 238, 144, 0.48) !important;
  }

  .transaction-store-header {
    height: 32px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-width: 2px 0px;
    border-style: solid
  }
</style>
