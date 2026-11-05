# 00badaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00badaf0.md)

## 関数情報

~~~json
{
  "address": "00badaf0",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07c9a509ff11e6028c3b377785da9f01b7af1ffd09a0c87e5a012ac2f1d15125",
  "source_text_sha256": "07c9a509ff11e6028c3b377785da9f01b7af1ffd09a0c87e5a012ac2f1d15125"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1783 bytes

~~~c

ulong _ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_
                (long param_1,undefined8 param_2,ushort *param_3,ushort *param_4,ulong *param_5,
                uint *param_6,uint *param_7,undefined8 *param_8)

{
  byte bVar1;
  ulong uVar2;
  uint *puVar3;
  ulong uVar4;
  uint uVar5;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x20) >> 2 & 1) != 0)) &&
     ((char)*param_3 == -1)) {
    param_3 = param_3 + (*(char *)((long)param_3 + 1) == -2);
  }
  if (param_3 < (ushort *)((long)param_4 + -1)) {
    uVar4 = *(ulong *)(param_1 + 0x18);
    puVar3 = param_6;
    do {
      param_6 = puVar3;
      if (param_7 <= puVar3) break;
      uVar5 = (uint)*param_3;
      bVar1 = *(byte *)((long)param_3 + 1) & 0xfc;
      if (bVar1 == 0xd8) {
        if ((long)param_4 - (long)param_3 < 4) {
          uVar2 = 1;
          goto LAB_00badbd0;
        }
                    /* catch() { ... } // from try @ 00badd8c with catch @ 00badbb0 */
        if (((*(byte *)((long)param_3 + 3) & 0xfc) != 0xdc) ||
           (uVar5 = ((uint)(byte)param_3[1] | (*(byte *)((long)param_3 + 3) & 3) << 8 |
                    (uVar5 & 0x3ff) << 10) + 0x10000, uVar4 < uVar5)) goto LAB_00badbdc;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00badbdc:
          uVar2 = 2;
          goto LAB_00badbd0;
        }
        uVar2 = 2;
        if (uVar4 < uVar5) goto LAB_00badbd0;
      }
      param_3 = (ushort *)((long)param_3 + uVar2);
      param_6 = puVar3 + 1;
      *puVar3 = uVar5;
      puVar3 = param_6;
    } while (param_3 < (ushort *)((long)param_4 + -1));
  }
  uVar2 = (ulong)(param_3 < param_4);
  puVar3 = param_6;
LAB_00badbd0:
  *param_5 = (ulong)param_3;
  *param_8 = puVar3;
  return uVar2;
}

~~~
