# 00babb5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00babb5c",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d17161b59f99e7ffe525def48afae8fe7b5d98e5cd06bceac57d432a55e2a3cc",
  "source_text_sha256": "d17161b59f99e7ffe525def48afae8fe7b5d98e5cd06bceac57d432a55e2a3cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1aa0](../00be1/00be1aa0.md)

## 疑似コード / UTF-8 1479 bytes

~~~c

int _ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m
              (long param_1,mbstate_t *param_2,char *param_3,char *param_4,ulong param_5)

{
  __locale_t __dataset;
  size_t sVar1;
  int iVar2;
  int iVar3;
  ulong uVar4;
  
                    /* try { // try from 00babb68 to 00cabb7f has its CatchHandler @ 00babbd0 */
  iVar3 = 0;
                    /* try { // try from 00babb80 to 00cabd3b has its CatchHandler @ 00bab67c */
  if ((param_5 != 0) && (param_3 != param_4)) {
    iVar3 = 0;
    uVar4 = 1;
    do {
      __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
      sVar1 = mbrlen(param_3,(long)param_4 - (long)param_3,param_2);
                    /* catch() { ... } // from try @ 00babb68 with catch @ 00babbd0 */
      if (__dataset != (__locale_t)0x0) {
        uselocale(__dataset);
      }
      if (sVar1 == 0) {
        sVar1 = 1;
        iVar2 = 1;
      }
      else {
                    /* catch() { ... } // from try @ 00babb58 with catch @ 00babbe8 */
        if (sVar1 + 2 < 2) {
          return iVar3;
        }
        iVar2 = (int)sVar1;
      }
                    /* catch() { ... } // from try @ 00baba44 with catch @ 00babbfc */
      iVar3 = iVar2 + iVar3;
      if (param_5 <= uVar4) {
        return iVar3;
      }
      param_3 = param_3 + sVar1;
      uVar4 = uVar4 + 1;
    } while (param_3 != param_4);
  }
                    /* catch() { ... } // from try @ 00bab8c8 with catch @ 00babc18 */
  return iVar3;
}

~~~
