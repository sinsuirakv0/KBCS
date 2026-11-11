# 00afb9dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afb9dc",
  "name": "FUN_00afb9dc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "743a3ff46077503980af42a7b466d2322a6d925f7e3509b1154e2caf87d6ad9a",
  "source_text_sha256": "743a3ff46077503980af42a7b466d2322a6d925f7e3509b1154e2caf87d6ad9a"
}
~~~

## 呼び出し元

- [005f2d68](../005f2/005f2d68.md)
- [00700af8](../00700/00700af8.md)
- [00707ee0](../00707/00707ee0.md)
- [00715500](../00715/00715500.md)
- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 385 bytes

~~~c

undefined4 FUN_00afb9dc(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afb9dc to 00bfb9e7 has its CatchHandler @ 00afca94 */
                    /* try { // try from 00afb9e8 to 00bfba27 has its CatchHandler @ 00afb44c */
  lVar1 = FUN_008514f8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849bc);
}

~~~
