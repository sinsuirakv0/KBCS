# 00af9cac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af9cac",
  "name": "FUN_00af9cac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "647df680772a3b5b4982b22e706883aac97283f5e615a5fc7c281fa0fddbe4ae",
  "source_text_sha256": "647df680772a3b5b4982b22e706883aac97283f5e615a5fc7c281fa0fddbe4ae"
}
~~~

## 呼び出し元

- [00a53028](../00a53/00a53028.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 876 bytes

~~~c

undefined4 FUN_00af9cac(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00af9cac to 00bf9d3b has its CatchHandler @ 00af9cac
                       catch() { ... } // from try @ 00af9cac with catch @ 00af9cac
                       catch() { ... } // from try @ 00af9d40 with catch @ 00af9cac
                       catch() { ... } // from try @ 00af9db0 with catch @ 00af9cac
                       catch() { ... } // from try @ 00af9f10 with catch @ 00af9cac
                       catch() { ... } // from try @ 00af9f4c with catch @ 00af9cac
                       catch() { ... } // from try @ 00af9fb8 with catch @ 00af9cac
                       catch() { ... } // from try @ 00afa1b0 with catch @ 00af9cac */
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84cb0);
}

~~~
