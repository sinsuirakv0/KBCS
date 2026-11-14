# 00af9fac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af9fac",
  "name": "FUN_00af9fac",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb4524da859cc6f889d0412da9eca0e74e0eff67a5956e065899a093dfeef41a",
  "source_text_sha256": "bb4524da859cc6f889d0412da9eca0e74e0eff67a5956e065899a093dfeef41a"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)
- [00af45b0](../00af4/00af45b0.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af9fac(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00af9fb0 to 00bf9fb7 has its CatchHandler @ 00afa218 */
                    /* try { // try from 00af9fb8 to 00bfa02f has its CatchHandler @ 00af9cac */
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8499c) = param_3;
  return;
}

~~~
