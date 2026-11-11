# 00afba1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afba1c",
  "name": "FUN_00afba1c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e01048c240c15e247360929d91636d7dde5ff39faad2f0116be292467c23eba",
  "source_text_sha256": "5e01048c240c15e247360929d91636d7dde5ff39faad2f0116be292467c23eba"
}
~~~

## 呼び出し元

- [00700af8](../00700/00700af8.md)
- [007102d8](../00710/007102d8.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00afba1c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00afba28 to 00bfba33 has its CatchHandler @ 00afca78 */
                    /* try { // try from 00afba34 to 00bfbbab has its CatchHandler @ 00afb44c */
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849bc) = param_3;
  return;
}

~~~
