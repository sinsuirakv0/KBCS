# 00a9cafc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a9cafc.md)

## 関数情報

~~~json
{
  "address": "00a9cafc",
  "name": "FUN_00a9cafc",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a0ce875e1e856e3db6e38bc508f931e76c49af51a87af911841d557fad1ffd42",
  "source_text_sha256": "a0ce875e1e856e3db6e38bc508f931e76c49af51a87af911841d557fad1ffd42"
}
~~~
## 呼び出し元

- [006dde48](../006dd/006dde48.md)
- [006ddfb8](../006dd/006ddfb8.md)
- [006e3f80](../006e3/006e3f80.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 489 bytes

~~~c

undefined4 FUN_00a9cafc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00a9cb0c to 00b9cb0f has its CatchHandler @ 00a9d544 */
                    /* try { // try from 00a9cb10 to 00b9cb5b has its CatchHandler @ 00a9a654 */
  lVar1 = FUN_0081f580();
  return *(undefined4 *)
          (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec +
           (long)*(int *)(&DAT_002f4804 + (long)param_3 * 4) * 4 + 0x84080);
}

~~~
