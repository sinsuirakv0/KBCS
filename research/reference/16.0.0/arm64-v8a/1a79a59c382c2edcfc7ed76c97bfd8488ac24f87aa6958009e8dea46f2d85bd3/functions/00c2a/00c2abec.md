# 00c2abec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c2abec",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE9do_lengthER9mbstate_tPKcS5_m",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b855bd549ed9029714d4888cfb0ac7662c2c19fb5390bf28221661e63553db50",
  "source_text_sha256": "b855bd549ed9029714d4888cfb0ac7662c2c19fb5390bf28221661e63553db50"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1639 bytes

~~~c

int _ZNKSt6__ndk115__codecvt_utf16IDsLb1EE9do_lengthER9mbstate_tPKcS5_m
              (long param_1,undefined8 param_2,char *param_3,long param_4,ulong param_5)

{
  bool bVar1;
  bool bVar2;
  int iVar3;
  ulong uVar4;
  
  iVar3 = (int)param_3;
                    /* try { // try from 00c2ac08 to 00d2ac0f has its CatchHandler @ 00c2ac1c */
                    /* catch() { ... } // from try @ 00c2abac with catch @ 00c2ac10
                       try { // try from 00c2ac10 to 00d2ac47 has its CatchHandler @ 00c2ab20 */
  if (((1 < param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == -1)) {
                    /* catch() { ... } // from try @ 00c2ab94 with catch @ 00c2ac1c
                       catch() { ... } // from try @ 00c2ac08 with catch @ 00c2ac1c */
    param_3 = param_3 + (ulong)(param_3[1] == -2) * 2;
  }
  if ((param_5 != 0) && (param_3 < (char *)(param_4 + -1))) {
    uVar4 = 1;
    do {
                    /* try { // try from 00c2ac48 to 00d2ad47 has its CatchHandler @ 00c2ac48
                       catch() { ... } // from try @ 00c2ac48 with catch @ 00c2ac48
                       catch() { ... } // from try @ 00c2ad90 with catch @ 00c2ac48
                       catch() { ... } // from try @ 00c2ae88 with catch @ 00c2ac48 */
      if ((param_3[1] & 0xf8U) == 0xd8) break;
      bVar1 = (ulong)CONCAT11(param_3[1],*param_3) <= *(ulong *)(param_1 + 0x10);
      param_3 = param_3 + (ulong)bVar1 * 2;
      bVar2 = uVar4 < param_5;
      uVar4 = uVar4 + 1;
    } while ((bVar1 && param_3 < (char *)(param_4 + -1)) && bVar2);
  }
  return (int)param_3 - iVar3;
}

~~~
